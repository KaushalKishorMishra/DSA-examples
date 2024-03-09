# list of string
string = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
# print the list before reversing
print(f"Original list: {string}")
# using slicing operator to reverse the list
reversed_list = string[::-1]
# print the list after reversing
print(f"Reversed list: {reversed_list}")

# Output:
# Original list: ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# Reversed list: ['Boron', 'Beryllium', 'Lithium', 'Helium', 'Hydrogen']