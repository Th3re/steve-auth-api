from api.app import access_manager
from http import HTTPStatus
from api.api.api import APICode


def get_token(userId):
    token = access_manager.get_token(userId)
    if not token:
        return {
               "code": APICode.ERROR,
               "message": "User unknown",
        }, HTTPStatus.NOT_FOUND
    return {
           "token": token,
           "code": APICode.OK,
           "message": "Token granted",
    }, HTTPStatus.OK
