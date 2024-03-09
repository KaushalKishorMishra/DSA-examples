# list of elements in the periodic table
Elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
print(f"Before pop(): {Elements}")
# popping the element from the list at index -1
pop_element = Elements.pop(-1)
print(f"Element popped from index -1: {pop_element}")
print(f"After pop(): {Elements}")


Elements = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
print(f"Before pop(): {Elements}")
#popping the element from the list at index -4
pop_element = Elements.pop(-4)
print(f"Element popped from index -4: {pop_element}")
print(f"After pop(): {Elements}")

# Output:
# Before pop(): ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# Element popped from index -1: Boron
# After pop(): ['Hydrogen', 'Helium', 'Lithium', 'Beryllium']
# Before pop(): ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# Element popped from index -4: Helium
# After pop(): ['Hydrogen', 'Lithium', 'Beryllium', 'Boron']