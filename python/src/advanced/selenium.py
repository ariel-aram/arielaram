# Author: Ariel Aram
# Date: 2026-04-18
# Description: Utilize Selenium to navigate and extract data from a silly books website.

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service)

# If internet is slower than a lazy ahh turtle, wait 10s and suffer

browser.implicitly_wait(10)

print("Searching on the bible frfr")

browser.get("https://books.toscrape.com")
time.sleep(60)

print(
    "Searching for the target, weaponz of mass destructions are being deployed OMG!1!1!1!"
)

logo = browser.find_element(By.XPATH, "/html/body/header/div/div/div/a")

text_logo = logo.text

print("The extracted text was: ", text_logo)
