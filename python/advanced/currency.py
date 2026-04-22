# Author: Harel Haram
# Date: 2026-03-21
# Description: Convert dollars with Brazilian Reals through the Python functions.
dollar = float(input("Input your dollars now: "))
real = 5.31


def brlusd(d, r):
    conversion = d * r
    return conversion


print(
    f"You've deposited US${dollar} on our totally secure bank account, now you got R${brlusd(dollar, real)}, your money is worth nothing, get scammed bozo"
)
