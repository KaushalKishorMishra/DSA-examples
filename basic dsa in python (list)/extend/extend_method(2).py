courses_IT = ["Bsc.CSIT", "BSc.IT", "BCA" ]
courses_ENG = ["Computer Engineering", "Civil Engineering", "Electrical Engineering", "Mechanical Engineering"]

# printing the list before using extend() method
print(f"Courses offered by TU: {courses_IT} and {courses_ENG}")

# using extend() method with + operator
courses_ENG = courses_ENG + courses_IT

# printing the list after using extend() method
print(f"Courses offered by our college: {courses_ENG}")

# Output:
# Courses offered by TU: ['Bsc.CSIT', 'BSc.IT', 'BCA'] and ['Computer Engineering', 'Civil Engineering', 'Electrical Engineering', 'Mechanical Engineering']
# Courses offered by our college: ['Computer Engineering', 'Civil Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Bsc.CSIT', 'BSc.IT', 'BCA']