# a mixed of numbers and dictionaries list that inserts a tuple at index 2
list = [1, 3, 7, 9, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}]
print(f"Before insert(): {list}")
# inserting a tuple at index 2
list.insert(2, (5, 6))
print(f"After insert(): {list}")

# output:
# Before insert(): [1, 3, 7, 9, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}]
# After insert(): [1, 3, (5, 6), 7, 9, {'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}]