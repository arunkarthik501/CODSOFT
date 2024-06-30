import random
import string

try:
    length = int(input("Enter the desired length of the password: "))
    if length <= 0:
        print("Length should be a positive integer.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid integer for the length.")