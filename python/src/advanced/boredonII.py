# Author: Harel Haram
# Date: 2026-03-21
# Description: Calculate the area of a square through Python functions.

# width = int(input("Input da first number: "))
# height = int(input("Input the second numbr now: "))
side = float(input("Input the sides of ur silly square: "))


def siding(L):
    # if a >= b:
    #     print(
    #         f"The width of ur square is {width}cm, which is higher than the height which is {height}cm, that's all mister"
    #     )
    # else:
    #     print(
    #         f"Welp the height is {height}cm, which is bigger than the width of {width}cm, from ur silly square"
    #     )
    return L**2


# Do the L >:D
print(f"The square with the size of {side} has the initial area of {siding(side)}")
