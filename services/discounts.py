"""
discounts.py
"""
def apply_discounts(selection, total):
    """
    Apply applicable discounts to the total membership cost.

    Discounts applied:
    - 10% discount if the membership is a group membership.
    - $50 discount if total exceeds $400.
    - $20 discount if total exceeds $200 (and is <= $400).

    Args:
        selection (Selection): The user's membership selection, including group status.
        total (float): The initial total cost before discounts.

    Returns:
        float: The total cost after applying all discounts.
    """
    if selection.is_group:
        total *= 0.90  # 10% off for group

    if total > 400:
        total -= 50
    elif total > 200:
        total -= 20

    return total
