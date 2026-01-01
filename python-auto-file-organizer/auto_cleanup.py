#!/usr/bin/env python3
"""
auto_cleanup.py

A Python script to automatically organize files in a folder
by extension or modification date, with optional destination folder
and reset functionality.

Features:
- Configurable source folder
- Optional destination folder (safe testing or packaging)
- Sort by extension or date
- Safe file handling to prevent overwriting
- Dry-run mode
- Reset test folder to original sample files
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import argparse

# Original sample files for reset
SAMPLE_FILES = ["document.pdf", "photo.jpg", "script.py", "notes.txt", "image.png"]

def get_args():
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(
        description="Organize files in a folder by extension or date, or reset it."
    )
    parser.add_argument(
        "-s", "--source",
        type=str,
        required=True,
        help="Path to the source folder to organize"
    )
    parser.add_argument(
        "-d", "--destination",
        type=str,
        help="Optional destination folder (default: organize in-place)"
    )
    parser.add_argument(
        "-m", "--mode",
        choices=["extension", "date"],
        default="extension",
        help="Sorting mode: 'extension' or 'date' (default: extension)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without moving files"
    )
    parser.add_argument(
        "--reset",
        action="store_true",
        help="Reset the folder to original sample files"
    )
    return parser.parse_args()

def safe_move(file_path: Path, target_folder: Path, dry_run=False):
    """Move a file safely, avoiding overwriting by appending a counter."""
    target_folder.mkdir(parents=True, exist_ok=True)
    target_file = target_folder / file_path.name
    counter = 1
    while target_file.exists():
        target_file = target_folder / f"{file_path.stem}_{counter}{file_path.suffix}"
        counter += 1
    if dry_run:
        print(f"[Dry Run] Would move: {file_path} -> {target_file}")
    else:
        shutil.move(str(file_path), str(target_file))
        print(f"Moved: {file_path} -> {target_file}")

def organize_by_extension(source_folder: Path, destination_folder: Path, dry_run=False):
    """Organize files into folders by extension."""
    for item in source_folder.iterdir():
        if item.is_file():
            ext = item.suffix[1:] if item.suffix else "no_extension"
            target_folder = destination_folder / ext
            safe_move(item, target_folder, dry_run=dry_run)

def organize_by_date(source_folder: Path, destination_folder: Path, dry_run=False):
    """Organize files into folders by last modification date (YYYY-MM-DD)."""
    for item in source_folder.iterdir():
        if item.is_file():
            mod_time = datetime.fromtimestamp(item.stat().st_mtime)
            date_folder = mod_time.strftime("%Y-%m-%d")
            target_folder = destination_folder / date_folder
            safe_move(item, target_folder, dry_run=dry_run)

def reset_folder(folder: Path):
    """Reset folder to original sample files."""
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
    print(f"'{folder}' has been reset to original state.")

def main():
    args = get_args()
    source = Path(args.source)
    destination = Path(args.destination) if args.destination else source

    if args.reset:
        reset_folder(source)
        return

    if not source.exists() or not source.is_dir():
        print(f"Error: '{source}' is not a valid folder")
        return

    if args.mode == "extension":
        organize_by_extension(source, destination, dry_run=args.dry_run)
    else:
        organize_by_date(source, destination, dry_run=args.dry_run)

if __name__ == "__main__":
    main()
