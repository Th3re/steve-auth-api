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
        LOG.debug(f'Connections {response["connections"]}')
        sources = list(map(lambda c: c["metadata"]["sources"], response["connections"]))
        elements = [item for sublist in sources for item in sublist]
        profiles = list(filter(lambda s: s["type"] == "PROFILE", elements))
        return list(map(lambda profile: profile["id"], profiles))

    def fetch(self, user_id: str, token: str) -> List[str]:
        params = dict(personFields=self.PERSON_FIELDS)
        response = self.api_client.get("/v1/people/me/connections", token, params)
        return self.connections_ids(response)
