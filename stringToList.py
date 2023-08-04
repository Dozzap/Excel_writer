#This will turn given string of entries into an array whilst keeping their original data type if string or int
input1 = ""
input2 = ""
input3 = ""
input4 = ""
input5 = ""
p = input1 + input2 + input3 input4 + input5


def stringToList(input_string):
# Split the input string by spaces to get individual entries
    entries = input_string.split()

    # Create a Python array by converting integers or keeping the original entry
    python_array = [int(entry) if entry.isdigit() else entry for entry in entries]

    # Print the resulting array
    return python_array

print(len(stringToList(p)))
print(len(stringToList(input1)))
print(len(stringToList(input2)))
print(len(stringToList(input3)))
print(len(stringToList(input4)))
print(len(stringToList(input5)))
print()    
print(stringToList(p))
