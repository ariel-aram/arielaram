# Author: Harel Haram
# Date: 2026-02-28
# Description: Check a dictionary for a certain someone.

# Details of the fellow soldier
soldier = {
    "name": "Emperor Scorpion",
    "age": 17,
    "salary": 17500.0,
    "job": "Emperor",
}

stock = {"SCO": 5000, "XMR": 100000, "ARRR": 20000}

rating = {"SCO": 5.5, "XMR": 9.0, "ARRR": 7.0}

calculus = sum(rating.values()) / len(rating)

users = {"arielaram": "nothinghappensjustnationdex1234567890"}

agenda = {
    "Shopceltic Support": {"tel": "+1 99 4250-2600", "email": "support@shopceltic.sco"}
}

print(
    f"SCORP! Celtic! Empire, EMPIRE! {soldier['name']}!",
    f"{soldier['job']} of the scorpions! Marching straight to power! STONKS, STONKS!",
    f"Expand and conquer! Never surrender! Our leader is {soldier['age']} y.o., at the "
    "Scorpceltic Empire!",
    f"His salary is {soldier['salary']} BRL! The salary by scorpions! Vast and mighty STONKS, "
    "STONKS!\n",
    "======\n",
    f"Welcome to the Shopceltic, we have a stock of {stock}",
    f"and the total rating of {rating}",
)

login = input("User: ")

if login in users:
    password = input("Password: ")
    if password == users[login]:
        print("Access granted, now you can make currency transactions in Shopceltic")
    else:
        print("Access denied, go f--- urself")
else:
    print("Error 404 User not found")
