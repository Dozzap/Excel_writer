from pdf2image import convert_from_path
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader
import os

POPPLER_PATH = r"C:\Users\dhyla\OneDrive\Desktop\prog\Release-23.07.0-0\poppler-23.07.0\Library\bin"
BASE_PDF_PATH = r'C:\Users\dhyla\OneDrive\Desktop\Excel_writer\120G\Cabinet 10\NCB120G C10D{}.pdf'
BASE_IMAGE_FOLDER = r'C:\Users\dhyla\OneDrive\Desktop\Excel_writer\example\img\D{}'


def convert_pdf_to_images(drawer_number):
    pdf_name = BASE_PDF_PATH.format(drawer_number)
    new_folder_path = BASE_IMAGE_FOLDER.format(drawer_number)

    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

    images = convert_from_path(pdf_name, poppler_path=POPPLER_PATH)

    for i, image in enumerate(images):
        image_path = f'page{i}.jpg'
        full_image_path = os.path.join(new_folder_path, image_path)
        image.save(full_image_path, 'JPEG')
        print(f"Saved {full_image_path}")
    return len(images)

def crop_images(input_directory, start_side):
    crop_folder = os.path.join(input_directory, 'cropimg')
    if not os.path.exists(crop_folder):
        os.makedirs(crop_folder)

    for index, filename in enumerate(sorted(os.listdir(input_directory))):
        if filename.endswith('.jpg'):
            if (start_side == "left" and index % 2 != 0) or (start_side == "right" and index % 2 == 0):
                left, upper, right, lower = 210, 226, 592, 1789
            else:
                left, upper, right, lower = 114, 227, 451, 1789

            crop_area = (left, upper, right, lower)
            image_path = os.path.join(input_directory, filename)
            image = Image.open(image_path)
            cropped_image = image.crop(crop_area)
            cropped_filename = 'cropped_' + filename
            cropped_image.save(os.path.join(crop_folder, cropped_filename))
            print(f"Cropped and saved {cropped_filename}")

    merge_and_clean(crop_folder)


def merge_and_clean(crop_folder):
    pdfs = []

    for filename in sorted(os.listdir(crop_folder)):
        if filename.endswith('.jpg'):
            image_path = os.path.join(crop_folder, filename)
            image = Image.open(image_path)
            pdf_path = os.path.join(crop_folder, filename.replace('.jpg', '.pdf'))
            image.save(pdf_path, 'PDF')
            pdfs.append(pdf_path)

    output_pdf_path = os.path.join(crop_folder, 'merged_cropped.pdf')
    output_pdf = PdfWriter()

    for pdf_path in pdfs:
        with open(pdf_path, 'rb') as f:
            pdf = PdfReader(f)
            output_pdf.add_page(pdf.pages[0])

    with open(output_pdf_path, 'wb') as f:
        output_pdf.write(f)

    print(f"Merged cropped images into {output_pdf_path}")

    for pdf_path in pdfs:
        os.remove(pdf_path)
    print("Deleted individual PDF files.")

def process_pdf(drawer_number, start_side):
    input_directory = BASE_IMAGE_FOLDER.format(drawer_number)
    convert_pdf_to_images(drawer_number)
    crop_images(input_directory, start_side)

def process_pdfs_for_specified_drawers(drawer_list, initial_side="left"):
    start_side = initial_side
    
    for drawer_number in drawer_list:
        num_pages = convert_pdf_to_images(drawer_number)
        process_pdf(drawer_number, start_side)
        
        # If the number of pages is odd, toggle the side for the next drawer.
        if num_pages % 2 != 0:
            start_side = "right" if start_side == "left" else "left"


# Example usage:
drawer_list = [i for i in range(1,12)]  # Suppose 3, 6, 8, 9, and 11 are missing.
process_pdfs_for_specified_drawers(drawer_list, initial_side="left")





