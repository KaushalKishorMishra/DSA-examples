# create a tuple of User details
user = ("John", 25, "Washington", "AI Engineer")

print(f"User: {user}")

# unpack the tuple
(name, age, city, profession) = user

print("Unpacked User Details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Address: {city}")
print(f"Profession: {profession}")

# output:
# User: ('John', 25, 'Washington', 'AI Engineer')
# Unpacked User Details:
# Name: John
# Age: 25
# Address: Washington
# Profession: AI Engineer
