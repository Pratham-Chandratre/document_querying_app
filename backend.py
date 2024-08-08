import fitz  # PyMuPDF
from docx import Document

# Document Processing Functions
def extract_text_from_pdf(pdf_file):
    pdf_data = pdf_file.read()  # Read the file into memory
    doc = fitz.open(stream=pdf_data, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text
    return text

def extract_text_from_txt(txt_file):
    text = txt_file.read().decode("utf-8")
    return text
