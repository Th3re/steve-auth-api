import logging

from api.app import issuer
from http import HTTPStatus
from api.app import manager
from api.api.api import APICode

LOG = logging.getLogger(__name__)


def register_user(scope, code):
    credentials = issuer.get_credentials(code)
    if credentials:
        LOG.debug(f'Credentials: {credentials}')
        manager.save_identity(credentials)
        return {
             "code": APICode.OK,
             "message": "User registered",
        }, HTTPStatus.OK
    else:
        LOG.error('Could not issue proper credentials base on the given code')
        return {
               "code": APICode.ERROR,
               "message": "User has already granted permissions to the app",
        }, HTTPStatus.BAD_REQUEST
