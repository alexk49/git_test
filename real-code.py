import sys

def dog():
    print("woof")

def default():
    print("Hello")


def newFeature():
    default()
    print("hello again")


def main():
    newFeature()

    if len(sys.argv) == 2:
        dog()
    else:
        default()


if __name__ == "__main__":
    main()
