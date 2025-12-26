
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Elham Morshedi Meibodi
Class: CS 521 - Spring 1
Date: 2.25.2025
Final Project
Description:
Expense Tracker

This script allows users to add, view, and compare expenses. 
Expenses are stored in a CSV file for persistence.
Users can categorize expenses, enter an amount, and add a description.

Modules:
    csv: Used for reading and writing expense records in CSV format.
    expense: Contains the Expense class definition.
"""

import csv  # Required for handling CSV file storage
from expense import Expense  # Importing the Expense class for creating expenses


class ExpenseTracker:
    """
    A class to track personal expenses.

    Attributes:
        filename (str): The name of the CSV file used for storing expenses.
    """

    def __init__(self, filename="expenses.csv"):
        """
        Initializes the ExpenseTracker with a specified CSV filename.

        Args:
            filename (str): The name of the CSV file to store expense records.
                Defaults to "expenses.csv".
        """
        self.filename = filename
        self.categories = [
            "Groceries", "Entertainment", "Home Facility",
            "Transportation", "Utilities"
        ]  #  List usage ( Uses List)

    def add_expense(self, category, amount, description):
        """
        Adds a new expense record to the CSV file.

        Args:
            category (str): The category of the expense.
            amount (float): The amount spent.
            description (str): A brief description of the expense.
        """
        expense = Expense(category, amount, description)
        with open(self.filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                expense.get_date(),
                expense.category,
                expense.amount,
                expense.description
            ])  # File Handling 

    def view_expenses(self):
        """
        Displays all expense records stored in the CSV file.
        Uses a dictionary to store expenses with dates as keys.
        """
        try:
            expenses_dict = {}  # Dictionary usage 
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 4:
                        continue  # Skip incomplete rows
                        # Date as key, details as values
                    expenses_dict[row[0]] = row[1:]  

            # Print expenses using dictionary
            print("\nExpense Records:")
            for date, details in expenses_dict.items():
                try:
                    amount = float(details[1])  # Convert amount to float
                    print(
                        f"Date: {date}, Category: {details[0]}, "
                        f"Amount: ${amount:.2f}, Description: {details[2]}"
                    )
                except (IndexError, ValueError):
                    print(f"Error processing record: {details}")

        except FileNotFoundError:
            print("No expense records found.")  # Exception Handling 

    def find_least_expensive(self):
        """
        Finds and displays the least expensive expense from the CSV file.
        """
        try:
            expenses = []
            with open(self.filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) < 4:
                        continue  # Skip incomplete rows
                    date, category, amount, description = row
                    expenses.append(Expense(category, float(amount), description))

            if not expenses:
                print("No expense records found.")
                return

            #  Uses Sorting 
            least_expensive = min(expenses, key=lambda exp: exp.amount)
            print("\nLeast Expensive Expense:")
            print(
                f"Date: {least_expensive.get_date()}, "
                f"Category: {least_expensive.category}, "
                f"Amount: ${least_expensive.amount:.2f}, "
                f"Description: {least_expensive.description}"
            )

        except FileNotFoundError:
            print("No expense records found.")  # File Handling Exception


def compare_expenses():
    """
    Allows users to compare two expenses by selecting categories
    from the predefined list. Uses the __eq__ and __lt__ magic methods.
    """
    print("\nCompare two expenses:")

    try:
        # Show available categories
        tracker = ExpenseTracker()
        print("Select a category:")
        for i, category in enumerate(tracker.categories, 1):
            print(f"{i}. {category}")

        #  Add error handling for category selection
        while True:
            category_choice1 = input(
                "Enter the number of the first expense category (1-5): ").strip()
            if (category_choice1.isdigit() and
                1 <= int(category_choice1) <= len(tracker.categories)):
                category1 = tracker.categories[int(category_choice1) - 1]
                break
            print("Invalid choice. Please select a number from 1 to 5.")

        #  Add validation for numeric input
        while True:
            try:
                amount1 = float(input(f"Enter amount for {category1}: ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")

        description1 = input(f"Enter description for {category1}: ").strip()

        # Fix 3: Add error handling for category selection
        while True:
            category_choice2 = input(
                "Enter the number of the second expense category (1-5): ").strip()
            if (category_choice2.isdigit() and
                1 <= int(category_choice2) <= len(tracker.categories)):
                category2 = tracker.categories[int(category_choice2) - 1]
                break
            print("Invalid choice. Please select a number from 1 to 5.")

        #  Add validation for numeric input
        while True:
            try:
                amount2 = float(input(f"Enter amount for {category2}: ").strip())
                break
            except ValueError:
                print("Invalid input. Please enter a valid numeric amount.")

        description2 = input(f"Enter description for {category2}: ").strip()

        # Create expense objects
        expense1 = Expense(category1, amount1, description1)
        expense2 = Expense(category2, amount2, description2)

        #  Add clarity by showing expenses before comparison
        print("\nComparing Expenses:")
        print(f"First Expense: {expense1}")
        print(f"Second Expense: {expense2}")

        # Uses Magic Methods (Rubric: __eq__, __lt__)
        if expense1 == expense2:
            print("Both expenses are equal (same category and amount).")
        elif expense1 < expense2:
            print(
                f"The first expense (${expense1.amount:.2f}) "
                f"is less than the second (${expense2.amount:.2f})."
            )
        else:
            print(
                f"The second expense (${expense2.amount:.2f}) "
                f"is less than the first (${expense1.amount:.2f})."
            )

    except ValueError:
        print("Invalid input. Please enter a valid numeric amount.")  


if __name__ == "__main__":
    """
    Main function to interact with the ExpenseTracker.
    Users can add new expenses, view expenses, compare expenses,
    find the least expensive expense, or exit.
    """
    tracker = ExpenseTracker()

    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Compare Expenses")
        print("4. Find Least Expensive Expense\n5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("Select a category:")
            for i, category in enumerate(tracker.categories, 1):
                print(f"{i}. {category}")

            while True:
                category_choice = input(
                    "Enter the number of your category (1-5): ").strip()
                if (category_choice.isdigit() and
                    1 <= int(category_choice) <= len(tracker.categories)):
                    category = tracker.categories[int(category_choice) - 1]
                    break
                print(
                    "Invalid category choice."
                    " Please select a number from 1 to 5.")

            while True:
                try:
                    amount = float(input(f"Enter amount for {category}: ")
                                   .strip())
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")

            description = input(f"Enter description for {category}: ").strip()
            tracker.add_expense(category, amount, description)

        elif choice == "2":
            tracker.view_expenses()

        elif choice == "3":
            compare_expenses()

        elif choice == "4":
            tracker.find_least_expensive()

        elif choice == "5":
            break  # Exit program

        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")
