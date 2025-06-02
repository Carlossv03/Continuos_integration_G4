"""
error_handler.py

This module provides utility functions for displaying and handling error messages
within the gym membership management system.
"""

def handle_error(message):
    """
    Displays an error message and exits with -1.

    Args:
        message: The error message to display.
    """
    print(f"Error: {message}")
    print("-1")
