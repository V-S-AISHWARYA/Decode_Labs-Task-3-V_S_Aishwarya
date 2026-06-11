import string
import secrets
def generate(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    character_pool = string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
        
    if not character_pool:
        return "Error: No character pool selected."
    password = "".join(secrets.choice(character_pool) for _ in range(length))
    return password
def main():
    print("=== Secure Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        if length < 4:
            print(" Password should be at least 4 characters long.")
            return
    except ValueError:
        print(" Invalid input. Please enter a number.")
        return
    include_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    include_nums = input("Include numbers? (y/n): ").strip().lower() == 'y'
    include_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
    secure_password = generate(length, include_upper, include_nums, include_special)
    
    print("\n--------------------------------------")
    print(f"Generated Password: {secure_password}")
    print("--------------------------------------")

if __name__ == "__main__":
    main()
