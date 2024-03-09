# list of students in a class with their name and marks
students = [["John", 90], ["Alex", 85], ["Richard", 80], ["David", 95], ["Matthew", 75]]
# print the list before sorting
print(f"Unsorted list: {students}")

# function to sort the list by marks
def sort_by_marks(student):
    return student[1]

# print the list after sorting by marks
students.sort(key=sort_by_marks)
print(f"Sorted list by marks: {students}")

# function to sort the list by name
def sort_by_name(student):
    return student[0]

# print the list after sorting by name
students.sort(key=sort_by_name)
print(f"Sorted list by name: {students}")

# output:
# Unsorted list: [['John', 90], ['Alex', 85], ['Richard', 80], ['David', 95], ['Matthew', 75]]
# Sorted list by marks: [['Matthew', 75], ['Richard', 80], ['Alex', 85], ['John', 90], ['David', 95]]
# Sorted list by name: [['Alex', 85], ['David', 95], ['John', 90], ['Matthew', 75], ['Richard', 80]]