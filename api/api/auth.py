import logging

from api.app import issuer
from http import HTTPStatus
from api.api.api import APICode

LOG = logging.getLogger(__name__)


def register_user(scope, code):
    credentials = issuer.get_credentials(code)
    LOG.debug(f'Credentials: {credentials}')
    return {
         "code": APICode.OK,
         "message": "User registered",
    }, HTTPStatus.OK