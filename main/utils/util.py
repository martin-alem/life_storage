from django.core.signing import BadSignature, SignatureExpired


def get_cookie(key, request):
    """
    Return the value of a signed cookie
    :param key: the key mapped to the signed cookie value
    :param request: the request object
    :return: string
    """
    salt = "90bed65b7fb6e1129b4de3309c7c1938b6274744cc8a7527a6"
    try:
        signed_cookie = request.get_signed_cookie(key=key, salt=salt, max_age=3600)
        return signed_cookie
    except (KeyError, BadSignature, SignatureExpired):
        return False


def is_logged_in(request):
    user_id = get_cookie("_access_token", request)
    return user_id


def fetch_all(model, category, user):
    media = model.objects.filter(category=category, user=user)
    if len(media) > 0:
        return media
    return []
