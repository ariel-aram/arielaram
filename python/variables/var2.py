# Author: Harel Haram
# Date: 2026-02-07
# Description: Convert Celsius to Fahrenheit and Kelvin

celsius = int(input("Input the temperature of ur booze: "))
fahrenheitdivision = 9 / 5
kelvinaddition = 273.15
fahrenheitaddition = 32

fahrenheit = celsius * fahrenheitdivision + fahrenheitaddition
kelvin = celsius + kelvinaddition

print(
    "The temperature of your booze is ",
    fahrenheit,
    "F° and ",
    kelvin,
    "K. Enjoy your boozing day with ur homies like the lame ahh booze you are.",
)
