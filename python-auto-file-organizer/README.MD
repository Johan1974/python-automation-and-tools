
# Python Auto File Organizer 🗂️🐍

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/python_auto_file_organizer_ci.yml/badge.svg)

**Python Auto File Organizer** is a Python CLI tool to automatically organize files in a folder by **extension** or **modification date**.
Ideal for **developers, data analysts, and productivity enthusiasts** who want clutter-free folders with minimal effort.

**GitHub Repository:**
[https://github.com/Johan1974/python-automation-and-tools/tree/main/python-auto-file-organizer](https://github.com/Johan1974/python-automation-and-tools/tree/main/python-auto-file-organizer)

---

## 📸 Screenshot / Preview


**Preview Screenshot:**

![Auto File Organizer Preview](screenshots/preview.png)
*Shows organized folder structure after running the tool.*

---

## 💡 Why Use This Tool?

* Save hours of manual file sorting
* Organize by **file type** or **modification date**
* Safe file handling — avoids overwriting existing files
* Dry-run mode previews changes before moving files
* Reset test folders for repeated testing
* Lightweight, fast, automation-friendly CLI

---

## 🎮 Features

* Sort files by **extension** (`.pdf`, `.jpg`, `.txt`, etc.)
* Sort files by **modification date** (`YYYY-MM-DD`)
* Dry-run mode to preview planned moves
* Reset function to restore original test folder
* Safe file moves with automatic renaming if conflicts occur
* Optional CI integration via GitHub Actions

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

* Validate file organization by **extension**
* Validate organization by **date**
* Test reset functionality
* Full end-to-end validation using a temporary folder

Workflow file: `.github/workflows/python_auto_file_organizer_ci.yml`

---

## 🤝 Contributing

Contributions are welcome! Examples:

* Improve file organization logic
* Add new CLI options or logging
* Enhance sorting rules or add GUI integration

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

All PRs run automatically through CI.

---

## 📅 Roadmap

Planned enhancements:

* Nested folder sorting
* Custom folder naming rules
* Logging and reporting of moved files
* Optional GUI interface
* Web-based Flask/FastAPI version
* Publish to PyPI (`pip install auto-file-organizer`)

---

## 📬 Freelance & Custom Automation

Need a **custom file automation tool**, organization script, or workflow?

I build:

* File organization and cleanup utilities
* Batch automation scripts
* CLI or web-based file management tools

Contact me via GitHub: **[https://github.com/Johan1974](https://github.com/Johan1974)**

---

## 📝 License

MIT License — free to use, modify, and distribute

