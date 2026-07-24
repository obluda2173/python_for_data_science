import sys

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        return

    try:
        assert len(args) == 1, "more than one argument is provided"
        assert is_integer(args[0]), "argument is not an integer"
        num = int(args[0])
        print("I'm Even." if num % 2 == 0 else "I'm Odd.")
    except AssertionError as err:
        print(f"AssertionError: {err}")

if __name__ == "__main__":
    main()
