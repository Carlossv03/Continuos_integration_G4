from models.membership import Membership
from models.feature import Feature
from models.user_selection import Selection
from services.discounts import apply_discounts

def test_no_discounts_applied():
    m = Membership("Basic", 50)
    s = Selection(m, [], False)
    assert apply_discounts(s, 50) == 50

def test_group_discount_applied():
    m = Membership("Family", 150)
    s = Selection(m, [], True)
    assert apply_discounts(s, 150) == 135

def test_threshold_discount_200():
    m = Membership("Premium", 100)
    f = [Feature("Group Classes", 60), Feature("PT", 50)]
    s = Selection(m, f, False)
    assert apply_discounts(s, 210) == 190

def test_threshold_discount_400():
    m = Membership("Family", 300)
    f = [Feature("PT", 60), Feature("GC", 60)]
    s = Selection(m, f, False)
    assert apply_discounts(s, 420) == 370

def test_combined_group_and_threshold_discount():
    m = Membership("Family", 300)
    f = [Feature("PT", 60), Feature("GC", 60)]
    s = Selection(m, f, True)
    total = 420
    after_group = total * 0.9
    expected = after_group - 50
    assert apply_discounts(s, total) == expected