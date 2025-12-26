"""
Name: Elham Morshedi Meibodi
class: CS 521 - Spring 1
Date: 2.25.2025
Final project
Description:
Expense Module

This module defines the Expense class, which is used to track expenses 
by category, amount, description, and date.
"""

from datetime import datetime


class Expense:
    """
    A class to represent an individual expense.

    Attributes:
        _date (str): Private attribute storing the date of the expense.
        category (str): The category of the expense.
        amount (float): The amount spent.
        description (str): A brief description of the expense.
    """

    CATEGORIES = [
        "Groceries", "Entertainment", "Home Facility", 
        "Transportation", "Utilities"
    ]

    def __init__(self, category: str, amount: float, description: str):
        """
        Initializes an Expense object.

        Args:
            category (str): The category of the expense.
            amount (float): The amount spent.
            description (str): A brief description of the expense.
        """
        # Validate category input
        if category not in self.CATEGORIES:
            raise ValueError(
                f"Invalid category: {category}. "
                f"Choose from: {', '.join(self.CATEGORIES)}"
            )

        # Store private date attribute
        self._date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category
        self.amount = amount
        self.description = description

    def get_date(self):
        """Returns the date of the expense."""
        return self._date

    def _format_expense(self):
        """Private method to format expense details."""
        return (
            f"{self._date} - {self.category}: "
            f"${self.amount:.2f} ({self.description})"
        )

    def __str__(self):
        """
        Returns a user-friendly string representation of the expense.
        """
        return self._format_expense()

    def __repr__(self):
        """
        Returns a technical string representation of the expense.
        Example: Expense('Groceries', 50.0, 'Bought vegetables')
        """
        return (
            f"Expense('{self.category}', {self.amount}, '{self.description}')"
        )

    def __eq__(self, other):
        """
        Check if two expenses are equal based on category and amount.
        This ignores the description and date.
        """
        return (
            isinstance(other, Expense) and
            self.category == other.category and
            self.amount == other.amount
        )

    def __lt__(self, other):
        """
        Less than comparison for sorting expenses by amount.
        """
        return self.amount < other.amount
    