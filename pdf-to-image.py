from pdf2image import convert_from_path

# Input PDF file path
pdf_file = r'C:\Users\dhyla\OneDrive\Desktop\Cabinet 13\NCB120B C13D1.pdf'

# Output image format (can be 'jpeg', 'png', 'tiff', 'ppm')
output_format = 'jpeg'

# Convert PDF to images
images = convert_from_path(pdf_file, output_folder=None, fmt=output_format)

# Save each image to a file
for i, image in enumerate(images):
    image_path = rf'C:\Users\dhyla\OneDrive\Desktop\Cabinet 13\NCB120B C13D{i + 1}.jpeg'
    image.save(image_path)
