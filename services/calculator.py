"""
calculator.py

This module contains functions to calculate the total cost of a gym membership
based on the selected membership plan and additional features.
"""
def calculate_total_cost(selection):
    """
    Calculate the total cost of the membership selection.

    The total cost includes:
    - Base membership cost
    - Additional feature costs
    - 15% surcharge if the membership includes premium features

    Args:
        selection (Selection): The user's membership selection, 
        including membership plan and features.

    Returns:
        float: The calculated total cost.
    """
    total = selection.membership.base_cost
    for f in selection.features:
        total += f.cost

    if selection.membership.premium:
        total *= 1.15

    return total
