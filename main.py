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

# input1 = "12905a 12903 12909 12911 12918 12913 12911 12914 12915 12016 12922 12917 12418 12924 12918 12923 12904 12921 12905 12013 12891 12922 12920 14521 12921 12921 14550a 14550 14550i 14550 8106 8107 8107a 8108 14546 8112 14549 8111 24268 24272 24274 24270 24268 7856a 29271 7858 7859 7860 7866 7861 2861 7863 7864 7865 7874 7867 7870 7871 7872 7875"
# input2 = "5 O S 5 0 5 0 5 S S 5 5 5 5 T T T T T T T T 5 5 5 0 s 5 0 O 5 5 5 5 5 5 5 5 5 5 5 5 5 S 5 S S P S 5 0 5 5 5 5 5 5 5 5 s"
# # def stringToList(input_string):
# # # Split the input string by spaces to get individual entries
# #     entries = input_string.split()

# #     # Create a Python array by converting integers or keeping the original entry
# #     python_array = [int(entry) if entry.isdigit() else entry for entry in entries]

# #     # Print the resulting array
# #     return python_array

# # def clean_data(input_data):
# #     transformed_string = input_data.replace("5", "S").replace("0", "O").upper().split()

# #     # Convert the transformed_string to a Python array
# #     python_array = list(transformed_string)

# #     return python_array

suffel_Num = [9021, 9022, 9023, 9026, '9028a', 9029, 4510, 4510, 4511, 4511, 4512, 4512, 9015, 22060, 1438, 1433, 1439, 1440, 4512, 1441, 8035, 4509, 22060, 1434, 1434, 1430, '1436a', 1437, 22062, 1431, 12119, 14609, 22056, 22060, 14606, '14606a', 14607, 14605, '14598a', 141599, 14600, 14602, 14603, '14603a']

cleaned_data =[
'S', 'S', 'S', 'S', 'S', 'O', 'S', 'P', 'S', 'P', 'S', 'P', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'P', 'O', 'S', 'T', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S'
]
room = ['120B'] * len(suffel_Num)
cabinet = [14] * len(suffel_Num)
drawer = [2] * len(suffel_Num)


# Check if the number of Sample types and the number of Suffel numbers size are the same
# If they are not the same, then the program will not run
if len(cleaned_data) != len(suffel_Num):
    print("Size of cleaned_data: ", len(cleaned_data))
    print("Size of suffel_Num: ", len(suffel_Num))
    print('The number of Sample types and the number of Suffel numbers are not the same')
    exit()

data = {
    'Suffel Number' :suffel_Num,
    'Sample type (S=Sample, P=Polished section, T=Thin section, O=Offcut)':cleaned_data,
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
