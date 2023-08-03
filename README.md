# Excel writer

## Background:
This is a program that I use for my work. This program works as your helper for inputing files in an Excel Sheet. I am given a folder with pdf files containing handwritten notes regarding the inventory of things we keep track at work (for the sake of anonymosity). I am tasked with inputing this data in a database.

I snip parts of the pdf file to turn it into an image while also grouping inputs given their column. I then use an [OCR website](https://www.pen-to-print.com/handwriting-to-text-online-ocr/) to read the data from the images and I double check the data to make sure the OCR did its job right. I Then use the helper methods to clean up the data and later put into the excel sheet using the main program.


## Fixed bug issues:
      Fixed a bug in which the total number of entries does not match the sum of the the inputs
            ### Files affected:
                    clean_data.py
                    stringToList.py

## Current Progress:

Update 2:
      2 (pdf_to_image and crop_image) have been merged into one
      
Update 1:
      Helper functions are created. 

      stringToList: This helper method takes in a string of mixed integer and string. This then creates an array that will store the entries taken from the string input
                  ### check measures:
                                  Given inputs from different pages, This will keep track of how many entries are in the array

## Future plans:
      Create an OCR program      
      Incorporate the output from the helper methods directly to the main program      (Almost complete)
      ✅Create a program that will translate PDF files into Images   
      ✅Create a program that will crop certain area of the Images
