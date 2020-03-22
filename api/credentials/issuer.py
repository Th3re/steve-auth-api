import abc

from api.model.credentials import Credentials


class PermissionIssuer(abc.ABC):
    @abc.abstractmethod
    def get_credentials(self, code: str) -> Credentials:
        pass

    @abc.abstractmethod
    def refresh_token(self, refresh_token) -> str:
        pass
