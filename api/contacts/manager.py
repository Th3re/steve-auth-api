import abc
from typing import List

from api.profile.issuer import Profile


class Manager(abc.ABC):
    @abc.abstractmethod
    def save_contacts(self, user_id: str, token: str):
        pass

    @abc.abstractmethod
    def get_contacts(self, user_id: str) -> List[Profile]:
        pass
