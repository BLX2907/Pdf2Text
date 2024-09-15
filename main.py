from pdftext.extraction import plain_text_output

# Define the PDF file path
PDF_PATH = 'download.pdf'

# Extract text from pages 1 to 34
text = plain_text_output(PDF_PATH, sort=True, hyphens=False, page_range=list(range(1, 33)))

# Write the extracted text to output.txt
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text)

print("Text has been extracted and saved to output.txt")
