def check_uppercase(password):
    return any(c.isupper() for c in password)

def check_lowercase(password):
    return any(c.islower() for c in password)

def check_numbers(password):
    return any(c.isdigit() for c in password)

def check_special_characters(password):
    valid_special_characters = {'!', '@', '#'}
    return any(c in valid_special_characters for c in password)

def validate_password(password, criteria):
    if len(password) < 8:
        return f"'{password}' is invalid. Less than 8 characters. Skipping validation."

    valid = True
    missing_criteria = []

    if 1 in criteria and not check_uppercase(password):
        valid = False
        missing_criteria.append("Uppercase letters")

    if 2 in criteria and not check_lowercase(password):
        valid = False
        missing_criteria.append("Lowercase letters")

    if 3 in criteria and not check_numbers(password):
        valid = False
        missing_criteria.append("Numbers")

    if 4 in criteria and not check_special_characters(password):
        valid = False
        missing_criteria.append("Special characters")

    if valid:
        return f"'{password}' is a valid password."
    else:
        return f"'{password}' is invalid. Missing: {', '.join(missing_criteria)}"

def main():
    print("Select criteria to check:\n1: Uppercase letters (A-Z)\n2: Lowercase letters (a-z)\n3: Numbers (0-9)\n4: Special characters (!, @, #)")
    criteria_input = input("Enter criteria (comma-separated, e.g., 1,2,3): ")

    try:
        criteria = list(map(int, criteria_input.split(',')))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    password_list = []
    while True:
        password = input("Enter a password (or type 'done' to finish): ")
        if password.lower() == 'done':
            break
        password_list.append(password)

    for password in password_list:
        result = validate_password(password, criteria)
        print(result)

if __name__ == "__main__":
    main()

