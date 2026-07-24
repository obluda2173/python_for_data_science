def ft_filter(f, obj):
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if f is None:
        return [x for x in obj]
    return [x for x in obj if f(x)]
