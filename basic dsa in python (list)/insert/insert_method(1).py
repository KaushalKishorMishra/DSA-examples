# list of odd numbers
odd = [1, 3, 7, 9]
print(f"Before insert(): {odd}")
# inserting 5 at index 2
odd.insert(2, 5)
print(f"After insert(): {odd}")

# output:
# Before insert(): [1, 3, 7, 9]
# After insert(): [1, 3, 5, 7, 9]