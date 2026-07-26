import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print shape, return the array sliced from start to end."""
    if (not isinstance(family, list)
            or not all(isinstance(row, list) for row in family)):
        assert ValueError("family must be a list of lists")
    if len(family) > 0 and len({len(row) for row in family}) != 1:
        assert ValueError("rows must all be the same size")

    array = np.array(family)
    print(f"My shape is : {array.shape}")
    truncated = array[start:end]
    print(f"My new shape is : {truncated.shape}")
    return truncated.tolist()
