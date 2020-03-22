from http import HTTPStatus
from api.api.api import APICode


def get_token(userId):
    return {
               "token": "abc",
               "code": APICode.OK,
               "message": "User registered",
           }, HTTPStatus.OK