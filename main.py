from utils.display import show_menu
from services.validator import validate_membership, validate_features
from services.calculator import calculate_total_cost
from services.discounts import apply_discounts
from models.user_selection import get_user_selection
from utils.error_handler import handle_error

def main():
    try:
        show_menu()
        selection = get_user_selection()
        if not validate_membership(selection.membership):
            return handle_error("Invalid membership selected.")

        if not validate_features(selection.membership, selection.features):
            return handle_error("One or more features are invalid.")

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
    except Exception as e:
        handle_error(str(e))

if __name__ == "__main__":
    main()
