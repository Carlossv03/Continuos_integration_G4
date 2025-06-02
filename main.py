"""
main.py

Main module to run the Gym Membership Management System.
Handles user interaction, validation, cost calculation, discount application,
and confirmation of the membership selection.
"""

from models.user_selection import get_user_selection
from services.calculator import calculate_total_cost
from services.discounts import apply_discounts
from services.validator import validate_membership, validate_features
from utils.display import show_menu
from utils.error_handler import handle_error

def main():
    """
    Orchestrates the gym membership selection process.

    Steps:
    - Display membership menu.
    - Get user selection.
    - Validate membership and features.
    - Calculate total cost with discounts.
    - Display summary and ask for confirmation.
    - Handle errors gracefully.

    Returns:
        None: Prints output to the console. Prints -1 on error or cancellation.
    """
    try:
        show_menu()
        selection = get_user_selection()
        if not validate_membership(selection.membership):
            handle_error("Invalid membership selected.")
            return

        if not validate_features(selection.membership, selection.features):
            handle_error("One or more features are invalid.")
            return

        total = calculate_total_cost(selection)
        total_with_discounts = apply_discounts(selection, total)

        print("\n===== Membership Summary =====")
        print(f"Plan: {selection.membership.name}")
        print("Features:", ', '.join(f.name for f in selection.features))
        print(f"Total after discounts: ${int(total_with_discounts)}")
        confirm = input("Confirm membership (yes/no)? ").strip().lower()
        if confirm == "yes":
            print("Membership confirmed!")
            print(f"Final cost: {int(total_with_discounts)}")
        else:
            print("Membership cancelled.")
            print("-1")
    except (ValueError, IndexError) as e:
        handle_error(str(e))
    except Exception as e:
        handle_error(f"Unexpected error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
