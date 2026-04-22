# Author: Harel Haram
# Date: 2026-02-07
# Description: Calculate gas pricing

gas_price = 1.50
ethanol_price = 1.20
division = ethanol_price / gas_price
currency = "USD"

soberano_bolivar = 381.68
bolivar = "VES"

conversion_gas = soberano_bolivar * gas_price
conversion_eth = soberano_bolivar * ethanol_price

print(
    "The price of the oil that you pump for money in the middle east and turn into a rich boi: ",
    gas_price,
    currency,
)
print(
    "As well as the price of your silly ethanol: ",
    ethanol_price,
    currency,
)
print(
    "Conversion to the most unvalued currency in the whole observable universe: Gas ",
    conversion_gas,
    bolivar,
    " | Ethanol ",
    conversion_eth,
    bolivar,
)
print("Your money is worth nothing.")
