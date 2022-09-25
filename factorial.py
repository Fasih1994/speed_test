from functools import reduce
import sys


def fectorial(init_number: int) -> int:
    """calculates factorial of the given number

    Args:
        init_number (int): number whose factorial needs to be calculated

    Returns:
        int: returns the calculated result
    """

    return reduce(lambda x, y: x * y, range(int(init_number), 1, -1))


if __name__ == "__main__":
    print(f"Factorail of {sys.argv[1]} is: {fectorial(sys.argv[1]):>5}")
