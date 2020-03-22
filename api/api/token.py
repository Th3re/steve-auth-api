from http import HTTPStatus
from api.api.api import APICode
from api.app import manager


def get_token(userId):
    token = manager.get_token(userId)
    return {
        "token": token,
        "code": APICode.OK,
        "message": "Token granted",
    }, HTTPStatus.OK