# list of elements in the periodic table
Elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
print(f"Before pop(): {Elements}")
# popping the element from the list at index 5
pop_element = Elements.pop(5)
print(f"Element popped: {pop_element}")
print(f"After pop(): {Elements}")


# Output:
# Before pop(): ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# IndexError: pop index out of range
