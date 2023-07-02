from fpdf import FPDF
import pandas as p


def line_generator(x1,y1,x2):
    for co_ord in range(y1,300,10):
        pdf.line(x1,co_ord,x2, co_ord)


def add_footer(footer_message):
    pdf.ln(265)
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(180,180,180)
    pdf.cell(w=0,h=12,txt=footer_message,align="R",ln=1)


def add_subsequent_pages(page_title, no_of_pages):
    for i in range(no_of_pages):
        pdf.add_page()
        line_generator(10, 20, 200)
        add_footer(page_title)


def add_first_page(page_title):
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=page_title, align="L", ln=1)
    line_generator(10, 20, 200)
    add_footer(page_title)


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
df = p.read_csv("topics.csv")

for index, page_details in df.iterrows():
    add_first_page(page_details['Topic'])
    add_subsequent_pages(page_details['Topic'], page_details['Pages'] - 1)
pdf.output("PdfFile.pdf")
