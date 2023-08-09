#Ananya Pillai
import itertools
# Define the character sets for password combinations
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special_characters = '!@#$%^&*()'
# Define the target username
target_username = 'admin'
target_username = input("enter password:")
# Define the maximum number of attempts
max_attempts = 1000000
# Generate all possible password combinations
password_chars = uppercase_letters + lowercase_letters + numbers + special_characters
password_length = 3
password_combinations = itertools.product(password_chars, repeat=password_length)
# Start the brute force attack
attempts = 0
for combination in password_combinations:
    password = ''.join(combination)
# Check if the password matches the target username
    if password == target_username:
        print(f"Password cracked: {password}")
        break
    attempts += 1
    if attempts >= max_attempts:
        print("Exceeded 1000000 attempts")
        break
print(f"Number of attempts made: {attempts}")
