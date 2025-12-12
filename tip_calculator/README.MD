# Python Tip Calculator – CLI & Web Versions

![Python Version](https://img.shields.io/badge/python-3.11-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/tip_calculator_ci.yml/badge.svg)

**GitHub Repository:** [https://github.com/Johan1974/python-automation-and-tools/tree/main/tip_calculator](https://github.com/Johan1974/python-automation-and-tools/tree/main/tip_calculator)

**Python Tip Calculator** is a versatile tool that quickly calculates tips and splits bills among multiple people.  
Both **CLI and Web versions share the same core calculation logic**, making it fully testable, reliable, and professional for freelance projects or portfolio demonstration.

---

## 🎮 Features

- Calculate **tip amount**, **total bill**, and **per-person payment**  
- Locale-aware input supports:
  - EU format: `1.234,56`  
  - US format: `1,234.56`  
- Web version built with **Flask** for a clean, interactive interface  
- CLI version runs directly in the terminal for quick calculations  
- Core calculation logic is **unit-tested** and reused across both interfaces

---

## 🖥️ Example CLI Usage

```text
Welcome to the Tip Calculator!
What was the total bill? 150.50
How much tip would you like to give? 15
How many people to split the bill? 3

--- Tip Calculation ---
Tip amount: $22.58
Total bill: $173.08
Each person should pay: $57.69
````

---

## 🚀 Installation (Conda)

1. Clone the repository:

```bash
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools/tip_calculator
```

2. Create and activate a Conda environment:

```bash
conda create -n python-tools python=3.12
conda activate python-tools
```

3. Install dependencies:

```bash
conda install flask
```

---

## 💡 Usage

### CLI Version

```bash
python calculator.py
```

* Enter the total bill, tip percentage, and number of people.
* View the calculated tip, total, and per-person payments instantly.

### Web Version (Flask)

```bash
python app.py
```

* Open your browser at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
* Enter the total bill, tip percentage, and number of people.
* Click **Calculate** to see results immediately.

---

## 🧪 Testing & CI

* Core logic is in `calculate_tip(bill, tip_percent, people)`
* Unit tests are located in `tip_calculator/tests/` and can be run with:

```bash
python -m unittest discover -s tip_calculator/tests -p "test_*.py"
```

* GitHub Actions workflow (`.github/workflows/tip_calculator_ci.yml`) runs automated tests on push or pull request.
* CLI and Web versions use the **same tested function**, ensuring reliability.

---

## 💡 Applications & Freelance Use

* Calculate tips for restaurants, events, or group gatherings
* Split bills accurately among friends, coworkers, or clients
* Professional Python implementation shows **clean, testable code** for portfolio or freelance projects
* Web version can be adapted for business tools, interactive calculators, or online services

---

## 🔑 Key Benefits

* Fast, reliable, and locale-aware calculations
* Interactive design with clear results display
* Shared core logic across CLI and Web ensures consistency and maintainability
* Easily extendable for business or custom freelance projects

---

## Project Structure

```
tip_calculator/
├── calculator.py         # CLI version
├── app.py                # Flask web application
├── templates/
│   └── index.html        # HTML form and results
├── static/
│   └── style.css         # CSS styling
└── tests/
    └── test_calculator.py # Unit tests for calculation logic
```

---

## License

MIT License — free to use, modify, and distribute

---

## Contact & Freelance

Need a **custom Python calculator**, interactive tool, or web application?
Reach out via GitHub for freelance projects or tailored solutions.
