"""
feature.py
"""
from dataclasses import dataclass

@dataclass
class Feature:
    """
    Represents an additional feature that can be added to a gym membership.

    Attributes:
        name (str): The name of the feature.
        cost (float): The cost of the feature.
    """
    name: str
    cost: float
