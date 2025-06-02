"""
membership.py
"""
from dataclasses import dataclass

@dataclass
class Membership:
    """
    Represents a gym membership plan.

    Attributes:
        name (str): The name of the membership plan.
        base_cost (float): The base cost of the membership.
        premium (bool): Indicates if the membership has premium features.
    """
    name: str
    base_cost: float
    premium: bool = False
