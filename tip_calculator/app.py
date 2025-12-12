#!/usr/bin/env python3
"""
Python Tip Calculator – Web Version (Flask)
Reuses calculation logic from calculator.py.
"""

from flask import Flask, request, render_template
from tip_calculator.calculator import parse_number, format_currency, calculate_tip

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = False
    tip = total = per_person = None

    if request.method == "POST":
        # --- Parse inputs ---
        bill = parse_number(request.form.get("bill", "0"))
        tip_percentage = parse_number(request.form.get("tip_percentage", "0"))
        people = int(request.form.get("people", "1"))

        # --- Calculations using shared function ---
        total_tip, total_bill, amount_per_person = calculate_tip(bill, tip_percentage, people)

        # --- Format results ---
        tip = format_currency(total_tip)
        total = format_currency(total_bill)
        per_person = format_currency(amount_per_person)

        result = True  # Flag to show results in template

    return render_template(
        "index.html",
        result=result,
        tip=tip,
        total=total,
        per_person=per_person
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

