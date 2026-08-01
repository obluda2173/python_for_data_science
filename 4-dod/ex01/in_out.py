def square(x: int | float) -> int | float:
    """Return x squared."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Return a closure applying `function` to a compounding accumulator."""
    count = 0

    def inner() -> float:
        """Advance the accumulator and return it."""
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner
