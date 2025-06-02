def validate_membership(membership):
    return membership.name in ["Basic", "Premium", "Family"]

def validate_features(membership, features):
    valid = ["Personal Training", "Group Classes", "Nutrition Plan"]
    return all(f.name in valid for f in features)
