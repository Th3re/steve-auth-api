import abc

from api.model.credentials import Credentials


class PermissionIssuer(abc.ABC):
    @abc.abstractmethod
    def get_credentials(self, code: str) -> Credentials:
        pass
