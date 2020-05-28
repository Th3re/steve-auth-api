import datetime
import typing

Token = typing.NamedTuple("Token", [('value', str), ('expiration_date', datetime.datetime)])
