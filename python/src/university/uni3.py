i = 3

while (i < 13):
    print(i)
    i += 1

for i in range(3, 13):
    print(i)

i2 = 0

for i2 in range(0, 9, 2):
    print(i)

while (i2 <= 8):
    print(i2)
    i2 += 2

print("\nOur SPAM convenience store\n")
print("1 - Ranger Spam $3.50")
print("2 - Classic Spam $3.50")
print("3 - Spicy Spam $3.50")
print("4 - Reduced Sodium Spam $3.50")
print("5 - Pull the middle finger (Not recommended)\n")

total = 0
while True:
    option = int(input("Please select an option: "))

    if option == 1:
        quantity = int(input("How many would you like? "))
        total = total + (quantity * 3.50)
    elif option == 2:
        quantity = int(input("How many would you like? "))
        total = total + (quantity * 3.50)
    elif option == 3:
        quantity = int(input("How many would you like? "))
        total = total + (quantity * 3.50)
    elif option == 4:
        quantity = int(input("How many would you like? "))
        total = total + (quantity * 3.50)
    elif option == 5:
        print("\nNI###\n")
        break
    else:
        print("\nThat's not an option u donkey\n")

    print("\nCurrent Total: $", total)

print("*cough* Thank you for spamming at our convenience store! Your total is $", total, "Now scram >:3\n\n")

value = int(input("Enter your change amount to verify purchase: "))

while True:
    if value >= 100:
        cont100 = value // 100
        value = value - cont100 * 100
        print(f"$100 Money Papers: {cont100} ||| You're a fraud for the ranger spam\n\n")
        if not value:
            break
    
    if value >= 50:
        cont50 = value // 50
        value = value - cont50 * 50
        print(f"$50 Money Papers: {cont50} ||| Stop buying ranger spams u dum\n\n")
        if not value:
            break

    if value >= 20:
        cont20 = value // 20
        value = value - cont20 * 20
        print(f"$20 Money Papers: {cont20} ||| You spamming bastard\n\n")
        if not value:
            break

    if value >= 10:
        cont10 = value // 10
        value = value - cont10 * 10
        print(f"$10 Money Papers: {cont10} ||| SPAMMER\n\n")
        if not value:
            break

    if value >= 5:
        cont5 = value // 5
        value = value - cont5 * 5
        print(f"$5 Money Papers: {cont5} ||| Really spamming?!\n\n")
        if not value:
            break

    if value >= 2:
        cont1 = value // 2
        value = value - cont1 * 2
        print(f"$2 Money Papers: {cont1} ||| What a cheap ass guy\n\n")
        if not value:
            break

    if value:
        cont1 = value
        print(f"$1 Money Papers: {cont1} ||| Gud thing you're broke, don't u dare ranger spamming\n\n")
        break

total2 = 0
monies = 0
acc_ages = 0

while True:
    age = float(input("Enter your age so we can do a age verification: "))
    if age == 0:
        break

    total2 += 1
    acc_ages += age
    if age < 3:
        ticket = 3
    else:
        if age > 12:
            ticket = 1.5
        else:
            ticket = 2

    monies += ticket

if total2 > 0:
    medium = acc_ages / total2
    print(f"Total people going to Helsinki: {total2}")
    print(f"Total of money gotten from lying about age verification checks: {monies}")
    print(f"Medium of money gotten from people: {medium}\n\n")
