from typing import List

from api.contacts.issuer import ContactsIssuer
from api.contacts.manager import Manager
from api.db.store import Store
from api.profile.issuer import Profile


class ContactsManager(Manager):
    def __init__(self, store: Store, contacts_issuer: ContactsIssuer):
        self.store = store
        self.contacts_issuer = contacts_issuer

    def save_contacts(self, user_id: str, token: str):
        contacts = self.contacts_issuer.fetch(user_id, token)
        self.store.save_contacts(user_id, contacts)

    def get_contacts(self, user_id: str) -> List[Profile]:
        return list(map(lambda x: dict(user_id=x[0], email=x[1]), self.store.get_contacts(user_id)))
