import sys


def count(text):
    """Counts and prints the number of different character types in a string"""
    ul = ll = pm = sp = dg = 0
    for c in text:
        if c.isupper():
            ul += 1
        elif c.islower():
            ll += 1
        elif not c.isalnum() and not c.isspace():
            pm += 1
        elif c.isspace():
            sp += 1
        elif c.isdigit():
            dg += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{ul} upper letters")
    print(f"{ll} lower letters")
    print(f"{pm} punctuation marks")
    print(f"{sp} spaces")
    print(f"{dg} digits")


def main():
    """Reads input from command-line args or standard input & calls count()"""
    args = sys.argv[1:]
    assert len(args) <= 1, "more than one argument provided"
    if not args or not args[0]:
        print("What is the text to count?")
        text = sys.stdin.read()
    else:
        text = args[0]
    count(text)


if __name__ == "__main__":
    main()
