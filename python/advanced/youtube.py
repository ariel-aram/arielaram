# Author: Harel Haram
# Date: 2026-03-07
# Description: Download videos from YouTube and convert them into MP4.

# Import the whole declaration of independence from the corporatov hellholl
# Example: `from discord import ballsdex`
from pytubefix import YouTube  # type: ignore
from pytubefix.cli import on_progress  # type: ignore

url = input("Input the URL of ur brainrot: ")
yt = YouTube(url, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()  # type: ignore

print("Downloading vido!1!1!1!")
ys.download()  # type: ignore
print("Download complete mister, enjoy ur stoopid brainrot AI slop")
