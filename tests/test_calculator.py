import pytest
from models.membership import Membership
from models.feature import Feature
from models.user_selection import Selection
from services.calculator import calculate_total_cost

def test_basic_membership_no_features():
    m = Membership("Basic", 50)
    s = Selection(m, [], False)
    assert calculate_total_cost(s) == 50

def test_basic_with_features():
    m = Membership("Basic", 50)
    f = [Feature("Group Classes", 30), Feature("Personal Training", 40)]
    s = Selection(m, f, False)
    assert calculate_total_cost(s) == 120

def test_premium_membership_surcharge():
    m = Membership("Premium", 100, premium=True)
    f = [Feature("Nutrition Plan", 25)]
    s = Selection(m, f, False)
    expected = (100 + 25) * 1.15
    assert calculate_total_cost(s) == pytest.approx(expected)