import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")
totals = df[["Coffee", "Tea", "Cakes"]].sum()
ax = totals.plot(kind="pie", autopct="%1.0f%%", figsize=(6, 6))
ax.set_ylabel("")
ax.set_title("Share of the year's sales")
plt.savefig("pie.png", dpi=150)
plt.show()
