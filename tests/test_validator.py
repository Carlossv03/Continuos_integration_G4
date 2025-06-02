import pytest
from models.membership import Membership
from models.feature import Feature
from services.validator import validate_membership, validate_features

def test_valid_membership():
    assert validate_membership(Membership("Basic", 50)) is True

def test_invalid_membership():
    assert validate_membership(Membership("Student", 50)) is False

def test_valid_features():
    f = [Feature("Personal Training", 40), Feature("Group Classes", 30)]
    assert validate_features(Membership("Basic", 50), f) is True

def test_invalid_features():
    f = [Feature("Yoga", 20), Feature("Spa", 50)]
    assert validate_features(Membership("Basic", 50), f) is False