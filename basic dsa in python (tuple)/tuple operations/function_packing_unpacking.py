class User:
    def __init__(self, name, age, city, profession):
        self.name = name
        self.age = age
        self.city = city
        self.profession = profession

    def get_user(self):
        # packing the user details into a tuple
        return (self.name, self.age, self.city, self.profession)


# create a user object
user = User("John", 25, "Washington", "AI Engineer")

# unpacking the user details tuple
print("User Details in Tuple:", user.get_user())
name, age, city, profession = user.get_user()

print("Unpacked User Details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Address: {city}")
print(f"Profession: {profession}")


# output:
# Unpacked User Details:
# Name: John
# Age: 25
# Address: Washington
# Profession: AI Engineer