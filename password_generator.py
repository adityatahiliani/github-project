import random
import string

def generate_password(length=12, use_special_chars=True):
    """Generate a random password.

    Args:
        length (int): Length of the password.
        use_special_chars (bool): Whether to include special characters.

    Returns:
        str: Generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = string.ascii_letters + string.digits
    if use_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
