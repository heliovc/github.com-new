import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales.xlsx")
df.plot(x="Month", y="Coffee")
plt.savefig("line1.png")
plt.show()
