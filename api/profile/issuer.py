import abc
import typing


Profile = typing.NamedTuple('Profile', [('user_id', str), ('email', str)])


class ProfileIssuer(abc.ABC):
    @abc.abstractmethod
    def fetch(self, user_id: str, token: str) -> Profile:
        pass
