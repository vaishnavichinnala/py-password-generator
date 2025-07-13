# 🔐 Password Generator Project

import random
import string

print("Welcome to the Python Password Generator! 🔐")

# Ask user for password length
try:
    length = int(input("Enter password length: "))
    if length <= 0:
        raise ValueError
except ValueError:
    print("❌ Please enter a valid positive number.")
    exit()

# Ask user for character preferences
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Build character set
characters = ''
if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_special:
    characters += string.punctuation

# Check if at least one type is selected
if not characters:
    print("❌ Please select at least one character type!")
    exit()

# Generate password
password = ''.join(random.choice(characters) for _ in range(length))
print("\n✅ Generated Password:", password)
