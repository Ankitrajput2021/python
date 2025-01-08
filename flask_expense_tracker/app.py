from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Load expenses from a file
def load_expenses():
    try:
        with open("expenses.txt", "r") as file:
            expenses = [line.strip().split(",") for line in file.readlines()]
            return [{"amount": float(expense[0]), "category": expense[1]} for expense in expenses]
    except FileNotFoundError:
        return []

# Save expenses to a file
def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']},{expense['category']}\n")

# Calculate total expense
def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)

@app.route("/", methods=["GET", "POST"])
def index():
    expenses = load_expenses()

    if request.method == "POST":
        # Get expense details from the form
        if "add" in request.form:
            amount = float(request.form["amount"])
            category = request.form["category"]
            
            # Add expense to the list
            expenses.append({"amount": amount, "category": category})
            save_expenses(expenses)
        elif "delete" in request.form:
            expense_id = int(request.form["expense_id"])
            expenses.pop(expense_id)
            save_expenses(expenses)

        return redirect(url_for("index"))

    total_expense = calculate_total(expenses)
    return render_template("index.html", expenses=expenses, total_expense=total_expense)

if __name__ == "__main__":
    app.run(debug=True)
