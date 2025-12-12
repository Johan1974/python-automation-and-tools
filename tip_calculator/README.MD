# Python Tip Calculator – CLI & Web Versions

[![Python Version](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-tip--calculator-blue?logo=github)](https://github.com/Johan1974/python-automation-and-tools/tree/main/tip_calculator)
[![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/tip_calculator_ci.yml/badge.svg)](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/tip_calculator_ci.yml)

**Python Tip Calculator** is a versatile tool for quickly calculating tips and splitting bills among multiple people.  
It works in both CLI and web (Flask) formats, supporting EU and US number formats for real-world usage.

---

## 🎮 Features

- Calculate **tip amount**, **total bill**, and **per-person share**  
- Locale-aware input handling:
  - EU format: `1.234,56`
  - US format: `1,234.56`
- CLI version for terminal use  
- Web version built with **Flask** and CSS styling for user-friendly interface  
- Extendable for rounding, suggested tips, or visual enhancements

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools/tip_calculator
````

2. (Optional) Create and activate a Conda environment:

```bash
conda create -n python-tools python=3.12
conda activate python-tools
```

3. Install dependencies:

```bash
pip install flask
```

---

## 💡 Usage

### CLI Version

From the **repo root**, run:

```bash
python3 -m tip_calculator.calculator
```

* Enter the total bill, tip percentage, and number of people.
* View the calculated tip, total bill, and per-person amount instantly.

**Note:** Always run from the repo root to ensure proper package imports.

**Screenshot:**

![CLI Version](screenshots/cli_version.png)

---

### Web Version (Flask)

From the **repo root**, start the web app:

```bash
python3 -m tip_calculator.app
```

* Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* Fill in the bill, tip percentage, and number of people
* Click **Calculate** to see results immediately

**Screenshot:**

![Web Version](screenshots/web_version.png)

---

## 📝 Applications & Use Cases

* Restaurants, cafés, and events needing quick tip calculations
* Splitting bills among friends, coworkers, or clients
* Demonstrating **Python scripting, Flask web apps, and locale handling**
* Portfolio example for freelance Python projects

---

## 🔑 Key Benefits

* Fast, reliable calculations for both CLI and web users
* Accurate handling of EU/US number formats
* Interactive web interface with clean display of results
* Easily extendable for business or personal use

---

## 🗂 Project Structure

```
tip_calculator/
├── calculator.py         # CLI version
├── app.py                # Flask web application
├── templates/
│   └── index.html        # HTML form & results
├── static/
│   └── style.css         # CSS styling
├── screenshots/          # CLI & Web screenshots
├── tests/                # Unit tests
└── __init__.py           # Package marker
```

---

## 🧪 Running Tests

Run unit tests:

```bash
PYTHONPATH=$(pwd) python -m unittest discover -s tip_calculator/tests -p "test_*.py"
```

---

## 📬 Contact & Freelance

Looking for a **custom Python calculator** or web application?
I develop **interactive Python tools, web utilities, and automation scripts**.

Contact via GitHub: [https://github.com/Johan1974](https://github.com/Johan1974)

---

## License

MIT License — free to use, modify, and distribute
