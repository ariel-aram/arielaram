# Author: Ariel Aram
# Date: 2026-04-18
# Description: Send a notification using ntfy.sh.

import requests

name = str(input("What's ur name mister: "))
topic = "jeoboden"
url = f"https://ntfy.sh/{topic}"

requests.post(url, data=f"{name} just sent you totally sincere greetings")

print(f"Message sent at {topic}!1!1! Check ur device frfr")
