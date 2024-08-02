from PyPDF2 import PdfReader, PdfWriter

def remove_starting_pages(pdf_path, start_remove, end_remove, output_path):
  
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    # Loop through all the pages and add only those not within the removal range
    for i in range(len(reader.pages)):
        if i < start_remove or i > end_remove:
            writer.add_page(reader.pages[i])

    # Write out the new PDF
    with open(output_path, "wb") as f:
        writer.write(f)

# Usage
input_pdf = "Path/to/the/file"
output_pdf = "output_textbook.pdf"
remove_starting_pages(input_pdf, 1, 11, output_pdf)