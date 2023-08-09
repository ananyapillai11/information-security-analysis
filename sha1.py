import hashlib
def sha1_hash(message):
# Create an instance of the SHA-1 hash object
 sha1 = hashlib.sha1()
# Update the hash object with the encoded message
 sha1.update(message.encode('utf-8'))
# Get the hexadecimal representation of the hash result
 hash_result = sha1.hexdigest()
# Return the hash result
 return hash_result
# Prompt the user to enter the message to be hashed
message = input("Enter the message: ")
# Call the sha1_hash function with the input message
hashed_message = sha1_hash(message)
# Print the original message and its SHA-1 hash
print("Original Message:", message)
print("SHA-1 Hash:", hashed_message)
