math1 = 403 % 73
math2 = 403 / 73
math3 = 403 // 73
math4 = 2**10
math5 = 54 - 57

a = 3
b = 4
c = a * a + b * b

s1 = "ant"
s2 = "bat"
s3 = "cod"

res1 = s1 + s2 + s3
res2 = 10 * (s1 + " ") + 2 * (s2 + " ") + 3 * (s3 + " ")

pricing1 = float(input("Input the price of an average university: "))
percentage = float(
    input("Input the discount percentage so you can be a cheap ass (0-100%): ")
)
discount = pricing1 * (percentage / 100)
final = pricing1 - discount

km = int(input("How much KMs you plan on running to university: "))
days = int(input("How many days you plan on running to university: "))
pricing2 = (60 * days) + (0.15 * km)

phrase = input("What'll be your yappathon phrase in university: ")
tam = len(phrase)
phrase2 = phrase[: int(tam / 2)]

print(
    "\n====== Uninter Calculations ======\n\n",
    math1,
    math2,
    math3,
    math4,
    math5,
    c,
    "\n\n",
    res1,
    res2,
    "\n\n====== Uninter Calculations ======\n",
)

if percentage >= 100:
    print("Explode yourself\n")
else:
    print(
        f"The price of an average university is {pricing1}. "
        f"The discount percentage is {percentage} percent. "
        f"The final price is {final}. "
        "Now scram. >:3\n"
    )

if days == 0 or km == 0:
    print("Imagine doing online university")
else:
    print(f"Km = {km}. Days = {days}")
    print(f"Total money spent = {pricing2}\n")

print(phrase2[-2:])
