import os
import json
from datetime import datetime

# Define the expense tracking data file path
data_file = "expense_tracking.json"

# Function to load expense tracking data from the JSON file
def load_data():
    data = {}
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            data = json.load(f)
    return data

# Function to save expense tracking data to the JSON file
def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)

# Function to display expenses
def display_expenses(data):
    if not data:
        print("No expenses found.")
    else:
        print("Expenses:")
        for expense in data:
            print(f"Date: {expense['date']}")
            print(f"Category: {expense['category']}")
            print(f"Amount: ${expense['amount']:.2f}")
            print(f"Description: {expense['description']}\n")

# Function to add a new expense
def add_expense(data, date, category, amount, description):
    expense = {
        "date": date,
        "category": category,
        "amount": float(amount),
        "description": description
    }
    data.append(expense)
    save_data(data)
    print("Expense added successfully.")

# Function to generate an expense report
def generate_report(data):
    if not data:
        print("No expenses found to generate a report.")
    else:
        total_expenses = sum(expense['amount'] for expense in data)
        print("Expense Report:")
        print(f"Total Expenses: ${total_expenses:.2f}")

if __name__ == "__main__":
    print("Welcome to ExpenseTracker - Your Fast Expense Tracking Tool!")

    expense_data = load_data()

    while True:
        print("\nMenu:")
        print("1. View Expenses")
        print("2. Add Expense")
        print("3. Generate Expense Report")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ").strip()

        if choice == '1':
            display_expenses(expense_data)
        elif choice == '2':
            date = input("Enter the expense date (YYYY-MM-DD): ").strip()
            category = input("Enter the expense category: ").strip()
            amount = input("Enter the expense amount: ").strip()
            description = input("Enter a description (optional): ").strip()
            add_expense(expense_data, date, category, amount, description)
        elif choice == '3':
            generate_report(expense_data)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")
