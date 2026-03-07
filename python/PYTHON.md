# Ariel Aram's Python Skills

Adition = ( + )

Subtraction = ( - )

Multiplication = ( * )

Division = ( / )

Exponent = ( ** )

## Variables omg

float, int, input(), try:, except:, if, elif, else, f"", \n, for, in, and, range(), list(), tuple(), def, return, from, import

### Organization and renaming of PDF files through OS

```py
folder = "src"

os.listdir( folder )

name, extension = os.path.splitext( file )

new_name = f"mr_spherical_archive{counter:03d}{extension}"

counter = 1

counter += 1
```

### Python video downloader for YouTube

```py
from pytubefix import YouTube

from pytubefix.cli import on_progress

yt = YouTube(url, on_progress_callback=on_progress)

ys = yt.streams.get_highest_resolution()

ys.download()
```
