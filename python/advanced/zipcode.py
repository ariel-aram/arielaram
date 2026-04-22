# Author: Harel Haram
# Date: 2026-03-14
# Description: Find out details about a Brazilian ZIP code, so you can be sent to Brazil.
import requests

# The secret code to input the ZIP code
brazilian_zip = input("Input your silly ZIP code: ")

# The Brazilian API yayayayayah
url = f"https://viacep.com.br/ws/{brazilian_zip}/json/"

# Your location bouta be tracked
response = requests.get(url)

# Ur deeta is being stolen
deeta = response.json()

# You're going to Brazil
if "error" in deeta:
    print(
        "Error 003 - Le fishe au chocolat ur next destination is Helsinki you need to suffer"
    )
else:
    print(f"YOU'RE GOING TO BRAZIL - {deeta['logradouro']}")
