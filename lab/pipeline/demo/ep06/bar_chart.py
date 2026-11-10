import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")
totals = df[["Coffee", "Tea", "Cakes"]].sum()
print(totals)

ax = totals.plot(kind="bar", color=["#8B5A2B", "#4C9A2A", "#E07A9B"], rot=0, figsize=(8, 5))
ax.set_title("Total sales in the year")
ax.bar_label(ax.containers[0])
plt.tight_layout()
plt.savefig("bar.png", dpi=150)
plt.show()
