# Python Tip Calculator – Web & Command-Line Versions

**Python Tip Calculator** is a versatile tool that quickly calculates tips and splits bills among multiple people.  
It provides accurate results in both CLI and web formats, supporting EU and US number formats for real-world use.

---

## 🎮 Features

- Calculate **tip amounts**, **total bills**, and **per-person payments** for any group size  
- Supports **locale-aware input**, automatically handling decimal and thousand separators:  
  - EU format: 1.234,56  
  - US format: 1,234.56  
- Web version built with **Flask** and styled with CSS for a clear, user-friendly interface  
- CLI version runs directly in the terminal for fast, reliable calculations  
- Easily extendable with rounding, suggested tips, or visual enhancements

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

## Usage

### CLI Version

1. Run the calculator in the terminal:
```bash
python calculator.py
```

2. Enter the total bill, tip percentage, and number of people.  
3. View the calculated tip, total, and per-person payments instantly.

---

### Web Version (Flask)

1. Start the web app:
```bash
python app.py
```

2. Open your browser at:
http://127.0.0.1:5000/

3. Enter the total bill, tip percentage, and number of people.  
4. Click **Calculate** to see results immediately in a clean, interactive interface.

---

## 💡 Applications & Use Cases

- Quickly calculate tips for restaurants, events, or group gatherings  
- Split bills accurately among friends, coworkers, or clients  
- Web interface allows easy use for businesses, cafes, or online services  
- Python implementation provides a reliable and interactive solution for real-world needs

---

## 🔑 Key Benefits

- Fast and reliable calculation for both web and CLI users  
- Handles multiple locales and number formats accurately  
- Interactive design keeps input values visible and displays results clearly  
- Extendable for business applications, group events, or custom projects

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

## License

MIT License — free to use, modify, and distribute

---

## Contact & Freelance

Need a **custom Python calculator**, interactive tool, or web application?  
Reach out via GitHub for freelance projects or tailored solutions.
