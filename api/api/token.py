from api.app import manager
from http import HTTPStatus
from api.api.api import APICode


def get_token(userId):
    token = manager.get_token(userId)
    if token:
        return {
                   "token": token,
                   "code": APICode.OK,
                   "message": "Token granted",
               }, HTTPStatus.OK
    else:
        return {
                   "code": APICode.ERROR,
                   "message": "User unknown",
               }, HTTPStatus.NOT_FOUND
