#This is a program that will translate the given input into a list of strings
input1 = "S 5 5 5 5 0 5 P S P 5 P S 5 5 5 5 5 5 5 5 p 0 5 T 5 5 "
input2 = "S " * 17 
input3 = ""
p = input1 + input2 + input3
def clean_data(input_data):
     transformed_string = input_data.replace("5", "S").replace("0", "O").upper().split()

     # Convert the transformed_string to a Python array
     python_array = list(transformed_string)

     return python_array
    
print(len(clean_data(p)))
print(len(clean_data(input1)))
print(len(clean_data(input2)))
print(len(clean_data(input3)))
print()

print(clean_data(p))