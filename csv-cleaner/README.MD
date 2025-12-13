# Python CSV Cleaner & Data Preprocessing CLI Tool

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green)
![CI](https://github.com/Johan1974/python-automation-and-tools/actions/workflows/csv_cleaner_ci.yml/badge.svg)

**CSV Cleaner** is a Python CLI tool for cleaning, normalizing, and prettifying CSV files.  
Ideal for **data analysts, developers, and data scientists** who want to remove duplicates, fill missing values, and standardize CSV data quickly and reliably.

**GitHub Repository:**  
https://github.com/Johan1974/python-automation-and-tools/tree/main/csv-cleaner

---

## 📸 Screenshot / Preview

Here’s an example of the ASCII preview output for a cleaned CSV:

![CSV Cleaner Preview](screenshots/preview.png)

## 🗂 Sample Output

**Cleaned CSV (`sample_data1_cleaned.csv`):**

```csv
name,email,age,city
John Doe,john@example.com,30,New York
Jane Smith,jane.smith@example.com,25,Los Angeles
Alice,alice@example.com,30,Chicago
Bob,bob@example.com,40,Unknown
Unknown,missing@example.com,22,Miami
Charlie,charlie@example.com,35,San Francisco
````

**Pretty ASCII Preview (`sample_data1_pretty.txt`):**

```
name        email                   age  city           
--------------------------------------------------------
John Doe    john@example.com        30   New York       
Jane Smith  jane.smith@example.com  25   Los Angeles    
Alice       alice@example.com       30   Chicago        
Bob         bob@example.com         40   Unknown        
Unknown     missing@example.com     22   Miami          
Charlie     charlie@example.com     35   San Francisco  
```

> ✅ All numeric columns are now **integers**, ensuring clean and consistent output for analysis or reporting.
> Floating-point numbers representing whole numbers are rounded to remove decimals.

---

## 💡 Why Use This Tool?

* Save hours of manual CSV cleaning
* Auto-detect numeric columns stored as text
* Fill missing values for strings and numbers
* Remove duplicate rows
* Pretty-print cleaned CSVs in your terminal
* Save formatted ASCII tables for quick reviews
* Works with **any CSV**, including large datasets

---

## 🎮 Features

* Strip spaces from column names
* Auto-detect and convert numeric fields
* Fill missing string values using a default or custom value
* Fill missing numeric values using mean, zero, or skip
* Remove duplicate rows
* Optional ASCII preview
* Output filenames auto-generated
* Lightweight, fast, automation-friendly CLI

---

## 🛠 Requirements

* Python 3.8+
* `pandas`
* `numpy`

Install dependencies:

```bash
pip install pandas numpy
```

---

## 🚀 Installation

```bash
git clone https://github.com/Johan1974/python-automation-and-tools.git
cd python-automation-and-tools/csv-cleaner
```

---

## Usage

Run the cleaner with the required input file:

```bash
python3 src/cleaner.py --in samples/input/example.csv
```

### Command-Line Options

| Option           | Description                                  | Default               |
| ---------------- | -------------------------------------------- | --------------------- |
| `--in`           | Input CSV file path                          | *Required*            |
| `--out`          | Output CSV file path                         | `<input>_cleaned.csv` |
| `--fill-strings` | Value to replace missing string fields       | `Unknown`             |
| `--fill-numbers` | Numeric fill method (`mean`, `zero`, `none`) | `mean`                |
| `--preview`      | Show cleaning results without saving         | N/A                   |
| `--pretty-out`   | ASCII preview output path                    | `<input>_pretty.txt`  |

---

## 🧪 Running Tests Locally

Run all unit tests:

```bash
pytest -v csv-cleaner/tests/
```

Run an integration test:

```bash
python3 src/cleaner.py --in samples/input/example.csv
```

Ensure dependencies are installed:

```bash
pip install -r requirements.txt
```

---

## ⚙️ CI/CD Pipeline

A fully automated GitHub Actions workflow runs on every push:

* Unit testing (`pytest`)
* CSV cleaner integration testing
* Output validation

Workflow file: `.github/workflows/csv_cleaner_ci.yml`

---

## 🤝 Contributing

Contributions are welcome! Especially improvements to cleaning logic or test coverage.

1. Fork the repo
2. Create a feature branch
3. Add or update tests
4. Submit a pull request

All PRs automatically run through CI.

---

## 📅 Roadmap

Planned enhancements:

* Support for TSV, JSON, and Excel formats
* Improved column-type inference
* Duplicate-row audit report
* Optional logfile output
* Desktop GUI wrapper
* Publish to PyPI (`pip install csv-cleaner`)

Suggestions are welcome.

---

## 📬 Freelance & Custom Automation

Need a **custom CSV transformation tool**, automation script, or data-cleaning workflow?

I build:

* ETL pipelines
* Data quality automation
* Python CLI utilities
* Custom CSV/Excel normalization tools

Contact me via GitHub: **[https://github.com/Johan1974](https://github.com/Johan1974)**

---

## 📝 License

MIT License — free to use, modify, and distribute

