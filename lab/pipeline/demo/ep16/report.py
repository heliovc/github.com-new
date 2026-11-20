import pandas as pd
from openpyxl.styles import Font, PatternFill

df = pd.read_csv("orders_clean.csv", parse_dates=["Date"])
df = df[df["Status"] != "cancelled"]
df["Revenue"] = df["Qty"] * df["Price"]
df["Month"] = df["Date"].dt.strftime("%Y-%m")

by_city = df.groupby("City")["Revenue"].sum().sort_values(ascending=False).reset_index()
by_month = df.pivot_table(index="Month", columns="City", values="Revenue",
                          aggfunc="sum", fill_value=0)

with pd.ExcelWriter("report.xlsx") as writer:
    by_city.to_excel(writer, sheet_name="By city", index=False)
    by_month.to_excel(writer, sheet_name="By month")
    df.to_excel(writer, sheet_name="Data", index=False)

    for ws in writer.sheets.values():
        for cell in ws[1]:
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="1F6F5C")
        for col in ws.columns:
            ws.column_dimensions[col[0].column_letter].width = 14
        ws.freeze_panes = "A2"

    ws = writer.sheets["By city"]
    last = ws.max_row
    ws[f"A{last + 1}"] = "Total"
    ws[f"B{last + 1}"] = f"=SUM(B2:B{last})"
    ws[f"A{last + 1}"].font = Font(bold=True)
    for row in ws.iter_rows(min_row=2, min_col=2):
        for cell in row:
            cell.number_format = "#,##0.00"

    for cell in writer.sheets["Data"]["B"]:
        cell.number_format = "yyyy-mm-dd"

print("Saved report.xlsx")
