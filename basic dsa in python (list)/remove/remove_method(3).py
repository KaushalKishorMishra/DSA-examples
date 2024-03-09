# remove() method in list
# list of odd numbers
odd = [1, 3, 5, 7, 9]
print(f"Before remove(): {odd}")
# here 2 is not an odd number in the above list
# so we remove it form the list with remove() method
odd.remove(10)
print(f"After remove(): {odd}")

# output:
# Before remove(): [1, 3, 5, 7, 9]
# Traceback (most recent call last):
#   File "path of the file\Codes\basic dsa in python\remove\remove_method(3).py", line 7, in <module>
#     odd.remove(10)
# ValueError: list.remove(x): x not in list