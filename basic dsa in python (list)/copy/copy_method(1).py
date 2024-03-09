string = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
# print the list before copying
print(f"Original list: {string}")
# using copy() method to copy the list
copied_list = string.copy()
# operating on the copied list
copied_list.reverse()
# print the list after operating on the copied list
print(f"Reversing copied list: {copied_list}")
# print the original list after operating on the copied list
print(f"Original list after operating on copied list: {string}")


# Output:
# Original list: ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# Reversing copied list: ['Boron', 'Beryllium', 'Lithium', 'Helium', 'Hydrogen']
# Original list after operating on copied list: ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']