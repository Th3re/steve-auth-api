from api.libs.environment.environmentreader import EnvironmentReader
from api.libs.representation.pretty import PrettyPrint


class Google(EnvironmentReader):
    def __init__(self):
        super()
        self.host = self.get('host')
        self.client_id = self.get('client_id')
        self.client_secret = self.get('client_secret')
        self.redirect_uri = self.get('redirect_uri')
        self.request_url = self.get('request_url')


class Mongo(EnvironmentReader):
    def __init__(self):
        super()
        self.uri = self.get('uri')
        self.user = self.get('user')
        self.password = self.get('password')
        self.database = self.get('database')
        self.collection = self.get('collection')


class Server(EnvironmentReader):
    def __init__(self):
        self.port = self.get('port')


class Environment(PrettyPrint):
    def __init__(self):
        self.server = Server()
        self.google = Google()
        self.mongo = Mongo()

    @staticmethod
    def read():
        return Environment()
