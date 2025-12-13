#!/usr/bin/env python3
import pandas as pd
import numpy as np
import argparse
import os
import sys

# -----------------------
# CSV Cleaner Functions
# -----------------------
def pretty_print(df):
    df_str = df.copy()
    
    for col in df_str.columns:
        if pd.api.types.is_integer_dtype(df_str[col]):
            df_str[col] = df_str[col].astype(int).astype(str)
        elif pd.api.types.is_float_dtype(df_str[col]):
            # If value is exactly an integer, show as int
            df_str[col] = df_str[col].apply(lambda x: str(int(x)) if x == int(x) else f"{x:.2f}")
        else:
            df_str[col] = df_str[col].astype(str)

    col_widths = {col: max(df_str[col].map(len).max(), len(col)) + 2 for col in df_str.columns}
    header = "".join(col.ljust(col_widths[col]) for col in df_str.columns)
    print(header)
    print("-" * sum(col_widths.values()))
    for _, row in df_str.iterrows():
        line = "".join(str(row[col]).ljust(col_widths[col]) for col in df_str.columns)
        print(line)


def read_csv(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist!")
    return pd.read_csv(file_path)

def normalize_column_names(df):
    df.columns = [col.strip().replace(" ","_").lower() for col in df.columns]
    return df

def auto_detect_numeric(df):
    for col in df.select_dtypes(include=['object']):
        converted = pd.to_numeric(df[col], errors='coerce')
        num_non_na = converted.notna().sum()
        total_non_empty = df[col].replace(['', 'nan', 'NaN'], np.nan).notna().sum()
        if total_non_empty > 0 and num_non_na / total_non_empty >= 0.8:
            df[col] = converted
    return df

def fill_strings(df, fill_value="Unknown"):
    for col in df.select_dtypes(include=['object']):
        # Replace NaN / None first
        df[col] = df[col].replace([None, '', 'nan', 'NaN'], fill_value)
        # Strip strings (only for non-null entries)
        df[col] = df[col].astype(str).str.strip()
    return df


def fill_numbers(df, method="mean"):
    for col in df.select_dtypes(include=[np.number]):
        if method == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif method == "zero":
            df[col] = df[col].fillna(0)

        # Round all numbers to 0 decimals if they are effectively integers
        non_nan_values = df[col].dropna()
        if (non_nan_values % 1 == 0).all():  # all whole numbers
            df[col] = df[col].astype(int)
        else:
            df[col] = df[col].round(0).astype(int)  # force rounding to int
    return df



def remove_duplicates(df):
    return df.drop_duplicates()

def save_csv(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

def save_pretty(df, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        col_widths = {col: max(df[col].astype(str).map(len).max(), len(col)) + 2 for col in df.columns}
        header = "".join(col.ljust(col_widths[col]) for col in df.columns)
        f.write(header + "\n")
        f.write("-" * sum(col_widths.values()) + "\n")
        for _, row in df.iterrows():
            line = "".join(str(row[col]).ljust(col_widths[col]) for col in df.columns)
            f.write(line + "\n")

# -----------------------
# CLI Wrapper
# -----------------------
def main():
    parser = argparse.ArgumentParser(description="Pro-level Generic CSV Cleaner")
    parser.add_argument("--in", dest="input_file", required=True, help="Input CSV file path")
    parser.add_argument("--out", dest="output_file", help="Output CSV file path")
    parser.add_argument("--fill-strings", default="Unknown", help="Fill missing string values with this")
    parser.add_argument("--fill-numbers", choices=["mean", "zero", "none"], default="mean", help="How to fill missing numeric values")
    parser.add_argument("--preview", action="store_true", help="Preview only; do not save")
    parser.add_argument("--pretty-out", help="Save a pretty ASCII table to a file")
    args = parser.parse_args()

    base_dir, input_filename = os.path.split(args.input_file)
    name, ext = os.path.splitext(input_filename)

    # Default output folder: samples/output/ relative to the input file
    parent_dir = os.path.dirname(base_dir)  # samples/
    default_output_dir = os.path.join(parent_dir, "output")
    os.makedirs(default_output_dir, exist_ok=True)

    if not args.output_file:
        args.output_file = os.path.join(default_output_dir, f"{name}_cleaned{ext}")

    if not args.pretty_out:
        args.pretty_out = os.path.join(default_output_dir, f"{name}_pretty.txt")

    # -----------------------
    # Read and clean
    # -----------------------
    df = read_csv(args.input_file)
    print("Original CSV:\n")
    pretty_print(df)

    df = normalize_column_names(df)
    df = auto_detect_numeric(df)
    df = fill_strings(df, args.fill_strings)
    df = remove_duplicates(df)
    if args.fill_numbers != "none":
        df = fill_numbers(df, args.fill_numbers)

    print("\nCleaned CSV:\n")
    pretty_print(df)

    # -----------------------
    # Save outputs
    # -----------------------
    save_pretty(df, args.pretty_out)
    print(f"\nPretty table saved to: {args.pretty_out}")
    if not args.preview:
        save_csv(df, args.output_file)
        print(f"\nCleaned CSV saved to: {args.output_file}")

# -----------------------
# Entry point
# -----------------------
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
