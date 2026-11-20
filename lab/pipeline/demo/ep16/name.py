from datetime import date

name = f"report_{date.today():%Y-%m}.xlsx"
print(name)
