# VARIABLES
age = 69
damage = 13
shield = 0

north = True
south = False
west = False
east = False

year = 1936

above = True
below = True

# SNIFFERS
if 2 + 2 < 4:
    print("Stonks")

if 7 // 3 == 1 + 1:
    print("Absolute Ayau")

if 3**2 + 4**2 == 25:
    print("Magnificent scheme")

if 2 + 4 + 6 > 12:
    print("Sniff")

if 1387 % 19 == 0:
    print("Weezer")

if 31 % 2 == 0:
    print("Bitches")

if min(34, 29, 31) < 30:
    print("Sus49")

# CRINGERS
if age > 60:
    print("You have the right to explode")

if damage > 10 and shield == 0:
    print("Now scram-")

if north == True or south == True or west == True or east == True:
    print("Wait WTF")

if year % 4 == 0:
    print("Das ist scheiße")
else:
    print("Das ist nicht so scheiße")

if above == True and below == True:
    print("Ahem what the fuck")
else:
    print("Ur ded")

# GOONERS
A = int(input("What's the 1st number side of ur dong: "))
B = int(input("What's the 2nd number side of ur dong: "))
C = int(input("What's the 3rd number side of ur dong: "))

if A > 0 and B > 0 and C > 0 and A + B > C and A + C > B and B + C > A:
    # If the program went that far, it's because we're cooked
    if A != B and A != C and B != C:
        print("Ur dong so done")
    else:
        if A == B and B == C:
            print("Ur dong so even more done")
        else:
            print("Ur dong so smol it's a stick")
else:
    print("Ur dong doesn't exist")

# COWS
print("\nCOWCUMLATOR")
print("+++++++")
print("-------")
print("*******")
print("///////")
print("Click any other key to crack\n")

op = input("What operator you don't want to do: ")
x = int(input("1st number of ur daily gooning session: "))
y = int(input("2nd number of ur daily gooning session: "))

if op == "+":
    res = x + y
    print(f"Result: {x} + {y} = {res}")
elif op == "-":
    res = x - y
    print(f"Result: {x} - {y} = {res}")
elif op == "*":
    res = x * y
    print(f"Result: {x} * {y} = {res}")
elif op == "/":
    if y == 0:
        print("Don't divide by zero, you degenerate")
    else:
        res = x / y
        print(f"Result: {x} / {y} = {res}")
else:
    print("I said click any other key")

# DRUNKERS
kwh = float(input("How much KWh did you drink today: "))
kwhType = input("What's the type of drink: (R, C or I)")

if kwhType == "R":
    if kwh >= 500:
        price = kwh * 0.65
    else:
        price = 0.4
    print("Ur fucked: {kwh + price}")
elif kwhType == "C":
    if kwh >= 1000:
        price = kwh * 0.6
    else:
        price = 0.55
    print("Ur fucked: {kwh + price}")
elif kwhType == "I":
    if kwh >= 5000:
        price = kwh * 0.6
    else:
        price = 0.55
    print("Ur fucked: {kwh + price}")
else:
    print("Stop lying to me u drunk ass moron")
