import pandas as pd
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
coffee = [1820,1750,1980,2100,2240,2050,1900,1950,2300,2480,2610,2950]
tea    = [ 940, 910, 880, 760, 640, 520, 480, 500, 690, 850, 990,1120]
cakes  = [ 610, 650, 700, 720, 790, 830, 870, 860, 760, 740, 820,1040]
pd.DataFrame({"Month": months, "Coffee": coffee, "Tea": tea, "Cakes": cakes}).to_excel("sales.xlsx", index=False)
