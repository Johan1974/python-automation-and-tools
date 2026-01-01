# Python Automation & Tools 🚀🐍

![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![Tip Calculator CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/tip_calculator_ci.yml/badge.svg)
![Python Auto File Organizer CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/python_auto_file_organizer_ci.yml/badge.svg)

A **professional collection of Python automation scripts and CLI tools** designed for freelancers, startups, and businesses. Automate repetitive tasks, clean and preprocess data, organize files, and prototype solutions quickly. All tools are **ready-to-use, customizable, and portfolio-ready**.

**GitHub Repository:** [https://github.com/Johan1974/python-automation-and-tools](https://github.com/Johan1974/python-automation-and-tools)

---

## 🌟 Featured Projects

| Project                        | Preview                                                                                                               | Example Usage                                                                       | Description                                                                                                                |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Tip Calculator**             | ![CLI Version](tip_calculator/screenshots/cli_version.png) ![Web Version](tip_calculator/screenshots/web_version.png) | `python tip_calculator/calculator.py`                                               | Quickly calculate tips, total bills, and per-person splits. CLI & web app (Flask). Fast, interactive, locale-aware.        |
| **Band Name Generator**        | ![Band Name Generator](band-name-generator/screenshots/sample.png)                                                    | `python band-name-generator/band_name_generator.py`                                 | Generate creative names for bands, businesses, or projects instantly. Ideal for branding and brainstorming.                |
| **CSV Cleaner**                | ![CSV Cleaner Preview](csv-cleaner/screenshots/preview.png)                                                           | `python csv-cleaner/src/cleaner.py --in samples/input/example.csv`                  | Clean, normalize, and prettify CSV files. Remove duplicates, fill missing values, and generate ASCII previews for reports. |
| **Treasure Island**            | ![Treasure Island Preview](treasure_island/screenshots/preview.png)                                                   | `python treasure_island/treasure.py`                                                | Interactive text-based adventure game with branching story paths and ASCII art. Learn Python fundamentals while playing.   |
| **Python Auto File Organizer** | ![Auto File Organizer Preview](python-auto-file-organizer/screenshots/preview.png)                                    | `python python-auto-file-organizer/auto_cleanup.py -s test_folder --mode extension` | Organize files by **extension** or **modification date**. Features dry-run, safe moves, reset functionality, and CI-ready. |

---

## 💡 Why Use These Tools?

* **Save time and reduce repetitive work** – automate calculations, file organization, and data cleanup.
* **Portfolio-ready scripts** – showcase Python skills to clients or employers.
* **Reliable data handling** – safely clean CSVs, prevent overwrites, and maintain folder integrity.
* **Interactive and educational** – games and creative generators teach Python concepts while being fun.
* **Flexible and extendable** – all tools are CLI-based and easily customizable for real-world workflows.
* **Cross-platform support** – works on Windows, Mac, and Linux with automated CI testing.

---

## 📸 Tool Previews

### Tip Calculator

![Tip Calculator CLI](tip_calculator/screenshots/cli_version.png)
![Tip Calculator Web](tip_calculator/screenshots/web_version.png)

### Band Name Generator

![Band Name Generator](band-name-generator/screenshots/sample.png)

### CSV Cleaner

![CSV Cleaner Preview](csv-cleaner/screenshots/preview.png)

### Treasure Island

![Treasure Island Preview](treasure_island/screenshots/preview.png)

### Python Auto File Organizer

![Auto File Organizer Preview](python-auto-file-organizer/screenshots/preview.png)

---

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools
```

Install dependencies for projects that require them:

```bash
pip install pandas numpy
# CSV Cleaner and Python Auto File Organizer
```

---

## 🚀 Quick Start Examples

### **Tip Calculator**

```bash
python tip_calculator/calculator.py
# CLI mode: enter total bill, tip %, number of people
# Outputs: tip, total, per-person split
```

```bash
cd tip_calculator
python app.py
# Flask web mode: open http://127.0.0.1:5000
```

### **Band Name Generator**

```bash
python band-name-generator/band_name_generator.py
# Enter your city and pet's name
# Generates creative names instantly
```

### **CSV Cleaner**

```bash
python csv-cleaner/src/cleaner.py --in samples/input/example.csv
# Outputs: cleaned CSV and ASCII preview table
```

### **Treasure Island**

```bash
python treasure_island/treasure.py
# Follow prompts to explore the story and find the treasure
```

### **Python Auto File Organizer**

**Dry-run (preview changes):**

```bash
python python-auto-file-organizer/auto_cleanup.py -s test_folder --mode extension --dry-run
```

**Organize by extension:**

```bash
python python-auto-file-organizer/auto_cleanup.py -s test_folder --mode extension
```

**Organize by modification date:**

```bash
python python-auto-file-organizer/auto_cleanup.py -s test_folder --mode date
```

**Reset test folder:**

```bash
python python-auto-file-organizer/auto_cleanup.py -s test_folder --reset
```

---

## 🧪 CI & Testing

* Each project has its own **GitHub Actions CI workflow**.
* Automated tests validate outputs, folder structure, and reset functionality.
* Badges display real-time build/test status.

---

## ❓ FAQ

**Q: Do these scripts work on Windows, Mac, and Linux?**
A: Yes, all tools are tested cross-platform with GitHub Actions.

**Q: Can I customize file organization rules?**
A: Absolutely. The Python Auto File Organizer supports extension and date sorting, and the CLI can be extended for custom rules.

**Q: Do I need Python packages for all tools?**
A: Only CSV Cleaner and Python Auto File Organizer require `pandas` and `numpy`. Other tools are standard library only.

**Q: Can I use these tools in production workflows?**
A: Yes, they are lightweight, fast, and automation-friendly, designed for real-world use.

---

## 📬 Freelance & Custom Automation

Need **custom Python automation, file organization, or data workflows**?

I can build:

* CLI and web automation tools
* ETL pipelines and data preprocessing
* File management and folder organization scripts
* Interactive Python utilities or games

Contact me via GitHub: **[https://github.com/Johan1974](https://github.com/Johan1974)**

---

## 📝 License

MIT License — free to use, modify, and distribute

