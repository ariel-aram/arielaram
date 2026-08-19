# Author: Ariel Aram
# Date: 2026-04-11
# Description: Utilize Pandas to analyze the Excel file.

import pandas as pd

df = pd.read_excel("pastaorpizza.xlsx")

# Groupify per register and name
result = df.groupby(["Registry", "Name"])["Hours"].sum()


# Showing the final results
for (registry, name), hours in result.items():
    print(f"{registry} - {name} - {hours} hours")
