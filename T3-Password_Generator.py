import random
import string

def generate_pass(length):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(char) for i in range(length))
    return password

def main():
    print("** Welcome to the Password Generator **")
    while True:
        try:
            length = int(input("Enter length of the password: "))
            if length <= 0:
                print("Length must be a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer.")

    password = generate_pass(length)
    print("Your Generated Password is:", password)


pass_gen=main()
