from pathlib import Path
import pandas as p
import glob
from fpdf import FPDF as pdf


filepaths = glob.glob("invoices/*.xlsx")

for file in filepaths:
    df = p.read_excel(file, sheet_name="Sheet 1")
    print(df)

    file_name = Path(file).stem
    invoice_nr = file_name.split("-")

    document = pdf(orientation="P", unit="mm", format="A4")
    document.add_page()

    document.set_font(family="Times",size=16, style="B")
    document.cell(w=50,h=8,txt=f"Invoice_nr. {invoice_nr[0]}",ln=1)
    document.set_font(family="Times",size=16, style="B")
    document.cell(w=50,h=8,txt=f"Date: {invoice_nr[1]}", ln=1)
    columns = list(df.columns)
    #columns = [item.replace("_", " ").title() for item in columns]
    document.set_font(family="Times", style="B", size=14)
    document.set_text_color(0,180,0)
    document.cell(w=30, h=8, txt=columns[0].replace("_", " ").title(), border=1)
    document.cell(w=50, h=8, txt=columns[1].replace("_", " ").title(), border=1)
    document.cell(w=50, h=8, txt=columns[2].replace("_", " ").title(), border=1)
    document.cell(w=30, h=8, txt=columns[3].replace("_", " ").title(), border=1)
    document.cell(w=30, h=8, txt=columns[4].replace("_", " ").title(), border=1,ln=1)
    for index,items in df.iterrows():
        document.set_font(family="Times", size=10)
        document.set_text_color(180, 0, 0)
        document.cell(w=30, h=8, txt=str(items[columns[0]]), border=1)
        document.cell(w=50, h=8, txt=str(items[columns[1]]), border=1)
        document.cell(w=50, h=8, txt=str(items[columns[2]]), border=1)
        document.cell(w=30, h=8, txt=str(items[columns[3]]), border=1)
        document.cell(w=30, h=8, txt=str(items[columns[4]]), border=1, ln=1)

    total_amount = df[df.columns[4]].sum()
    document.set_font(family="Times", size=10)
    document.set_text_color(180, 0, 0)
    document.cell(w=30, h=8, txt="", border=1)
    document.cell(w=50, h=8, txt="", border=1)
    document.cell(w=50, h=8, txt="", border=1)
    document.cell(w=30, h=8, txt="", border=1)
    document.cell(w=30, h=8, txt=str(total_amount), border=1, ln=1)

    document.set_font(family="Times", size=16, style="B")
    document.cell(w=50, h=8, txt=f"The total amount is {total_amount}", ln=1)


    document.output(f"PDFs/{file_name}.pdf")