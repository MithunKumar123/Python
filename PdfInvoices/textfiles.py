import pandas as p
import glob
from fpdf import FPDF as pdf
from pathlib import Path

filepaths = glob.glob("text files/*.txt")
document = pdf(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    df = p.read_fwf(filepath)
    file_name = Path(filepath).stem

    document.add_page()

    document.set_font(family="Times", size=16, style="B")
    document.cell(w=50, h=8, txt=f"{file_name.capitalize()}",ln=1,align="L")

    document.set_font(family="Times", size=12)
    with open(filepath, "r") as file_content:
        content = file_content.read()
    document.multi_cell(w=0, h=8, txt=content)


document.output("PDFs/output.pdf")