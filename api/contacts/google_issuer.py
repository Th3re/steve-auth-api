from typing import List

from api.contacts.issuer import ContactsIssuer


class GoogleIssuer(ContactsIssuer):
    def fetch(self, user_id: str, token: str) -> List[str]:
        pass