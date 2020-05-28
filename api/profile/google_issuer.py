from api.libs.google.client import Client
from api.profile.issuer import ProfileIssuer, Profile


class GoogleProfileIssuer(ProfileIssuer):
    def __init__(self, api_client: Client):
        self.api_client = api_client

    def fetch(self, user_id: str, token: str) -> Profile:
        response = self.api_client.get(f'gmail/v1/users/me/profile', token, dict())
        return Profile(user_id, response['emailAddress'])
