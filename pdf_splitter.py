import PyPDF2

def split_pdf(pdf_file, page_numbers):
    # Open the original PDF
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        for i, (start, end) in enumerate(page_numbers):
            writer = PyPDF2.PdfWriter()

            # Add the selected pages to the writer object
            for page_num in range(start-1, end):
                writer.add_page(reader.pages[page_num])

            # Save the new PDF file
            output_filename = f"{pdf_file[:-4]}_part{i+1}.pdf"
            with open(output_filename, 'wb') as output_file:
                writer.write(output_file)
            print(f"Created: {output_filename}")

def get_user_input():
    pdf_file = input("Enter the name of the PDF file (with .pdf extension): ")
    pages = input("Enter the page ranges (e.g., 1-3, 4-6): ")

    # Parse the input page ranges
    page_numbers = []
    for part in pages.split(','):
        start, end = map(int, part.split('-'))
        page_numbers.append((start, end))

    return pdf_file, page_numbers

def main():
    pdf_file, page_numbers = get_user_input()
    split_pdf(pdf_file, page_numbers)

if __name__ == "__main__":
    main()
