import random
import string
def generate_password(length, num_alphabets, num_digits, num_special_chars):
    if length < num_alphabets + num_digits + num_special_chars:
        return "The sum of alphabets, digits, and special characters exceeds the password length."
    all_chars = string.ascii_letters + string.digits + string.punctuation
    alphabet_chars = string.ascii_letters
    digit_chars = string.digits
    special_chars = string.punctuation
    password = []
    for _ in range(num_alphabets):
        password.append(random.choice(alphabet_chars))
    for _ in range(num_digits):
        password.append(random.choice(digit_chars))
    for _ in range(num_special_chars):
        password.append(random.choice(special_chars))
    while len(password) < length:
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)

print("Random Password Generator")
length = int(input("Enter password length: "))
num_alphabets = int(input("Enter the number of alphabets: "))
num_digits = int(input("Enter the number of digits: "))
num_special_chars = int(input("Enter the number of special characters: "))
password = generate_password(length, num_alphabets, num_digits, num_special_chars)
print("Generated Password: ",password)
