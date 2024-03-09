# create a list of first 20 prime numbers
my_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# find the index of an element in the list with the given starting index
element = 23
start = 5
index = my_list.index(element, start)

# print the index
print("Index of", element, "is", index)

# find the index of an element in the list within the given range
element = 31
start = 5
end = 15
index = my_list.index(element, start, end)

# print the index
print("Index of", element, "is", index)

# Output: 
# Index of 31 is 10