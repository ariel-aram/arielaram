# Author: Harel Haram
# Date: 2026-02-28
# Description: Calculate the entire world.

# Assemble all functionalities
def triforce(base: float, height: float) -> float:
    return (base * height) / 2


def kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit(celsius: float) -> float:
    return celsius * 1.8 + 32


def conversion(cash: float) -> float:
    return cash / 4.9535


def gas_prices(gas: float, eta: float) -> float:
    return eta / gas


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
MIN_BEER_MONEY = 5

if m >= MIN_BEER_MONEY:
    print(
        f"The triforce area is {triforce(b, h)}, so FEEL THE WRATH OF NAPOLEON, PUNKS!1!1!1!",
        f"The temperature of y'all's booze is over {kelvin(w)}K and {fahrenheit(w)}°F.",
        f"Your money is worth {conversion(m)} USD, and it is plummeting as we speak, make "
        "america greta agann RAAAAAAAAAAH.",
        f"The gas prices are over ${gas_prices(g, e)} a gallon, too bad mister how dare u drink "
        "alcohol.",
    )
else:
    print(
        f"MUAHHAHAHAHAHAHAHAHAHAHJSGFGJDSGJGG U HAVE ONLY {conversion(m)} USD ON UR BANK "
        "ACCOUNT LMFAOOOOOOOOO",
        "bro can't even get drunk lmfao get lost",
    )
