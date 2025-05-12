import pandas as pd
from fpdf import FPDF 

data = pd.read_excel("ikea_preces_3.xlsx")

class pdf_file(FPDF):
    def header(self):
        self.set_font("DejaVu", "", 8)
        self.cell(0, 10, txt="Preču katalogs", align="C")
        pdf.ln()
    def footer(self):
        self.set_y(-15)
        self.set_font("DejaVu", "", 8)
        self.cell(0,10, txt=f"Lapa {self.page_no()}", align="C")
        pass

pdf = pdf_file(orientation="P", unit="mm", format="A4")
pdf.add_font("DejaVu", "", "./DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)
pdf.add_page()

atlasits = data[["nosaukums", "cena", "apraksts"]]

us_w = pdf.w - 2 * pdf.r_margin
col_w = us_w / 12
row_h = pdf.font_size *2

for i in range(atlasits.shape[0]):
    pdf.set_font("DejaVu", size=10)
    pdf.cell(col_w*4, row_h, txt=str(atlasits["nosaukums"].iloc[i]), border=1)
    pdf.set_font("DejaVu", size=10)
    pdf.cell(col_w*2,row_h, txt=str(atlasits["cena"].iloc[i]), border=1)
    pdf.set_font("DejaVu", size=8)
    pdf.cell(col_w*6,row_h, txt=str(atlasits["apraksts"].iloc[i]), border=1)
    pdf.set_font("DejaVu", size=10)
    pdf.ln()
pdf.set_font("DejaVu", size=14)
pdf.cell(us_w, row_h, txt="something something", align="C")
pdf.ln()
#pdf.image("grfk.png", x=None, y=None, w=0, h=0)
url = "https://das.lv"

pdf.cell(us_w, row_h, txt="page", link=url, align="L", ln=True)

pdf.output("ikea_0.pdf")


