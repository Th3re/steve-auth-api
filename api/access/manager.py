import abc

from api.model.credentials import Credentials


class Manager(abc.ABC):
    @abc.abstractmethod
    def save_identity(self, credentials: Credentials):
        pass

    @abc.abstractmethod
    def get_token(self, user_id) -> str:
        pass
