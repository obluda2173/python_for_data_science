from typing import Any


def callLimit(limit: int):
    """Create a decorator granting at most limit calls from a shared quota."""
    count = 0

    def callLimiter(function):
        """Wrap `function` so its calls draw on the shared quota."""
        def limit_function(*args: Any, **kwds: Any):
            """Call `function` if quota remains, else print an error."""
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            print(f"Error: {function} call too many times")
            return None
        return limit_function
    return callLimiter
