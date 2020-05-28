import logging
from http import HTTPStatus

from api.api.api import APICode
from api.app import access_manager, contacts_manager
from api.app import token_issuer, profile_manager

LOG = logging.getLogger(__name__)


def register_user(scope, code):
    credentials = token_issuer.get_credentials(code)
    if not credentials:
        LOG.error('Could not issue proper credentials base on the given code')
        return {
            "code": APICode.ERROR,
            "message": "User has already granted permissions to the app",
        }, HTTPStatus.BAD_REQUEST
    LOG.debug(f'Credentials: {credentials}')
    access_manager.save_identity(credentials)
    user_id = credentials.user_id
    token = access_manager.get_token(user_id)
    contacts_manager.save_contacts(user_id, token)
    profile_manager.save_profile(user_id, token)
    return {
        "code": APICode.OK,
        "message": "User registered",
         "code": APICode.OK,
         "message": f"User {user_id} registered",
    }, HTTPStatus.OK
