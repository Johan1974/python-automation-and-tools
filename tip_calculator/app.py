from flask import Flask, request, render_template
import locale

# --- Load system locale settings ---
locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()

SYSTEM_DECIMAL = conv['decimal_point']
SYSTEM_THOUSAND = conv['thousands_sep']
SYSTEM_CURRENCY = conv['currency_symbol']

app = Flask(__name__)

def parse_number(value):
    """Parse number string into float (locale-aware, EU/US fallback)."""
    value = value.strip()
    try:
        return locale.atof(value)
    except ValueError:
        pass
    last_dot = value.rfind(".")
    last_comma = value.rfind(",")
    if last_comma > last_dot:  # EU
        clean = value.replace(".", "").replace(",", ".")
        return float(clean)
    return float(value.replace(",", ""))  # US

def format_currency(amount):
    """Format currency using locale if possible, fallback $X.XX."""
    try:
        return locale.currency(amount, grouping=True)
    except ValueError:
        return f"${amount:,.2f}"

@app.route("/", methods=["GET", "POST"])
def home():
    result = False
    tip = total = per_person = None

    if request.method == "POST":
        # --- Parse inputs ---
        bill = parse_number(request.form.get("bill"))
        tip_percentage = parse_number(request.form.get("tip_percentage"))
        people = int(request.form.get("people"))

        # --- Calculations ---
        tip_amount = bill * (tip_percentage / 100)
        total_bill = bill + tip_amount
        per_person_amount = total_bill / people

        # --- Format results ---
        tip = format_currency(tip_amount)
        total = format_currency(total_bill)
        per_person = format_currency(per_person_amount)

        result = True  # flag to show results in HTML

    # --- Render HTML with results ---
    return render_template(
        "index.html",
        result=result,
        tip=tip,
        total=total,
        per_person=per_person
    )

if __name__ == "__main__":
    app.run(debug=True)
