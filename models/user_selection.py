from models.membership import Membership
from models.feature import Feature

def get_user_selection():
    # Datos de ejemplo
    basic = Membership("Basic", 50)
    premium = Membership("Premium", 100, premium=True)
    family = Membership("Family", 150)

    available_memberships = [basic, premium, family]
    print("Available Memberships:")
    for i, m in enumerate(available_memberships):
        print(f"{i + 1}. {m.name} - ${m.base_cost}")

    choice = int(input("Select membership (1-3): ")) - 1
    selected_membership = available_memberships[choice]

    features = [
        Feature("Personal Training", 40),
        Feature("Group Classes", 30),
        Feature("Nutrition Plan", 25)
    ]

    print("\nAvailable Features:")
    for i, f in enumerate(features):
        print(f"{i + 1}. {f.name} - ${f.cost}")

    feature_indices = input("Select features (comma separated): ").split(",")
    selected_features = [features[int(i) - 1] for i in feature_indices if i.strip().isdigit()]

    group = input("Is this a group membership? (yes/no): ").strip().lower() == "yes"

    return Selection(selected_membership, selected_features, group)

class Selection:
    def __init__(self, membership, features, is_group):
        self.membership = membership
        self.features = features
        self.is_group = is_group
