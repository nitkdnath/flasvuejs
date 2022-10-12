import bcrypt

def encrypt_password(password):
    pwhash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    return pwhash


def compare_passwords(password, hashed_password):
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False