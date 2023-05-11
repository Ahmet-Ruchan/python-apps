from pdf2docx import Converter

pdf_file = "pdf-sample.pdf"
docx_file = "output.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()