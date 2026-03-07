# Author: Harel Haram
# Date: 2026-02-28
# Description: Calculate the classmates in a specific college.

classmates = ["Gerbica", "Achitop", "Swedefi", "Yac", "B0jaque"]
reactions = ["Boredom", "Tiredness", "Sleepiness"]
hypeValue = []
weather = ("Sunrise", "Morning", "Afternoon", "Sunset", "Night", "Midnight")
config = ("Classroom", "WindowsOpen", True)
feelings = ["Joy", "Happiness"]
location = (-21.6420, -67.2025)
lattitude, longitude = location
grades = (8.5, 7.0, 9.0, 6.0, 10.0)
finalList = tuple(feelings)

new_classmates = ["Maya", "Cayla", "Metr"]
classmates.extend(new_classmates)

reactions.insert(1, "Craizee")

for i in range(3):
    value = input(f"Type how much you are hyped about the {i + 1}° new classmate: ")
    hypeValue.append(value)  # type: ignore

typedName = input("Type your name to enter the college: ")

temporaryFeeling = input("What are your feelings just right now mister: ")
feelings.append(temporaryFeeling)

if typedName in classmates:
    print(f"Access granted! Welcome to your classroom, {typedName}")
else:
    print(
        "Too bad mister, you're not a student in this institution, get out before we deport u to Siberia"
    )

print("-" * 20)
print(f"Your college day starts at {weather[1]}")
print(f"It'll end at {weather[3]}, too bad if you're sleepy, now go study jamal")
print(f"The location is at: Lat = {lattitude} | Lon = {longitude}")
print(f"Your hype value is {hypeValue}, and they've arrived.")
print(f"Full list of classmates: {classmates}")
print(f"Total classmates: {len(classmates)}")
print(f"Their reactions to the new classmates are: {reactions}")
print(f"And their feelings were: {feelings}")
print(
    f"Btw the biggest grade is {max(grades)}, while the smallest grade is {min(grades)}"
)
print(f"Which is equal to {sum(grades)}")
