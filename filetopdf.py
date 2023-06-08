import img2pdf
from PIL import Image
import os

img_path = "D:/images/Article.png"

pdf_path = "D:/images/Article.pdf"

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()

print("Successfully made pdf file")

import img2pdf
from PIL import Image
import os

img_path = "D:/images/aurebesh.jpg"

pdf_path = "D:/images/Article.pdf"

image = Image.open(img_path)

pdf_bytes = img2pdf.convert(image.filename)

file = open(pdf_path, "wb")

file.write(pdf_bytes)

image.close()

file.close()

print("Successfully made pdf file")

from win32com import client

excel = client.Dispatch("Excel.Application")

sheets = excel.Workbooks.Open("D:\PdfConv\input_xlsx.xlsx")
work_sheets = sheets.Worksheets[0]

work_sheets.ExportAsFixedFormat(0, "D:\PdfConv\input_xlsx.pdf")

from win32com import client

excel = client.Dispatch("Excel.Application")

sheets = excel.Workbooks.Open("D:\PdfConv\input_xls.xls")
work_sheets = sheets.Worksheets[0]

work_sheets.ExportAsFixedFormat(0, "D:\PdfConv\input_xls.pdf")

from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 15)

f = open("D:\PdfConv\input_txt.txt", "r")

for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')

pdf.output("D:\PdfConv\input_txt.pdf")