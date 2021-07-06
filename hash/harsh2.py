import hashlib

# initializing string
str2hash = "dhaneshwar.vbootcam"

# encoding dhaneshwar.vbootcam using encode()
# then sending to md5()
result = hashlib.md5(str2hash.encode())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())
