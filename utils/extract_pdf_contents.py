import os
import PyPDF2
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF file using pdfplumber."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
            return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def process_pdfs(input_dir, output_dir):
    """Extract text from all PDFs in the input directory using pdfplumber."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            text = extract_text_from_pdf(pdf_path)
            if text:
                output_file = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.txt")
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"Extracted text saved to: {output_file}")
            else:
                print(f"Failed to extract text from: {pdf_path}")