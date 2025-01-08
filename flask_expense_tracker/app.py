from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Define the file path for expenses.txt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXPENSES_FILE = os.path.join(BASE_DIR, "expenses.txt")

# Load expenses from a file
def load_expenses():
    try:
        with open(EXPENSES_FILE, "r") as file:
            expenses = [line.strip().split(",") for line in file.readlines()]
            return [{"amount": float(expense[0]), "category": expense[1]} for expense in expenses]
    except FileNotFoundError:
        return []

# Save expenses to a file
def save_expenses(expenses):
    with open(EXPENSES_FILE, "w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']},{expense['category']}\n")

# Calculate total expense
def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

@app.route("/", methods=["GET", "POST"])
def index():
    expenses = load_expenses()

    if request.method == "POST":
        if "add" in request.form:  # Handle adding an expense
            amount = float(request.form["amount"])
            category = request.form["category"].strip()
            
            # Add expense to the list
            expenses.append({"amount": amount, "category": category})
            save_expenses(expenses)

        elif "delete" in request.form:  # Handle deleting an expense
            expense_id = int(request.form["expense_id"])
            if 0 <= expense_id < len(expenses):
                expenses.pop(expense_id)
                save_expenses(expenses)

        return redirect(url_for("index"))

    total_expense = calculate_total(expenses)
    return render_template("index.html", expenses=expenses, total_expense=total_expense)

if __name__ == "__main__":
    app.run(debug=True)