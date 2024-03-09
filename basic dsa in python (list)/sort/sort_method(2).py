# list of string
string = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron"]
# print the list before sorting
print(f"Unsorted list: {string}")
# using sort() method to sort the list
string.sort()
# print the list after sorting
print(f"Sorted list: {string}")
# sorting the list in reverse
string.sort(reverse=True)
# print the list after sorting in reverse
print(f"Sorted list in reverse: {string}")

# output
# Unsorted list: ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron']
# Sorted list: ['Beryllium', 'Boron', 'Helium', 'Hydrogen', 'Lithium']
# Sorted list in reverse: ['Lithium', 'Hydrogen', 'Helium', 'Boron', 'Beryllium']
