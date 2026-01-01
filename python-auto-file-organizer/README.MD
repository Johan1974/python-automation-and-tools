# Python Auto File Organizer 🗂️🐍

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/python_auto_file_organizer_ci.yml/badge.svg)

**Python Auto File Organizer** is a Python CLI tool that automatically organizes files in a folder by **extension** or **modification date**.
Perfect for **developers, data analysts, and productivity enthusiasts** who want to keep folders tidy without manual effort.

**GitHub Repository:**
[https://github.com/Johan1974/python-automation-and-tools/tree/main/python-auto-file-organizer](https://github.com/Johan1974/python-automation-and-tools/tree/main/python-auto-file-organizer)

---

## 📸 Screenshot / Preview

**Before organizing:**

```
test_folder/
├── document.pdf
├── image.png
├── notes.txt
├── photo.jpg
└── script.py
```

**After organizing by extension:**

```
by_extension/
├── jpg/
│   └── photo.jpg
├── pdf/
│   └── document.pdf
├── png/
│   └── image.png
├── py/
│   └── script.py
└── txt/
    └── notes.txt
```

**After organizing by date:**

```
by_date/
└── 2026-01-02/
    ├── document.pdf
    ├── image.png
    ├── notes.txt
    ├── photo.jpg
    └── script.py
```
---

## 💡 Why Use This Tool?

* Save time and keep folders clutter-free
* Organize by **file type** (extension) or **modification date**
* Safe file handling — avoids overwriting
* Dry-run mode to preview changes
* Reset test folders for repeated testing
* Lightweight, fast, automation-friendly CLI

---

## 🎮 Features

* Sort files by **extension** (`.pdf`, `.jpg`, `.txt`, etc.)
* Sort files by **modification date** (`YYYY-MM-DD`)
* Dry-run mode to preview changes without moving files
* Reset function to restore original test folder
* Safe file moves with automatic renaming if conflicts occur
* Optional integration with GitHub Actions for CI testing

---

## 🛠 Requirements

* Python 3.8+
* No additional packages required

---

## 🚀 Installation

Clone the repository and navigate to the tool:

```
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools/python-auto-file-organizer
```

---

## Usage

### 🔹 Dry-Run (Preview Changes)

```
python3 auto_cleanup.py -s test_folder --mode extension --dry-run
```

### 📂 Organize by Extension

```
python3 auto_cleanup.py -s test_folder --mode extension
```

### 📅 Organize by Date

```
python3 auto_cleanup.py -s test_folder --mode date
```

### 🔄 Reset Test Folder

```
python3 auto_cleanup.py -s test_folder --reset
```

---

## 🧪 Running Tests Locally

```
python3 auto_cleanup.py -s test_folder --mode extension --dry-run
python3 auto_cleanup.py -s test_folder --mode date --dry-run
python3 auto_cleanup.py -s test_folder --reset
```

---

## ⚙️ CI/CD Pipeline

GitHub Actions workflow runs on every push:

* Test organization by **extension**
* Test organization by **date**
* Reset folder functionality
* Temporary folder end-to-end validation

Workflow file: `.github/workflows/python_auto_file_organizer_ci.yml`

---

## 🤝 Contributing

Contributions are welcome! Examples include:

* Improved file organization logic
* Enhanced CLI options or logging
* Additional sorting rules or GUI integration

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

All PRs run through CI automatically.

---

## 📅 Roadmap

Planned enhancements:

* Nested folder sorting
* Custom folder naming rules
* Logging and reporting of file moves
* Optional GUI interface
* Web-based Flask/FastAPI version
* Publish to PyPI (`pip install auto-file-organizer`)

---

## 📬 Freelance & Custom Automation

Need a **custom file automation tool**, organization script, or workflow?

I build:

* File organization and cleanup tools
* Batch automation scripts
* CLI or web-based file management utilities

Contact via GitHub: **[https://github.com/Johan1974](https://github.com/Johan1974)**

---

## 📝 License

MIT License — free to use, modify, and distribute
