import logging

from api.access.cache.cache import AccessCache
from api.access.manager import Manager
from api.credentials.issuer import PermissionIssuer
from api.db.store import Store
from api.model.credentials import Credentials


LOG = logging.getLogger(__name__)


class AccessManager(Manager):
    def __init__(self, access_cache: AccessCache, store: Store, issuer: PermissionIssuer, token_ttl):
        self.access_cache = access_cache
        self.store = store
        self.issuer = issuer
        self.token_ttl = token_ttl

    def save_identity(self, credentials: Credentials):
        self.store.save(credentials)

    def get_token(self, user_id):
        access_token = self.access_cache.get(user_id)
        if access_token:
            LOG.debug(f'Using cached token: {access_token} for user_id: {user_id}')
            return access_token
        credentials = self.store.get(user_id)
        refresh_token = credentials.refresh_token
        access_token = self.issuer.refresh_token(refresh_token)
        self.access_cache.set(user_id, access_token, self.token_ttl)
        return access_token
