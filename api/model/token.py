import typing
import datetime

Token = typing.NamedTuple("Token", [('value', str), ('expiration_date', datetime.datetime)])
