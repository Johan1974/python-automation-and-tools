#!/usr/bin/env python3
"""
Python Tip Calculator – CLI Version
Calculates tip amounts, total bills, and per-person payments.
Locale-aware for EU/US formats.
"""

import locale

# --- Load system locale settings ---
locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()

SYSTEM_DECIMAL = conv['decimal_point']      # ',' in EU, '.' in US
SYSTEM_THOUSAND = conv['thousands_sep']     # '.' in EU, ',' in US
SYSTEM_CURRENCY = conv['currency_symbol']   # €, $, etc.

# --- Core calculation logic ---


def parse_number(value: str) -> float:
    """
    Parse a number string into a float using locale settings.
    Supports EU (1.234,56) and US (1,234.56) formats.
    """
    value = value.strip()
    try:
        return locale.atof(value)
    except ValueError:
        pass

    last_dot = value.rfind(".")
    last_comma = value.rfind(",")

    if last_comma > last_dot:  # EU format
        clean = value.replace(".", "").replace(",", ".")
        return float(clean)

    clean = value.replace(",", "")  # US format
    return float(clean)


def get_float(prompt: str) -> float:
    """Prompt user for a float using locale-aware input."""
    while True:
        user_input = input(prompt)
        try:
            return parse_number(user_input)
        except ValueError:
            print("Please enter a valid number (supports both . and ,).")


def get_int(prompt: str) -> int:
    """Prompt user for a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def format_currency(amount: float) -> str:
    """
    Format a number as currency using locale.
    Falls back to simple $X.XX formatting if needed.
    """
    try:
        return locale.currency(amount, grouping=True)
    except ValueError:
        return f"${amount:,.2f}"


def calculate_tip(bill: float, tip_percent: int, people: int) -> tuple[float, float, float]:
    """
    Calculate total tip, total bill, and amount per person.
    Returns a tuple: (total_tip, total_bill, amount_per_person)
    """
    tip_fraction = tip_percent / 100
    total_tip = bill * tip_fraction
    total_bill = bill + total_tip
    amount_per_person = total_bill / people
    return total_tip, total_bill, amount_per_person


# --- CLI Interface ---

def main():
    print("Welcome to the Tip Calculator!")

    # --- User input ---
    bill = get_float("What was the total bill? ")
    tip = get_int("How much tip would you like to give? 10, 12, or 15? ")
    people = get_int("How many people to split the bill? ")

    # --- Calculations ---
    total_tip, total_bill, amount_per_person = calculate_tip(bill, tip, people)

    # --- Format output ---
    formatted_tip = format_currency(total_tip)
    formatted_total = format_currency(total_bill)
    formatted_per_person = format_currency(amount_per_person)

    # --- Display results ---
    print("\n--- Tip Calculation ---")
    print(f"Tip amount: {formatted_tip}")
    print(f"Total bill: {formatted_total}")
    print(f"Each person should pay: {formatted_per_person}")


if __name__ == "__main__":
    main()
