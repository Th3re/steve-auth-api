import abc

from api.model.credentials import Credentials

from typing import List


class Store(abc.ABC):
    @abc.abstractmethod
    def save_credentials(self, credentials: Credentials):
        pass

    @abc.abstractmethod
    def get_credentials(self, user_id: str) -> Credentials:
        pass

    @abc.abstractmethod
    def save_contacts(self, user_id: str, contacts: List[str]):
        pass

    @abc.abstractmethod
    def get_contacts(self, user_id: str) -> List[str]:
        pass
