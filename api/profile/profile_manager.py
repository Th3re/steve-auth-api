from typing import Optional

from api.db.store import Store
from api.profile.issuer import Profile, ProfileIssuer
from api.profile.manager import Manager


class ProfileManager(Manager):
    def __init__(self, store: Store, profile_issuer: ProfileIssuer):
        self.store = store
        self.profile_issuer = profile_issuer

    def get_profile(self, user_id: str) -> Optional[Profile]:
        return self.store.get_profile(user_id)

    def save_profile(self, user_id: str, token: str):
        profile = self.profile_issuer.fetch(user_id, token)
        self.store.save_profile(user_id, profile)
