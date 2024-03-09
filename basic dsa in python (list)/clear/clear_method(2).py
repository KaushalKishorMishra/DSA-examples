# list of top 10 prime numbers 

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(f"Before clear(): {prime}")
# clear the list with del operator
del prime[:]
print(f"After clear(): {prime}")

# output:
# Before clear(): [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# After clear(): []
