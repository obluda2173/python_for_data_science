import sys

NESTED_MORSE = {" ": "/ ",
                "A": ".- ",
                "B": "-... ",
                "C": "-.-. ",
                "D": "-.. ",
                "E": ". ",
                "F": "..-. ",
                "G": "--. ",
                "H": ".... ",
                "I": ".. ",
                "J": ".--- ",
                "K": "-.- ",
                "L": ".-.. ",
                "M": "-- ",
                "N": "-. ",
                "O": "--- ",
                "P": ".--. ",
                "Q": "--.- ",
                "R": ".-. ",
                "S": "... ",
                "T": "- ",
                "U": "..- ",
                "V": "...- ",
                "W": ".-- ",
                "X": "-..- ",
                "Y": "-.-- ",
                "Z": "--.. ",
                "0": "----- ",
                "1": ".---- ",
                "2": "..--- ",
                "3": "...-- ",
                "4": "....- ",
                "5": "..... ",
                "6": "-.... ",
                "7": "--... ",
                "8": "---.. ",
                "9": "----. "}


def val_argv(argv):
    """Validate argv and return the arg"""
    assert len(sys.argv) == 2, "the arguments are bad"
    arg = sys.argv[1]
    assert all(c.isalnum() or c == " " for c in arg), "the arguments are bad"
    return arg


def main():
    """Print the translated to Morse code text"""
    try:
        arg = val_argv(sys.argv)
    except AssertionError as err:
        print(f"AssertionError: {err}")
        return
    print("".join(NESTED_MORSE[c] for c in arg.upper()).strip())


if __name__ == "__main__":
    main()
