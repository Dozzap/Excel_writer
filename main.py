#Excel writer Program
#Given an excel sheet with provided information
#This program will write the information to an already existing excel file
#Given an array of values, it will write the informations to the excel file

#Importing the necessary libraries
import pandas as pd
import numpy as np

#Clean up the data
#This function will take in the data and clean it up
#It will return the cleaned up data
sample_Type = ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 
        'T', 'T', '0', '5', '5', '0', '5', '5', 'S', '5', '0', 'S', 
        '0', '0', '5']

cleaned_Type = ['O' if x == '0' else 'S' if x == '5' else x for x in sample_Type]
# Define the dictionary of the data you want to add

suffel_Num = [21396, 21397, 21398, 21399, 21400, 21401, 21402, 21403, 21404, 21405, 21406, 21407, 21408, 21409, 21409, 21409, '21408a', 21408, 21408, 21402, 21403, 21404, 21404, 21405, 21405, 21406, 21407]

cleaned_data =[
'S', 'S', 'S', 'S', 'S', 'O', 'S', 'P', 'S', 'P', 'S', 'P', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'P', 'O', 'S', 'T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'
]
room = ['120B'] * len(suffel_Num)
cabinet = [13] * len(suffel_Num)
drawer = [1] * len(suffel_Num)
Quantity = [1] * len(suffel_Num)
#Check if the number of Sample types and the number of Suffel numbers size are the same
#If they are not the same, then the program will not run
if len(suffel_Num) != len(cleaned_Type):
    print("The number of Sample types and the number of Suffel numbers are not the same")
    print("Please check the data")
    exit()

data = {
    'Quantity': Quantity,
    'Suffel Number' :suffel_Num,
    'Sample type (S=Sample, P=Polished section, T=Thin section, O=Offcut)':cleaned_Type,
    'Room':room,
    'Cabinet Number':cabinet,
    'Drawer Number':drawer,
}

# Create a DataFrame from your data
df = pd.DataFrame(data)

# Load the existing Excel file
existing_file = r'C:\Users\dhyla\OneDrive\Desktop\Excel_writer\120B Inventory Book DONE C12,  D13.xlsx'

# Load the existing Excel file into a pandas DataFrame
existing_df = pd.read_excel(existing_file)

# Append the new data to the existing DataFrame
merged_df = pd.concat([existing_df, df], ignore_index=True)

# Save the merged DataFrame to the existing Excel file
merged_df.to_excel(existing_file, index=False)
