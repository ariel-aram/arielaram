# Author: Harel Haram
# Date: 2026-03-21
# Description: Calculating if a number is even or odd.
num = int(input("Input ur silly number for our system to tracc: "))


def even(val: int) -> bool:
    return val % 2 == 0


even(num)


def even_or_odd(val: int) -> None:
    if even(val):
        print("The number is even fr")
    else:
        print("Suffer. The number is odd, too bad so sad")


even_or_odd(num)
