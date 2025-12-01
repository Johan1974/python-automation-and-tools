import locale

# --- Load system locale settings ---
locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()

SYSTEM_DECIMAL = conv['decimal_point']      # ',' in EU, '.' in US
SYSTEM_THOUSAND = conv['thousands_sep']     # '.' in EU, ',' in US
SYSTEM_CURRENCY = conv['currency_symbol']   # e.g., €, $

def parse_number(value):
    """
    Parse a number string into a float.
    Tries system locale first, then fallback to US/EU detection.
    """
    value = value.strip()
    try:
        return locale.atof(value)
    except ValueError:
        pass

    last_dot = value.rfind(".")
    last_comma = value.rfind(",")

    if last_comma > last_dot:  # EU format
        clean = value.replace(".", "")
        clean = clean.replace(",", ".")
        return float(clean)
    
    clean = value.replace(",", "")  # US format
    return float(clean)

def get_float(prompt):
    """Prompt for a float using locale-aware input."""
    while True:
        user_input = input(prompt)
        try:
            return parse_number(user_input)
        except ValueError:
            print("Please enter a valid number (supports both . and ,).")

def get_int(prompt):
    """Prompt for a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

def format_currency(amount):
    """
    Format currency using locale if possible.
    Fallback: simple $X.XX formatting.
    """
    try:
        return locale.currency(amount, grouping=True)
    except ValueError:
        # Fallback formatting
        return f"${amount:,.2f}"

# --- Start of Tip Calculator ---
print("Welcome to the Tip Calculator!")

# --- User input ---
bill = get_float("What was the total bill? ")
tip = get_int("How much tip would you like to give? 10, 12, or 15? ")
people = get_int("How many people to split the bill? ")

# --- Calculations ---
tip_percent = tip / 100
total_tip = bill * tip_percent
total_bill = bill + total_tip
amount_per_person = total_bill / people

# --- Format output safely ---
formatted_tip = format_currency(total_tip)
formatted_total = format_currency(total_bill)
formatted_per_person = format_currency(amount_per_person)

# --- Display results ---
print("\n--- Tip Calculation ---")
print(f"Tip amount: {formatted_tip}")
print(f"Total bill: {formatted_total}")
print(f"Each person should pay: {formatted_per_person}")
