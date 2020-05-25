import abc

from typing import List


class ContactsIssuer(abc.ABC):
    @abc.abstractmethod
    def fetch(self, user_id: str, token: str) -> List[str]:
        return ["1", "2", "3"]
