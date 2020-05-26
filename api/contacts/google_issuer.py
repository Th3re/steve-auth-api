import logging
from typing import List

from api.contacts.issuer import ContactsIssuer
from api.libs.google.client import Client

LOG = logging.getLogger(__name__)


class GoogleIssuer(ContactsIssuer):
    PERSON_FIELDS = "names,emailAddresses,metadata"

    def __init__(self, api_client: Client):
        self.api_client = api_client

    @staticmethod
    def connections_ids(response):
        sources = map(lambda c: c['metadata']['sources'], response['connections'])
        return [list(filter(lambda s: s['type'] == "PROFILE", source))[0]['id'] for source in sources]

    def fetch(self, user_id: str, token: str) -> List[str]:
        params = dict(
            personFields=self.PERSON_FIELDS
        )
        response = self.api_client.get("/v1/people/me/connections", token, params)
        return self.connections_ids(response)
