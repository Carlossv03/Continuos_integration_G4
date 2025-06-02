"""
validator.py
"""
def validate_membership(membership):
    """
    Validate if the given membership is one of the available plans.

    Args:
        membership (Membership): The membership object to validate.

    Returns:
        bool: True if membership name is valid, False otherwise.
    """
    return membership.name in ["Basic", "Premium", "Family"]

def validate_features(_membership, features):
    """
    Validate if all features are valid for the membership.

    Args:
        membership (Membership): The membership object (not used in current validation).
        features (list of Feature): List of features to validate.

    Returns:
        bool: True if all feature names are valid, False otherwise.
    """
    valid = ["Personal Training", "Group Classes", "Nutrition Plan"]
    return all(f.name in valid for f in features)
