import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    print("=== PASSWORD GENERATOR ===")
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print("Try a longer password for better security.")
            return
    except ValueError:
        print("Please enter a valid number!")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")
    
if__name__="__main__":
    main()

