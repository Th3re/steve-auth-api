import logging
import time

from api.access.manager import Manager
from api.credentials.issuer import PermissionIssuer
from api.db.store import Store
from api.libs.cache.cache import Cache
from api.model.credentials import Credentials

LOG = logging.getLogger(__name__)


class AccessManager(Manager):
    def __init__(self, access_cache: Cache, store: Store, issuer: PermissionIssuer):
        self.access_cache = access_cache
        self.store = store
        self.issuer = issuer

    def save_identity(self, credentials: Credentials):
        self.store.save_credentials(credentials)

    def get_token(self, user_id):
        access_token = self.access_cache.get(user_id)
        if access_token:
            return access_token
        credentials = self.store.get_credentials(user_id)
        if not credentials:
            return
        refresh_token = credentials.refresh_token
        token = self.issuer.refresh_token(refresh_token)
        ttl = token.expiration_date.timestamp() - time.time()
        self.access_cache.set(user_id, token.value, max(ttl, 0))
        return token.value
