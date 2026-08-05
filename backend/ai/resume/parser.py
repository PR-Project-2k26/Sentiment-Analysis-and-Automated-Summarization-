import fitz  # PyMuPDF

def extract_resume_text(pdf_path):
    """
    Extracts text from a PDF resume.

    Args:
        pdf_path (str): Path to the uploaded PDF.

    Returns:
        str: Extracted text.
    """

    text = ""

    doc = fitz.open(pdf_path)

    for page in doc:
        text += page.get_text()

    doc.close()

    return text.strip()