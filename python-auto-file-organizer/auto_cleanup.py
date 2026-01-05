#!/usr/bin/env python3
"""
auto_cleanup.py

A Python script to automatically organize files in a folder
by extension or modification date, with optional destination folder,
reset functionality, and undo support.

Features:
- Configurable source folder
- Optional destination folder (safe testing or packaging)
- Sort by extension or date
- Safe file handling to prevent overwriting
- Dry-run mode
- Reset test folder to original sample files
- Undo last cleanup
- Logs and prints paths relative to project root
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import argparse
import logging

# --- Project and script paths ---
SCRIPT_DIR = Path(__file__).parent.resolve()  # /.../python-auto-file-organizer
HOME_DIR = Path.home()  # /home/johan

# --- Logging setup ---
LOG_DIR = SCRIPT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "auto_cleanup.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger(__name__)

# Undo log
UNDO_LOG_PATH = LOG_DIR / "undo.log"

# Original sample files
SAMPLE_FILES = ["document.pdf", "photo.jpg", "script.py", "notes.txt", "image.png"]

# --- CLI arguments ---
def get_args():
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by extension or date, with optional reset and undo."
    )
    parser.add_argument("-s", "--source", type=str, required=True,
                        help="Path to the source folder to organize")
    parser.add_argument("-d", "--destination", type=str,
                        help="Optional destination folder (default: organize in-place)")
    parser.add_argument("-m", "--mode", choices=["extension", "date"], default="extension",
                        help="Sorting mode: 'extension' or 'date' (default: extension)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be done without moving files")
    parser.add_argument("--reset", action="store_true",
                        help="Reset the folder to original sample files")
    parser.add_argument("--undo", action="store_true",
                        help="Undo the last cleanup")
    return parser.parse_args()

# --- Helper: print paths relative to project root ---
def project_path(path: Path):
    """Return path starting from project folder, with leading slash."""
    try:
        relative = path.resolve().relative_to(HOME_DIR)
        return Path("/" + str(relative))
    except ValueError:
        return path  # fallback

# --- Safe move with undo support ---
def safe_move(file_path: Path, target_folder: Path, dry_run=False):
    """Move a file safely, avoiding overwriting by appending a counter.
    Record move in undo log if not dry-run."""
    target_folder.mkdir(parents=True, exist_ok=True)
    target_file = target_folder / file_path.name
    counter = 1
    while target_file.exists():
        target_file = target_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
        counter += 1

    if dry_run:
        print(f"[DRY-RUN] {project_path(file_path)} -> {project_path(target_file)}")
        logger.info(f"DRY-RUN: {project_path(file_path)} -> {project_path(target_file)}")
    else:
        shutil.move(str(file_path), str(target_file))
        print(f"Moved: {project_path(file_path)} -> {project_path(target_file)}")
        logger.info(f"Moved: {project_path(file_path)} -> {project_path(target_file)}")
        # Record for undo
        with open(UNDO_LOG_PATH, "a") as f:
            f.write(f"{target_file}|{file_path}\n")  # target_file -> original location

# --- Organize functions ---
def organize_by_extension(source_folder: Path, destination_folder: Path, dry_run=False):
    for item in source_folder.iterdir():
        if item.is_file():
            ext = item.suffix[1:] if item.suffix else "no_extension"
            target_folder = destination_folder / ext
            safe_move(item, target_folder, dry_run=dry_run)

def organize_by_date(source_folder: Path, destination_folder: Path, dry_run=False):
    for item in source_folder.iterdir():
        if item.is_file():
            mod_time = datetime.fromtimestamp(item.stat().st_mtime)
            date_folder = mod_time.strftime("%Y-%m-%d")
            target_folder = destination_folder / date_folder
            safe_move(item, target_folder, dry_run=dry_run)

# --- Reset folder ---
def reset_folder(folder: Path):
    if not folder.exists():
        folder.mkdir(parents=True)

    # Remove all subfolders
    for item in folder.iterdir():
        if item.is_dir():
            shutil.rmtree(item)

    # Remove unexpected files
    for item in folder.iterdir():
        if item.is_file() and item.name not in SAMPLE_FILES:
            item.unlink()

    # Recreate original sample files
    for file_name in SAMPLE_FILES:
        file_path = folder / file_name
        if not file_path.exists():
            file_path.touch()

    # Clear undo log
    if UNDO_LOG_PATH.exists():
        UNDO_LOG_PATH.unlink()

    print(f"'{project_path(folder)}' has been reset to original state.")
    logger.info(f"Reset folder: {project_path(folder)}")


def remove_empty_folders(folder: Path):
    for subfolder in folder.iterdir():
        if subfolder.is_dir():
            remove_empty_folders(subfolder)
            if not any(subfolder.iterdir()):  # folder is empty
                subfolder.rmdir()

# --- Undo last cleanup ---
def undo_cleanup(dry_run=False):
    if not UNDO_LOG_PATH.exists():
        print("No undo history found.")
        logger.info("Undo attempted but no history found.")
        return

    with open(UNDO_LOG_PATH, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    for line in reversed(lines):  # reverse order to prevent conflicts
        target_str, original_str = line.split("|")
        target_path = Path(target_str)
        original_path = Path(original_str)

        if target_path.exists() or dry_run:
            if not dry_run:
                original_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(target_path), str(original_path))
            print(f"{'[DRY-RUN] ' if dry_run else 'Undo: '} {project_path(target_path)} -> {project_path(original_path)}")
            logger.info(f"{'DRY-RUN: ' if dry_run else 'Undo: '} {project_path(target_path)} -> {project_path(original_path)}")

    if not dry_run and UNDO_LOG_PATH.exists():
        UNDO_LOG_PATH.unlink()
        print("Undo completed.")
        logger.info("Undo completed and log cleared.")

# --- Main ---
def main():
    args = get_args()

    # Resolve absolute paths
    source = (Path(args.source) if Path(args.source).is_absolute() else SCRIPT_DIR / args.source).resolve()
    destination = (Path(args.destination) if args.destination else source).resolve()

    # Reset
    if args.reset:
        reset_folder(source)
        return

    # Undo
    if args.undo:
        undo_cleanup(dry_run=args.dry_run)
        remove_empty_folders(source)
        return

    # Validate folder
    if not source.exists() or not source.is_dir():
        print(f"Error: '{source}' is not a valid folder")
        return

    logger.info(f"Started cleanup | mode={args.mode} | dry_run={args.dry_run} | source={source}")

    # Perform cleanup
    if args.mode == "extension":
        organize_by_extension(source, destination, dry_run=args.dry_run)
    else:
        organize_by_date(source, destination, dry_run=args.dry_run)

    logger.info("Cleanup completed")

if __name__ == "__main__":
    main()
