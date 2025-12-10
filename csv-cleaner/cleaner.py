#!/usr/bin/env python3
import pandas as pd
import numpy as np
import argparse
import os

# -----------------------
# Pretty-print function
# -----------------------
def pretty_print(df):
    df_str = df.astype(str)
    col_widths = {col: max(df_str[col].map(len).max(), len(col)) + 2 for col in df_str.columns}
    header = "".join(col.ljust(col_widths[col]) for col in df_str.columns)
    print(header)
    print("-" * sum(col_widths.values()))
    for _, row in df_str.iterrows():
        line = "".join(str(row[col]).ljust(col_widths[col]) for col in df_str.columns)
        print(line)

# -----------------------
# CLI Arguments
# -----------------------
parser = argparse.ArgumentParser(description="Pro-level Generic CSV Cleaner")
parser.add_argument("--in", dest="input_file", required=True, help="Input CSV file path")
parser.add_argument("--out", dest="output_file", help="Output CSV file path")
parser.add_argument("--fill-strings", default="Unknown", help="Fill missing string values with this")
parser.add_argument("--fill-numbers", choices=["mean", "zero", "none"], default="mean", help="How to fill missing numeric values")
parser.add_argument("--preview", action="store_true", help="Preview only; do not save")
parser.add_argument("--pretty-out", help="Save a pretty ASCII table to a file")
args = parser.parse_args()

# -----------------------
# Check if input file exists
# -----------------------
if not os.path.isfile(args.input_file):
    print(f"Error: Input file '{args.input_file}' does not exist!")
    exit(1)

# -----------------------
# Auto-generate output filename if not given
# -----------------------
if not args.output_file:
    base, ext = os.path.splitext(args.input_file)
    args.output_file = f"{base}_cleaned{ext}"

# Default pretty file if not provided
# Default pretty file if not provided
if not args.pretty_out:
    base_dir, input_filename = os.path.split(args.input_file)
    name, _ = os.path.splitext(input_filename)
    args.pretty_out = os.path.join(base_dir, f"{name}_pretty.txt")


# -----------------------
# Read CSV
# -----------------------
data = pd.read_csv(args.input_file)
print("Original CSV:\n")
pretty_print(data)

# -----------------------
# Clean CSV
# -----------------------
# Normalize column names
data.columns = [col.strip().replace(" ","_").lower() for col in data.columns]

# Auto-detect numeric columns stored as strings
for col in data.select_dtypes(include=['object']):
    converted = pd.to_numeric(data[col], errors='coerce')
    num_non_na = converted.notna().sum()
    total_non_empty = data[col].replace(['', 'nan', 'NaN'], np.nan).notna().sum()
    if total_non_empty > 0 and num_non_na / total_non_empty >= 0.8:
        data[col] = converted

# Trim string columns & fill missing strings
for col in data.select_dtypes(include=['object']):
    data[col] = data[col].astype(str).str.strip()
    data[col] = data[col].replace(['', 'nan', 'NaN'], args.fill_strings)

# Remove duplicates
data = data.drop_duplicates()

# Numeric columns
for col in data.select_dtypes(include=[np.number]):
    if args.fill_numbers == "mean":
        data[col] = data[col].fillna(data[col].mean())
    elif args.fill_numbers == "zero":
        data[col] = data[col].fillna(0)
    # Auto-detect likely integer columns
    non_nan_values = data[col].dropna()
    if (non_nan_values % 1 == 0).all():
        data[col] = data[col].round(0).astype(int)
    else:
        data[col] = data[col].round(2)

# -----------------------
# Preview / Save
# -----------------------
print("\nCleaned CSV:\n")
pretty_print(data)

# Save pretty ASCII table
with open(args.pretty_out, "w") as f:
    col_widths = {col: max(data[col].astype(str).map(len).max(), len(col)) + 2 for col in data.columns}
    header = "".join(col.ljust(col_widths[col]) for col in data.columns)
    f.write(header + "\n")
    f.write("-" * sum(col_widths.values()) + "\n")
    for _, row in data.iterrows():
        line = "".join(str(row[col]).ljust(col_widths[col]) for col in data.columns)
        f.write(line + "\n")
print(f"\nPretty table saved to: {args.pretty_out}")

# Save CSV unless preview-only
if not args.preview:
    data.to_csv(args.output_file, index=False)
    print(f"\nCleaned CSV saved to: {args.output_file}")
