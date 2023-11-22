import sys

def hello_world():
    print("hello world")

def hello():
    print("hello")

def dog():
    print("woof") * 4


def default():
    print("Hello ")


def newFeature():
    default()
    print("hello again")


def main():
    if len(sys.argv) == 2:
        dog()
    else:
        default()
        newFeature()


if __name__ == "__main__":
    main()
