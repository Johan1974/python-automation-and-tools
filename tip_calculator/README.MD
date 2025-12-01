# Python Tip Calculator – Web & Command-Line (CLI) Versions

A **Python Tip Calculator** to quickly calculate tips, split bills among multiple people, and display results in a **locale-aware** format.
Available in **two variants**:

1. **[CLI Tip Calculator in Python](https://github.com/Johan1974/python-automation-and-tools/blob/main/tip_calculator/calculator.py)** – runs in the terminal, supports both EU and US number formats.
2. **[Web-based Tip Calculator (Flask)](https://github.com/Johan1974/python-automation-and-tools/blob/main/tip_calculator/app.py)** – built with **Flask**, styled with CSS, preserves input values, and shows results instantly in a user-friendly interface.

---

## Features

* Calculate **tip amount**, **total bill**, and **amount per person**.
* Supports **locale-aware input**:

  * EU format: `1.234,56`
  * US format: `1,234.56`
* Web version built with **Flask and CSS styling**:

  * Input values remain after submission
  * Results displayed neatly with formatting
* CLI version works directly in terminal for quick calculations
* Can be extended with rounding, tip suggestions, or color-coded tips

---

## Installation (Conda)

1. Clone the repository:

```bash
git clone [https://github.com/Johan1974/python-automation-and-tools.git](https://github.com/Johan1974/python-automation-and-tools.git)
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

## Usage

### CLI Version

1. Run the terminal-based calculator:

```bash
python calculator.py
```

2. Enter the **total bill**, **tip percentage**, and **number of people**.
3. View calculated tip, total, and per-person amounts directly in the terminal.

---

### Web Version (Flask)

1. Run the web app:

```bash
python app.py
```

2. Open your browser at:

```
http://127.0.0.1:5000/
```

3. Enter the **total bill**, **tip percentage**, and **number of people**.
4. Click **Calculate** to see results instantly in a **user-friendly, styled interface**.

---

## Project Structure

```
tip_calculator/
├── calculator.py         # CLI version
├── app.py                # Flask web application
├── templates/
│   └── index.html        # HTML form and results
└── static/
    └── style.css         # CSS styling
```

---

## Screenshots

*(Add screenshots here for web and CLI versions to improve SEO and visual appeal)*

---

## License

MIT License

---

## Notes

* Both versions are **locale-aware** and handle decimal and thousand separators automatically.
* Web version keeps input values after submission for convenience.
* Great for learning Python, Flask, and building **portfolio-ready projects**.
* Can be further extended with additional features like automatic tip suggestions, rounding rules, or color-coded results.

---

## SEO-friendly Description (for GitHub and search engines)

> Python Tip Calculator – Web & CLI versions. Quickly calculate tips, split bills, and display results with locale-aware formatting. Web app built with Flask, user-friendly interface, input persistence, and styled with CSS.

---

This version is **optimized for keywords** like:

* Python tip calculator
* Flask tip calculator web app
* CLI tip calculator Python
* Locale-aware currency calculator
* Split bill calculator

It’s ready to copy into your GitHub repository.

