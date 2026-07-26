import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """Calculates and returns BMI value from height and weight lists."""
    height, weight = np.array(height), np.array(weight)
    if height.shape != weight.shape:
        raise ValueError("height and weight must be the same length")
    if not (np.issubdtype(height.dtype, np.number) and
            np.issubdtype(weight.dtype, np.number)):
        raise ValueError("height and weight must be numeric")
    return [(weight[i] / height[i]**2) for i in range(len(height))]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return a mask marking which BMI values exceed the limit."""
    bmi = np.array(bmi)
    if not np.issubdtype(bmi.dtype, np.number):
        raise ValueError("bmi must be numeric")
    if not isinstance(limit, int):
        raise ValueError("limit must be int")
    return list(bmi > limit)
