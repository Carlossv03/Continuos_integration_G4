def apply_discounts(selection, total):
    if selection.is_group:
        total *= 0.90  # 10% off for group

    if total > 400:
        total -= 50
    elif total > 200:
        total -= 20

    return total
