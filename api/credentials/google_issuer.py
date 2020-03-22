import jwt
import logging
import requests

from api.model.credentials import Credentials
from api.credentials.issuer import PermissionIssuer

LOG = logging.getLogger(__name__)


class GoogleIssuer(PermissionIssuer):
    def __init__(self, google_configuration):
        self.request_url = google_configuration.request_url
        self.redirect_uri = google_configuration.redirect_uri
        self.client_secret = google_configuration.client_secret
        self.client_id = google_configuration.client_id

    def get_credentials(self, code: str) -> Credentials:
        response = requests.post(url=self.request_url,
                                 data=dict(grant_type='authorization_code',
                                           redirect_uri=self.redirect_uri,
                                           code=code,
                                           client_id=self.client_id,
                                           client_secret=self.client_secret))
        data = response.json()
        LOG.debug(f'Authentication response: {data}')
        subject = self.__get_subject(data['id_token'])
        return Credentials(refresh_token=data['refresh_token'], user_id=subject)

    @staticmethod
    def __get_subject(id_token):
        decoded_token = jwt.decode(id_token, verify=False, algorithms=['RS256'])
        return decoded_token['sub']

    def refresh_token(self, refresh_token) -> str:
        response = requests.post(url=self.request_url,
                                 data=dict(grant_type='refresh_token',
                                           refresh_token=refresh_token,
                                           redirect_uri=self.redirect_uri,
                                           client_id=self.client_id,
                                           client_secret=self.client_secret))
        data = response.json()
        LOG.debug(f'Authentication response: {data}')
        token = data['access_token']
        return token
