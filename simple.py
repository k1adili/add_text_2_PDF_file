import fitz  # PyMuPDF

def add_text_to_pdf(input_pdf_path, output_pdf_path, text_to_add):
    # Open the existing PDF file
    pdf_document = fitz.open(input_pdf_path)

    # Iterate through all pages of the PDF
    for page_num in range(pdf_document.page_count):
        # Get the page from the PDF document
        page = pdf_document[page_num]

        # Create a new text object to add to the page
        text_rectangle = fitz.Rect(100, 100, 300, 120)  # Adjust the rectangle coordinates as needed
        text_point = fitz.Point(10, 10)  # Set the starting point of the text
        page.insert_text(text_point, text_to_add, fontsize=7, fontname="Segoe UI")

    # Save the modified PDF to a new file
    pdf_document.save(output_pdf_path)
    pdf_document.close()

if __name__ == "__main__":
    input_pdf_path = "a.pdf"
    output_pdf_path = "b.pdf"
    text_to_add = "This is the text you want to add."

    add_text_to_pdf(input_pdf_path, output_pdf_path, text_to_add)
