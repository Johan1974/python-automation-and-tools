# Python Auto File Organizer 🗂️🐍 — Automatic Folder Sorting CLI

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/python_auto_file_organizer_ci.yml/badge.svg)

**Python Auto File Organizer** is a lightweight Python CLI tool to **automatically organize files** in any folder by **file type (extension)** or **modification date**.
Keep your **downloads, project folders, or shared directories** clutter-free without manual effort. Ideal for **developers, data analysts, freelancers, and productivity enthusiasts**.

**GitHub Repository:** [Python Automation & Tools — Auto File Organizer](https://github.com/Johan1974/python-automation-and-tools/tree/main/python-auto-file-organizer)

---

## 📸 Screenshot / Preview

**Original folder (`test_folder/`):**

```
document.pdf
image.png
notes.txt
photo.jpg
script.py
```

**Organized by extension:**

```
jpg/
└── photo.jpg
pdf/
└── document.pdf
png/
└── image.png
py/
└── script.py
txt/
└── notes.txt
```

**Organized by date (`YYYY-MM-DD` folders):**

```
2026-01-02/
├── document.pdf
├── image.png
├── notes.txt
├── photo.jpg
└── script.py
```

![Auto File Organizer Preview](screenshots/preview.png)

---

## 💡 Benefits of Using This Tool

* ✅ **Save time** — automate manual folder cleanup
* ✅ **Reduce clutter** — organize large download or project folders quickly
* ✅ **Flexible sorting** — by **file type** or **last modification date**
* ✅ **Safe handling** — avoids overwriting files
* ✅ **Dry-run mode** — preview changes before applying
* ✅ **Repeatable testing** — reset folders with a single command
* ✅ **Cross-platform** — works on **Windows, macOS, and Linux**

---

## 🎮 Features

* Organize by **file extension** (`.pdf`, `.jpg`, `.txt`, etc.)
* Organize by **modification date** (`YYYY-MM-DD`)
* **Dry-run mode** to preview changes
* **Reset function** to restore original test folder
* **Safe file moves** with automatic renaming to prevent conflicts
* **Lightweight CLI** with optional CI integration for automated testing

---

## 🛠 Requirements

* Python 3.8+
* No additional Python packages required

---

## 🚀 Installation

```bash
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools/python-auto-file-organizer
```

---

## Usage Examples

### 🔹 Preview Changes (Dry-Run)

```bash
python3 auto_cleanup.py -s test_folder --mode extension --dry-run
```

### 📂 Organize by File Type (Extension)

```bash
python3 auto_cleanup.py -s test_folder --mode extension
```

### 📅 Organize by Modification Date

```bash
python3 auto_cleanup.py -s test_folder --mode date
```

### 🔄 Reset Test Folder

```bash
python3 auto_cleanup.py -s test_folder --reset
```

---

## 🧪 Running Tests Locally

```bash
python3 auto_cleanup.py -s test_folder --mode extension --dry-run
python3 auto_cleanup.py -s test_folder --mode date --dry-run
python3 auto_cleanup.py -s test_folder --reset
```

---

## ❓ FAQ

**Q1: Can I organize folders with thousands of files?**
Yes — the script handles large folders efficiently and safely, with automatic renaming to prevent overwrites.

**Q2: Will it work on Windows, macOS, and Linux?**
Yes — fully cross-platform.

**Q3: Can I customize folder names?**
Currently it uses **extensions** or **modification dates**, but the roadmap includes **custom folder rules**.

**Q4: What if files have no extensions?**
They are placed in a folder named `no_extension`.

**Q5: Can I preview before moving files?**
Yes — use `--dry-run` mode to see exactly what will happen.

---

## ⚙️ CI/CD Pipeline

GitHub Actions automatically tests:

* Organizing by extension
* Organizing by date
* Resetting test folder
* Temporary folder validation

Workflow file: `.github/workflows/python_auto_file_organizer_ci.yml`

---

## 🤝 Contributing

Enhancements, bug fixes, and feature requests are welcome:

* Improved organization logic
* Additional CLI options or logging
* Nested folder sorting or GUI integration

1. Fork the repo
2. Create a feature branch
3. Submit a pull request

All PRs are automatically validated with CI.

---

## 📅 Roadmap

* Nested folder sorting
* Custom folder naming rules
* Logging and reporting of file moves
* Optional GUI interface
* Web-based Flask/FastAPI version
* Publish to PyPI (`pip install auto-file-organizer`)

---

## 📬 Freelance & Custom Automation

I build **custom file automation tools, CLI utilities, and workflow scripts**.
Contact via GitHub: **[https://github.com/Johan1974](https://github.com/Johan1974)**

---

## 📝 License

MIT License — free to use, modify, and distribute

