import sys
from ft_filter import ft_filter


def is_int(value):
    """Return True if the string can be parsed as an integer"""
    try:
        int(value)
        return True
    except ValueError:
        return False


def parse_args(argv):
    """Validate argv and return the pair (string, integer)"""
    assert len(argv) == 2, "the arguments are bad"
    text, length = argv
    assert not is_int(text), "the arguments are bad"
    assert is_int(length), "the arguments are bad"
    return text, int(length)


def main():
    """Print the words of the first argument longer than the second one"""
    try:
        text, length = parse_args(sys.argv[1:])
    except AssertionError as err:
        print(f"AssertionError: {err}")
        return
    print(ft_filter(lambda word: len(word) > length, text.split()))


if __name__ == "__main__":
    main()
