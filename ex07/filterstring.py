from sys import argv


def main():
    """Filter words longer than a given size"""
    if len(argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        size = int(argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = argv[1].split()
    punctuation = ".,?!;:'\"-–—()[]{}.../\\"

    result = [
        word for word in words
        if (lambda w: len(w) > size and all(
            char not in punctuation and char.isprintable()
            for char in w
        ))(word)
    ]

    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
