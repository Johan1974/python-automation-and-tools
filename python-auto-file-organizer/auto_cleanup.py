#!/usr/bin/env python3
"""
auto_cleanup.py

Automatically organize files in a folder by extension or modification date.

Features:
- Configurable source folder
- Optional destination folder
- Sort by extension or date
- Safe file handling (no overwrite)
- Dry-run mode
- Reset test folder to original sample files
- Logging for audit & debugging
- Undo last cleanup run
"""

import shutil
from pathlib import Path
from datetime import datetime
import argparse
import logging

# -----------------------------
# Logging setup
# -----------------------------
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "auto_cleanup.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# -----------------------------
# Undo log file
# -----------------------------
UNDO_LOG_FILE = LOG_DIR / "undo.log"

# -----------------------------
# Original sample files for reset
# -----------------------------
SAMPLE_FILES = ["document.pdf", "photo.jpg", "script.py", "notes.txt", "image.png"]


# -----------------------------
# CLI Arguments
# -----------------------------
def get_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Organize files by extension or date, with safety features."
    )
    parser.add_argument(
        "-s", "--source",
        required=True,
        help="Path to the source folder"
    )
    parser.add_argument(
        "-d", "--destination",
        help="Optional destination folder (default: organize in-place)"
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["extension", "date"],
        default="extension",
        help="Sorting mode (default: extension)"
    )
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=[],
        help="File extensions to ignore (e.g. .exe .tmp)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview actions without moving files"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset folder to original sample files"
    )
    parser.add_argument(
        "--undo",
        action="store_true",
        help="Revert the last cleanup run"
    )
    return parser.parse_args()


# -----------------------------
# Core Functions
# -----------------------------
def log_undo_move(src: Path, dest: Path):
    """Log a move for possible undo."""
    with UNDO_LOG_FILE.open("a") as f:
        f.write(f"{src}|{dest}\n")


def safe_move(file_path: Path, target_folder: Path, dry_run: bool):
    """Move a file safely, avoiding overwrites."""
    target_folder.mkdir(parents=True, exist_ok=True)
    target_file = target_folder / file_path.name

    counter = 1
    while target_file.exists():
        target_file = target_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
        counter += 1

    if dry_run:
        print(f"[DRY-RUN] {file_path.name} -> {target_file}")
        logger.info(f"DRY-RUN: {file_path} -> {target_file}")
    else:
        shutil.move(str(file_path), str(target_file))
        print(f"Moved: {file_path.name} -> {target_file}")
        logger.info(f"Moved: {file_path} -> {target_file}")
        log_undo_move(file_path, target_file)


def should_skip(file: Path, excluded_exts):
    """Determine whether a file should be skipped."""
    if file.name.startswith("."):
        return True
    if file.suffix.lower() in excluded_exts:
        logger.info(f"Excluded: {file.name}")
        return True
    return False


def organize_by_extension(source: Path, destination: Path, dry_run: bool, excluded_exts):
    """Organize files into folders by extension."""
    for item in source.iterdir():
        if item.is_file() and not should_skip(item, excluded_exts):
            ext = item.suffix[1:] if item.suffix else "no_extension"
            safe_move(item, destination / ext, dry_run)


def organize_by_date(source: Path, destination: Path, dry_run: bool, excluded_exts):
    """Organize files into folders by modification date."""
    for item in source.iterdir():
        if item.is_file() and not should_skip(item, excluded_exts):
            mod_time = datetime.fromtimestamp(item.stat().st_mtime)
            date_folder = mod_time.strftime("%Y-%m-%d")
            safe_move(item, destination / date_folder, dry_run)


def reset_folder(folder: Path):
    """Reset folder to original sample files."""
    folder.mkdir(parents=True, exist_ok=True)

    for item in folder.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        elif item.is_file() and item.name not in SAMPLE_FILES:
            item.unlink()

    for name in SAMPLE_FILES:
        (folder / name).touch(exist_ok=True)

    logger.warning(f"Folder reset: {folder}")
    print(f"'{folder}' has been reset to original state.")


def undo_last_run(dry_run=False):
    """Revert all moves from the last cleanup run."""
    if not UNDO_LOG_FILE.exists():
        print("No undo history found.")
        return

    lines = UNDO_LOG_FILE.read_text().splitlines()
    if not lines:
        print("Undo log is empty.")
        return

    print("Undoing last cleanup run...")
    for line in reversed(lines):
        try:
            src_str, dest_str = line.split("|")
            src, dest = Path(src_str), Path(dest_str)
            if dest.exists():
                if dry_run:
                    print(f"[DRY-RUN] Would move: {dest} -> {src}")
                else:
                    src.parent.mkdir(parents=True, exist_ok=True)
                    shutil.move(str(dest), str(src))
                    print(f"Restored: {dest.name} -> {src}")
            else:
                print(f"Skipped (destination missing): {dest}")
        except Exception as e:
            print(f"Error undoing move {line}: {e}")
    if not dry_run:
        UNDO_LOG_FILE.unlink()
        print("Undo completed and log cleared.")


# -----------------------------
# Main
# -----------------------------
def main():
    args = get_args()

    source = Path(args.source)
    destination = Path(args.destination) if args.destination else source
    excluded_exts = {ext.lower() for ext in args.exclude}

    if args.reset:
        reset_folder(source)
        return

    if args.undo:
        undo_last_run(dry_run=args.dry_run)
        return

    if not source.exists() or not source.is_dir():
        print(f"Error: '{source}' is not a valid folder")
        logger.error(f"Invalid source folder: {source}")
        return

    logger.info(
        f"Started cleanup | mode={args.mode} | dry_run={args.dry_run} | source={source}"
    )

    if args.mode == "extension":
        organize_by_extension(source, destination, args.dry_run, excluded_exts)
    else:
        organize_by_date(source, destination, args.dry_run, excluded_exts)

    logger.info("Cleanup completed")


if __name__ == "__main__":
    main()
