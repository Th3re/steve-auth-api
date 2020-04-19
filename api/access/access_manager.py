import time
import logging

from api.db.store import Store
from api.access.manager import Manager
from api.model.credentials import Credentials
from api.access.cache.cache import AccessCache
from api.credentials.issuer import PermissionIssuer


LOG = logging.getLogger(__name__)


class AccessManager(Manager):
    def __init__(self, access_cache: AccessCache, store: Store, issuer: PermissionIssuer):
        self.access_cache = access_cache
        self.store = store
        self.issuer = issuer

    def save_identity(self, credentials: Credentials):
        self.store.save(credentials)

    def get_token(self, user_id):
        access_token = self.access_cache.get(user_id)
        if access_token:
            return access_token
        credentials = self.store.get(user_id)
        if credentials:
            refresh_token = credentials.refresh_token
            token = self.issuer.refresh_token(refresh_token)
            ttl = token.expiration_date.timestamp() - time.time()
            self.access_cache.set(user_id, token.value, max(ttl, 0))
            return token.value
