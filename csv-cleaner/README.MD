# Python CSV Cleaner & Data Preprocessing CLI Tool

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![GitHub Repo](https://img.shields.io/badge/GitHub-csv--cleaner-blue?logo=github)](https://github.com/Johan1974/python-automation-and-tools/tree/main/csv-cleaner)

Clean, normalize, and prettify messy CSV files with this **Python-based CSV cleaner**.
Ideal for **data analysts, developers, and data scientists** who want to **remove duplicates, fill missing values, and standardize CSV data** quickly and efficiently.

---

## Why Use This Tool?

* Save hours of manual CSV cleaning
* Automatically detect numeric columns stored as text
* Fill missing values intelligently for strings and numbers
* Remove duplicate rows
* Pretty-print CSVs in terminal or save as formatted ASCII tables
* Works with **any CSV**, even large and messy datasets

---

## Features

* Trim extra spaces from column names and string values
* Detect numeric columns stored as strings and convert them
* Fill missing string values with default (`Unknown`) or user-defined value
* Fill missing numeric values using **mean**, `0`, or leave as-is
* Remove duplicate rows automatically
* Optional **pretty ASCII output**
* Auto-generate output filename if not provided
* Fully **CLI-based** for automation

---

## Requirements

* Python 3.8+
* [pandas](https://pandas.pydata.org/)
* [numpy](https://numpy.org/)

Install dependencies:

```bash
pip install pandas numpy
```

---

## Installation

Clone the repository and navigate directly to the CSV cleaner folder:

```bash
git clone [https://github.com/Johan1974/python-automation-and-tools.git](https://github.com/Johan1974/python-automation-and-tools.git)
cd python-automation-and-tools/csv-cleaner
```

---

## Usage

Run the cleaner with the required input file:

```bash
python3 cleaner.py --in samples/before.csv
```

### Optional Command-Line Flags

| Option           | Description                                          | Default                                           |
| ---------------- | ---------------------------------------------------- | ------------------------------------------------- |
| `--in`           | Input CSV file path                                  | *Required*                                        |
| `--out`          | Output CSV file path                                 | `<input>_cleaned.csv` if not provided             |
| `--fill-strings` | Fill missing string values with this                 | `Unknown`                                         |
| `--fill-numbers` | Fill missing numeric values (`mean`, `zero`, `none`) | `mean`                                            |
| `--preview`      | Preview changes only, do not save                    | N/A                                               |
| `--pretty-out`   | Save a pretty ASCII table to a file                  | Automatically generated with `_pretty.txt` suffix |

---

## Demo ASCII Preview

**Input CSV:**

| Name       | Email                                                   | Age | City        |
| ---------- | ------------------------------------------------------- | --- | ----------- |
| John Doe   | [john@example.com](mailto:john@example.com)             | 30  | New York    |
| Jane Smith | [jane.smith@example.com](mailto:jane.smith@example.com) | 25  | Los Angeles |
| Alice      | [alice@example.com](mailto:alice@example.com)           |     | Chicago     |
| Bob        | [bob@example.com](mailto:bob@example.com)               | 40  |             |

**Terminal Preview After Cleaning:**

```
name       email                  age   city
--------------------------------------------

John Doe   [john@example.com](mailto:john@example.com)       30    New York
Jane Smith [jane.smith@example.com](mailto:jane.smith@example.com) 25    Los Angeles
Alice      [alice@example.com](mailto:alice@example.com)      31    Chicago
Bob        [bob@example.com](mailto:bob@example.com)        40    Unknown
```

---

## Who Is This For?

* Data analysts cleaning CSV exports from Excel, CRM, ERP, etc.
* Python developers automating data preprocessing
* Data scientists needing quick CSV fixes
* Freelancers building data automation pipelines for clients

---

## Contact / Custom Solutions

Looking for **custom CSV cleaning tools or Python automation scripts**?
Reach out on [GitHub](https://github.com/Johan1974) — professional consulting and freelance solutions available.

---

## License

MIT License

---

## Notes

* Duplicate rows are automatically removed.
* Numeric columns stored as strings are detected and converted.
* Missing string values default to `"Unknown"` (or your custom value).
* Missing numeric values can be filled by mean, zero, or left as-is.
* Pretty-printing helps quickly inspect your data without opening Excel.
* Works on **large CSVs** with consistent results.
* All output files (cleaned CSV and pretty ASCII table) are saved in the **same folder as the input file** unless a different path is specified.
