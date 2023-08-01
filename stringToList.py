#This will turn given string of entries into an array whilst keeping their original data type if string or int
input1 = "9021 9022 9023 9026 9028a 9029 4510 4510 4511 4511 4512 4512 9015 22060 1438 1433 1439 1440 4512 1441 8035 4509 22060 1434 1434 1430 1436a"
input2 = " 1437 22062 1431 12119 14609 22056 22060 14606 14606a 14607 14605 14598a 141599 14600 14602 14603 14603a"
input3 = ""

p = input1 + input2 + input3


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
print()    
print(stringToList(p))