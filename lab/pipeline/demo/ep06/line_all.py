import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")
ax = df.plot(x="Month", y=["Coffee", "Tea", "Cakes"], marker="o", figsize=(10, 5))
ax.set_title("Monthly sales by product")
ax.set_ylabel("Sales ($)")
ax.set_xlabel("")
plt.tight_layout()
plt.savefig("line_all.png", dpi=150)
plt.show()
