import abc
from typing import Optional

from api.profile.issuer import Profile


class Manager(abc.ABC):
    @abc.abstractmethod
    def save_profile(self, user_id: str, token: str):
        pass

    @abc.abstractmethod
    def get_profile(self, user_id: str) -> Optional[Profile]:
        pass
