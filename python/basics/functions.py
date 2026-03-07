# Author: Harel Haram
# Date: 2026-02-28
# Description: Calculate the entire world.

# Assemble all functionalities
def triforce(base, height):  # type: ignore
    return (base * height) / 2  # type: ignore


def kelvin(celsius):  # type: ignore
    return celsius + 273.15  # type: ignore


def fahrenheit(celsius):  # type: ignore
    return celsius * 1.8 + 32  # type: ignore


def conversion(cash):  # type: ignore
    return cash / 5.13  # type: ignore


def gaseta(gas, eta):  # type: ignore
    return eta / gas  # type: ignore


b = float(input("Input the base number of your force: "))
h = float(input("Input the height of Napoleon: "))
print("======\n")
w = float(input("Input the temperature of ur booze: "))
m = float(input("How much money do u have to buy beer: "))
g = float(
    input(
        "What's the current gas pricings, just so you don't end up without fuel mister: "
    )
)
e = float(input("Now what's the eta pricing mister: "))
print("======\n")
if m >= 5:
    print(
        f"The triforce area is {triforce(b, h)}, so FEEL THE WRATH OF NAPOLEON, PUNKS!1!1!1!",
        f"The temperature of y'all's booze is over {kelvin(w)}K and {fahrenheit(w)}°F.",
        f"Your money is worth {conversion(m)} USD, and it is plummeting as we speak, make america greta agann RAAAAAAAAAAH.",
        f"The gas prices are over ${gaseta(g, e)} a gallon, too bad mister how dare u drink alcohol.",
    )
else:
    print(
        f"MUAHHAHAHAHAHAHAHAHAHAHJSGFGJDSGJGG U HAVE ONLY {conversion(m)} USD ON UR BANK ACCOUNT LMFAOOOOOOOOO",
        "bro can't even get drunk lmfao get lost",
    )
