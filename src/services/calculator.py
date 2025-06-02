def calculate_total_cost(selection):
    total = selection.membership.base_cost
    for f in selection.features:
        total += f.cost

    if selection.membership.premium:
        total *= 1.15

    return total
