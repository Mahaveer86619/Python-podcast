import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extract text from the PDF file located at pdf_path.
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None
