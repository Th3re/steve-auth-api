import abc

from typing import List


class Manager(abc.ABC):
    @abc.abstractmethod
    def save_contacts(self, user_id: str, token: str):
        pass

    @abc.abstractmethod
    def get_contacts(self, user_id: str) -> List[str]:
        pass
