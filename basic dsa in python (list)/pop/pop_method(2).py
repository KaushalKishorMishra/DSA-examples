# list of elements in the periodic table
Elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
print(f"Before pop(): {Elements}")
# popping the element from the list at index 1
pop_element = Elements.pop()
print(f"Element popped: {pop_element}")
print(f"After pop(): {Elements}")

# Output:
# Before pop(): ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# Element popped: Boron
# After pop(): ['Hydrogen', 'Lithium', 'Beryllium', 'Boron']