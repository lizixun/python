class Employee():
    """A class to represent an employee."""

    def __init__(self, f_name, l_name, salary):
        """Initialize the employee."""
        self.f_name = f_name.title()
        self.l_name = l_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """Give the employee a raise."""
        self.salary += amount

import unittest

class TestEmployee(unittest.TestCase):
    """Tests for the module employee."""

    def setUp(self):
        """Make an employee to use in tests."""
        self.eric = Employee('eric', 'matthes', 65000)

    def test_give_default_raise(self):
        """Test that a default raise works correctly."""
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 70000)

    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        self.eric.give_raise(10000)
        self.assertEqual(self.eric.salary, 75000)

unittest.ma