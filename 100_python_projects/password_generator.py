import string
import secrets  # More secure for cryptographically strong passwords

def generate_password(length=16, include_lowercase=True, include_uppercase=True, include_digits=True, include_symbols=True):
    """Generates a strong, customizable password.

    Args:
        length: Desired password length (default 16).
        include_lowercase: Include lowercase letters (default True).
        include_uppercase: Include uppercase letters (default True).
        include_digits: Include digits (default True).
        include_symbols: Include symbols (default True).

    Returns:
        The generated password as a string.
    """

    character_pool = ""
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation 

    # Use secrets for enhanced security (optional but recommended)
    password = ''.join(secrets.choice(character_pool) for _ in range(length))

    return password

# Generate and print a few passwords with different options:

print("Strong password:", generate_password())
print("No symbols:", generate_password(include_symbols=False))
print("Short password:", generate_password(length=10))
print("Extra strong (24 characters):", generate_password(length=24))
