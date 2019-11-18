import bcrypt


def encrypt_password(password: str) -> str:
    """
    Encryption on a password
    :param password: the password to encrypt
    :return: the hashed password
    """
    return bcrypt.hashpw(password.encode("utf8"),
                         bcrypt.gensalt()).decode("utf8")


def decrypt_password(password: str, hashed_password: str) -> bool:
    """
    Checks if the entered hashed password matches the hashed password in
    database
    :param password: the inputted password
    :param hashed_password: the password hashed in database
    :return: whether or not their hashes match
    """
    return bcrypt.checkpw(password.encode("utf8"),
                          hashed_password.encode("utf8"))
