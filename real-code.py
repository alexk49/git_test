import sys


def default():
    print("Hello")


def newFeature():
    default()
    print("hello again")


def main():
    default()
    newFeature()


if __name__ == "__main__":
    main()
