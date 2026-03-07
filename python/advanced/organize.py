# Author: Harel Haram
# Date: 2026-03-07
# Description: Organize and rename PDF files.

# Import the whole consititution from the silly operatin system
# Windows 11 sucks donkey duckz
# Linux is goated and peaked
import os

# Analyze da foldrr
folder = "src"

# How mucc Wolfkang filez
listArchives = os.listdir(folder)

# Loopimg machine
counter = 1
for file in listArchives:
    # One file has name and extension
    # We have to split the name from the extension
    name, extension = os.path.splitext(file)

    # Generate the new random name
    new_name = f"mr_spherical_archive{counter:03d}{extension}"

    # Location of the old file
    oldPath = os.path.join(folder, file)

    # Location of the new file
    newPath = os.path.join(folder, new_name)

    # Action to rename the silly archives
    os.rename(oldPath, newPath)

    # Success message
    print(f"File {file} renamed to {new_name} lol")

    counter += 1

# It's joever omg
print(
    "\nAll files have been renamed with peak and great success!1!1!1!1! Take gud care of ur ballz, Bloxy"
)
