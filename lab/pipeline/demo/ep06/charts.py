import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")
products = ["Coffee", "Tea", "Cakes"]
totals = df[products].sum()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

df.plot(x="Month", y=products, marker="o", ax=ax1)
ax1.set_title("Monthly sales by product")
ax1.set_xlabel("")

totals.plot(kind="bar", rot=0, ax=ax2, color=["#8B5A2B", "#4C9A2A", "#E07A9B"])
ax2.set_title("Total sales in the year")
ax2.bar_label(ax2.containers[0])

plt.tight_layout()
plt.savefig("dashboard.png", dpi=150)
print("Saved dashboard.png")
plt.show()
