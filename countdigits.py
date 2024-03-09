# number of digits
num = int(input("Enter a multi digit number: "))
count = 0

while num > 0:
    num = num // 10 
    count+=1

print(f"Number of digits = {count}")

# Output: 
# Enter a multi digit number: 123456
# Number of digits = 6