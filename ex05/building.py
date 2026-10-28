from sys import argv
import sys


def main():
    """Count and display the different character types in a string"""
    assert len(argv) <= 2, "Only one argument is accepted"

    if (len(argv) == 1):
        print("What is the text to count?")
        text = sys.stdin.read()
    else:
        text = argv[1]

        lcount = len(text)
        upper = 0
        lower = 0
        space = 0
        digit = 0
        punct = 0

        for i in text:
            if (i.isupper()):
                upper += 1
            elif (i.islower()):
                lower += 1
            elif (i.isspace()):
                space += 1
            elif (i.isdigit()):
                digit += 1
            elif (i in ".,?!;:''\"\"-–—()[]{}.../\\"):
                punct += 1

        print(f"The text contains {lcount} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
    except KeyboardInterrupt:
        pass
