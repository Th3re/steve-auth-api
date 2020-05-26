import logging
from typing import List

from api.contacts.issuer import ContactsIssuer
from api.libs.google.client import Client

LOG = logging.getLogger(__name__)


class GoogleIssuer(ContactsIssuer):
    PERSON_FIELDS = "names,emailAddresses,metadata"

    def __init__(self, api_client: Client):
        self.api_client = api_client

    def fetch(self, user_id: str, token: str) -> List[str]:
        # https://content-people.googleapis.com/v1/people/me/connections?pageSize=10&personFields=
        params = dict(
            personFields=self.PERSON_FIELDS
        )
        connections = self.api_client.get("/v1/people/me/connections", token, params)
        LOG.info(f'USER {user_id} CONNECTIONS {connections}')
        return ["1", "2", "3"]