import sys

def dog():
    print("woof")

def default():
    print("Hello")


def main():
    if len(sys.argv) == 2:
        dog()
    else:
        default()


if __name__ == "__main__":
    main()
