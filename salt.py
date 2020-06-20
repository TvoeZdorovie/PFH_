

def hash(password):
    hash_object = hashlib.md5(password.encode())
    a = hash_object.hexdigest()
    return a