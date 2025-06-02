"""Tests for calculator functionality."""
from models.membership import Membership
from models.feature import Feature
from services.validator import validate_membership, validate_features


def test_valid_membership():
    """
    Test that validate_membership returns True for a valid membership.

    Asserts that a 'Basic' membership is recognized as valid.
    """
    assert validate_membership(Membership("Basic", 50)) is True

def test_invalid_membership():
    """
    Test that validate_membership returns False for an invalid membership.

    Asserts that a 'Student' membership is recognized as invalid.
    """
    assert validate_membership(Membership("Student", 50)) is False

def test_valid_features():
    """
    Test that validate_features returns True for valid features.

    Checks that valid features 'Personal Training' and 'Group Classes' 
    are accepted for the 'Basic' membership.
    """
    f = [Feature("Personal Training", 40), Feature("Group Classes", 30)]
    assert validate_features(Membership("Basic", 50), f) is True

def test_invalid_features():
    """
    Test that validate_features returns False for invalid features.

    Checks that invalid features 'Yoga' and 'Spa' are rejected for the 'Basic' membership.
    """
    f = [Feature("Yoga", 20), Feature("Spa", 50)]
    assert validate_features(Membership("Basic", 50), f) is False
