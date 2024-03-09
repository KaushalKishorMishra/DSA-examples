# remove() method in list
# list of odd numbers
odd = [1, 2, 3, 5, 7, 9]
print(f"Before remove(): {odd}")
# here 2 is not an odd number in the above list
# so we remove it form the list with remove() method
odd.remove(2)
print(f"After remove(): {odd}")

# output:
# Before remove(): [1, 2, 3, 5, 7, 9]
# After remove(): [1, 3, 5, 7, 9]