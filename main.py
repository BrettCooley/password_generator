# Password Generator Project
import random  # Import the random module to generate random choices

# Lists of possible characters for the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '£']

print("Welcome to the Password Generator!")  # Welcome message for the user

# Get the number of each type of character from the user
total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

password_list = []  # Initialize an empty list to store password characters

# Add the specified number of random letters to the password list
for char in range(1, total_letters + 1):
    password_list += random.choice(letters)

# Add the specified number of random symbols to the password list
for char in range(1, total_symbols + 1):
    password_list += random.choice(symbols)

# Add the specified number of random numbers to the password list
for char in range(1, total_numbers + 1):
    password_list += random.choice(numbers)

# Shuffle the list to randomize the order of characters
random.shuffle(password_list)

password = ""  # Initialize an empty string for the final password
# Convert the list of characters into a single string
for char in password_list:
    password += char

print(password)  # Print the generated password
