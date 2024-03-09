address = ["Kathmandu"]
print(f"Before append(): {address}")
address.append(3)
address.append("Nepal")
print(f"After append(): Address: {address[0]}-{address[1]}, {address[2]}")

# output:
# Before append(): ['Kathmandu']
# After append(): Address: Kathmandu-3, Nepal
