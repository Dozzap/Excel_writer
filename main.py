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
# sample = my_array = ['O', 'S', 'S', 'S', 'S', 'O', 'P', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'O', 'S', 'S', 'S', 'S', 'S', 'O', 'S', 'S', 'O', 'P', 'S', 'O', 'S', 'S', 'O', 'S', 'S', 'S', 'O', 'P', 'S', 'S', 'S', 'O', 'P', 'S', 'O', 'P', 'S', 'O', 'P', 'P', 'P', 'P', 'O', 'S', 'S', 'O', 'S', 'P', 'P', 'P', 'S', 'S', 'O', 'P', 'S', 'O', 'P', 'S', 'S', 'S', 'O', 'P']

# cleaned_data = ['O' if x == '0' else 'S' if x == '5' else x for x in sample]

# Define the dictionary of the data you want to add
suffel_Num =[    12822, 12822, 12823, 12824, "12824a", 12827, 12827, 12828, 12828, "12828a", "12823a",
    12829, 12829, 12830, 12831, 12832, 12832, 12834, "12834b", "12834b", 12835, 12837, 12837, 12838, 12840, 12841, "12841",
        12843, 14692, 12822, 12823, 12823, 12822, 14698, 14699, 14916, 14918, 14919,
    12827, 12824, 12832, 12828, 12834, 1837, 14920, 14696, 22218, 22219, 22220, 22221,
    22222, 22223, 22224, 14922,
        22227, 22217, 22228, 22229, 22230, 22231, "22231a", 22232, "22232a", "22232b",
    12919, 12885, 12884, 12887, 12890,
    12891, 12898, 12899, 12900, 12902, 12903, 12905]

room = ['120B'] * len(suffel_Num)
cabinet = [13] * len(suffel_Num)
drawer = [6] * len(suffel_Num)

# Array of skip_values
skip_values = []

# Create the 'Quantity' column by checking if 'Suffel Number' is in 'skip_values'
quantity = [1 if str(x) not in skip_values else np.NaN for x in suffel_Num]

#Check if the number of Sample types and the number of Suffel numbers size are the same
#If they are not the same, then the program will not run
# if len(cleaned_data) != len(suffel_Num):
#     print("Size of cleaned_data: ", len(cleaned_data))
#     print("Size of suffel_Num: ", len(suffel_Num))
#     print('The number of Sample types and the number of Suffel numbers are not the same')
#     exit()

data = {
    'Quantity': quantity,
    'Suffel Number' :suffel_Num,
    # 'Sample type (S=Sample, P=Polished section, T=Thin section, O=Offcut)':cleaned_data,
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
