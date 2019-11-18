from datetime import datetime, timedelta
from typing import Dict

import jwt

from {{cookiecutter.app_name}}.constants import CONSTANTS

WEB_TOKEN_SECRET_KEY = CONSTANTS.get("WEB_TOKEN_SECRET_KEY")


def encode_token(profile: Dict[str, str]) -> str:
    """
    Encodes profile data into a web token
    :param profile:
    :return:
    """
    return jwt.encode({
        "username": profile["username"],
        "exp": datetime.utcnow() + timedelta(hours=1)},
        WEB_TOKEN_SECRET_KEY,
        algorithm="HS256").decode("utf-8")


def decode_token(token: str) -> Dict[str, str]:
    """
    Decodes a web token and checks
    :param token: the token to decode
    :return:
    """
    try:
        decoded = jwt.decode(token, WEB_TOKEN_SECRET_KEY, algorithms=["HS256"])
        if (datetime.utcnow() - decoded["exp"]).total_seconds() >= 1:
            raise Exception('Token expired. Please login again.')
        return decoded
    except Exception:
        raise Exception('Failed to decode token')
