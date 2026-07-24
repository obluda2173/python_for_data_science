import sys

def main():
    args = sys.argv[1:]

    if not args:
        return
    try:
        assert len(args) == 1, "more than one argument is provided"
        try:
            num = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")
        print("I'm Even." if num % 2 == 0 else "I'm Odd.")
    except AssertionError as err:
        print(f"AssertionError: {err}")

if __name__=="__main__":
    main()
