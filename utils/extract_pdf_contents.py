import os
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def process_pdfs(input_dir, output_dir):
    """Extract text from all PDFs in the input directory and save to the output directory."""
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

if __name__ == "__main__":
    input_directory = "raw"  # Directory containing the PDF files
    output_directory = "extracted_text"  # Directory to save the extracted text files
    process_pdfs(input_directory, output_directory)