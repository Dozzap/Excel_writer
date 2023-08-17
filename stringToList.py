input11 = " "
input22 = " "
input33 = " "
input44 = ""
input55 = ""
p = input11 + input22 + input33+ input44 + input55


def stringToList(input_string):
# Split the input string by spaces to get individual entries
    
    entries = input_string.split()
    
    
    # Create a Python array by converting integers or keeping the original entry
    python_array = []
    for entry in entries:
        if len(str(entry)) < 3:
            print("error")
            break
        if entry.isdigit():
            python_array.append(int(entry))
        else:
            python_array.append(entry)
        # python_array = [int(entry) if entry.isdigit() else entry for entry in entries]

    # Print the resulting array
    return python_array

print(len(stringToList(p)))
print(len(stringToList(input11)))
print(len(stringToList(input22)))
print(len(stringToList(input33)))
print(len(stringToList(input44)))
print(len(stringToList(input55)))
print()    
print(stringToList(p))
