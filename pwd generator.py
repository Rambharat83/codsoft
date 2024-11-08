import random
import string

def gernate(length=12):
    cr = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(cr) for _ in range(length))
    return password

while True:
    try:
        length = int(input("Enter password length: "))
        print("Generated Password:", gernate(length))
    except ValueError:
        print("Please enter a valid number for length.")
        continue
    another = input("Generate another password? (yes/no): ").strip().lower()
    if another != 'yes':
        print("Thankyou")
        break
