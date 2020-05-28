import abc
import typing

from api.model.credentials import Credentials
from api.model.token import Token


class PermissionIssuer(abc.ABC):
    @abc.abstractmethod
    def get_credentials(self, code: str) -> typing.Optional[Credentials]:
        pass

    @abc.abstractmethod
    def refresh_token(self, refresh_token) -> Token:
        pass
