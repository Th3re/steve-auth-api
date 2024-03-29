from typing import List

import pymongo

from api.db.store import Store
from api.model.credentials import Credentials
from api.profile.issuer import Profile


class MongoStore(Store):
    USER_ID = 'userId'
    REFRESH_TOKEN = 'refreshToken'
    EMAIL = 'email'
    CONTACTS = 'contacts'

    def __init__(self, client: pymongo.MongoClient, database, collection):
        self.client = client
        self.collection = self.client[database][collection]

    def save_credentials(self, credentials: Credentials):
        document = {
            '$set': {
                self.USER_ID: credentials.user_id,
                self.REFRESH_TOKEN: credentials.refresh_token,
            }
        }
        query = {
            self.USER_ID: credentials.user_id
        }
        self.collection.find_one_and_update(query, document, upsert=True)

    def _get_user(self, user_id: str):
        query = {
            self.USER_ID: user_id
        }
        return self.collection.find_one(query)

    def get_credentials(self, user_id) -> Credentials:
        document = self._get_user(user_id)
        return Credentials(user_id=user_id, refresh_token=document[self.REFRESH_TOKEN]) if document else None

    def save_contacts(self, user_id: str, contacts: List[str]):
        document = {
            '$set': {
                self.CONTACTS: contacts
            }
        }
        query = {
            self.USER_ID: user_id
        }
        self.collection.find_one_and_update(query, document, upsert=True)

    def get_contacts(self, user_id: str) -> List[Profile]:
        document = self._get_user(user_id)
        user_contacts = set(document[self.CONTACTS]) if document else None
        all_contacts = self.collection.find()
        contacts = set(map(lambda x: x[self.USER_ID], all_contacts))
        return list(map(self.get_profile, contacts.intersection(user_contacts)))

    def get_profile(self, user_id: str) -> Profile:
        document = self._get_user(user_id)
        return Profile(user_id=user_id, email=document[self.EMAIL]) if document else None

    def save_profile(self, user_id: str, profile: Profile):
        document = {
            '$set': {
                self.EMAIL: profile.email
            }
        }
        query = {
            self.USER_ID: user_id
        }
        self.collection.find_one_and_update(query, document, upsert=True)
