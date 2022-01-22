import hashlib


def hash_password(password):
    """
        Hashes a password using sha224 algorithm
        :param password string password to be hashed
        :return string
    """
    hashed_password = hashlib.sha224(bytes(password, "utf8")).hexdigest()
    return hashed_password


def set_cookie(key, value, response):
    """
        Sets a signed cookie to the browser
        :param key the key for the cookie value
        :param value the value of the cookie
        :param response the response object
        :return None
    """
    salt = "90bed65b7fb6e1129b4de3309c7c1938b6274744cc8a7527a6"
    response.set_signed_cookie(key=key, value=value, salt=salt, max_age=3600, expires=None, path="/", domain=None, secure=False, httponly=True, samesite="Strict")
