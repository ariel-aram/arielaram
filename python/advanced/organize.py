# Author: Harel Haram
# Date: 2026-03-07
# Description: Organize and rename PDF files.

# Import the whole consititution from the silly operatin system
# Windows 11 sucks donkey duckz
# Linux is goated and peaked
from pathlib import Path

# Analyze da foldrr
folder = Path("src")

# Loopimg machine
counter = 1
for file_path in folder.iterdir():
    # Only rename files
    if file_path.is_file():
        # Get the file extension
        extension = file_path.suffix

        # Generate the new random name
        new_name = f"mr_spherical_archive{counter:03d}{extension}"

        # Location of the new file
        new_path = folder / new_name

        # Action to rename the silly archives
        file_path.rename(new_path)

        # Success message
        print(f"File {file_path.name} renamed to {new_name} lol")

        counter += 1

# It's joever omg
print(
    "\nAll files have been renamed with peak and great success!1!1!1!1! "
    "Take gud care of ur ballz mr. Bloxy"
)
