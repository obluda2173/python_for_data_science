from typing import Any


def mean(args):
    return sum(args) / len(args)


def median(args):
    s = sorted(args)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]


def percentile(s, p):
    n = len(s)
    pos = (n - 1) * p
    lo = int(pos)
    hi = min(lo + 1, n - 1)
    frac = pos - lo
    return float(s[lo] + (s[hi] - s[lo]) * frac)


def quartile(args):
    s = sorted(args)
    return [percentile(s, 0.25), percentile(s, 0.75)]


def var(args):
    m = mean(args)
    return sum((x - m) ** 2 for x in args) / len(args)


def std(args):
    return var(args) ** 0.5


func = {
    "mean": mean,
    "median": median,
    "quartile": quartile,
    "std": std,
    "var": var,
}


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    for operation in kwargs.values():
        if operation not in func:
            continue
        try:
            print(f"{operation} : {func[operation](args)}")
        except (ZeroDivisionError, IndexError, TypeError, ValueError):
            print("ERROR")
