import hashlib
def md5_hash(data):
 # Create an instance of the MD5 hash object
 md5 = hashlib.md5()
 # Update the hash object with the encoded data
 md5.update(data.encode('utf-8'))
 # Get the hexadecimal representation of the hash result
 hash_result = md5.hexdigest()
 # Return the hash result
 return hash_result
# Prompt the user to enter the data to be hashed
data = input("Enter the data to be hashed: ")
# Call the md5_hash function with the input data
hashed_data = md5_hash(data)
# Print the MD5 hash
print("MD5 Hash:", hashed_data)
