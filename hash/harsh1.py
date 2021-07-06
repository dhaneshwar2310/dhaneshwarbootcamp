import hashlib

# encoding dhaneshwar.vbootcamp using md5 hash
# function
result = hashlib.md5(b'dhaneshwar.vbootcamp')

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.digest())
