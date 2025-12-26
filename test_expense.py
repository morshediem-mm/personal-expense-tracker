
"""
Name: Elham Morshedi Meibodi
class: CS 521 - Spring 1
Date: 2.25.2025
Final project
Description:
Unit Tests for the Expense Class

This module contains unit tests for the Expense 
class using the unittest framework.
"""

import unittest
from expense import Expense  # Importing the Expense class


class TestExpense(unittest.TestCase):
    """
    A test case for the Expense class.

    This test case checks:
    - Correct initialization of category, amount, and description.
    - The validity of the date attribute (retrieved via get_date method).
    - Equality comparison between two expense objects.
    - Validation of allowed categories.
    """

    def test_expense_creation(self):
        """Test the creation of an Expense object with valid attributes."""
        expense = Expense("Groceries", 50.0, "Bought fruits and vegetables")
        self.assertEqual(expense.category, "Groceries")
        self.assertEqual(expense.amount, 50.0)
        self.assertEqual(expense.description, "Bought fruits and vegetables")
        self.assertIsInstance(expense.get_date(), str)

    def test_expense_equality(self):
        """Test if two expenses with the same category and 
        amount are considered equal."""
        exp1 = Expense("Groceries", 50.0, "Bought fruits")
        exp2 = Expense("Groceries", 50.0, "Bought vegetables")
        self.assertEqual(exp1, exp2)

    def test_invalid_category(self):
        """Test that an invalid category raises a ValueError."""
        # Invalid category should raise an error
        with self.assertRaises(ValueError):
            Expense("InvalidCategory", 20.0, "Should fail") 
            


if __name__ == "__main__":
    unittest.main()
    
