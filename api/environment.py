import os


class Google:
    CLIENT_ID = 'GOOGLE_CLIENT_ID'
    CLIENT_SECRET = 'GOOGLE_CLIENT_SECRET'
    REDIRECT_URI = 'REDIRECT_URI'
    REQUEST_URL = 'REQUEST_URL'

    def __init__(self, client_id, client_secret, redirect_uri, request_url):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.request_url = request_url

    def __repr__(self):
        return f'CLIENT_ID: {self.client_id} CLIENT_SECRET: {self.client_secret}\
        REDIRECT_URI: {self.redirect_uri} REQUEST_URL: {self.request_url}'


class Mongo:
    MONGO_URI = 'MONGO_URI'
    MONGO_USER = 'MONGO_USER'
    MONGO_PASSWORD = 'MONGO_PASSWORD'
    MONGO_DATABASE = 'MONGO_DATABASE'
    MONGO_COLLECTION = 'MONGO_COLLECTION'

    def __init__(self, uri, user, password, database, collection):
        self.uri = uri
        self.user = user
        self.password = password
        self.database = database
        self.collection = collection

    def __repr__(self):
        return f'URI: {self.uri} USER: {self.user} PASSWORD: {self.password}'


class Environment:
    PORT = "PORT"

    def __init__(self, port, google_credentials: Google, mongo: Mongo):
        self.port = port
        self.google_credentials = google_credentials
        self.mongo = mongo

    def __repr__(self):
        return f'PORT: {self.port} GOOGLE_CREDENTIALS: [{self.google_credentials}] MONGO: [{self.mongo}]'


def read_environment() -> Environment:
    return Environment(port=os.environ[Environment.PORT],
                       google_credentials=Google(client_id=os.environ[Google.CLIENT_ID],
                                                 client_secret=os.environ[Google.CLIENT_SECRET],
                                                 redirect_uri=os.environ[Google.REDIRECT_URI],
                                                 request_url=os.environ[Google.REQUEST_URL]),
                       mongo=Mongo(uri=os.environ[Mongo.MONGO_URI],
                                   user=os.environ[Mongo.MONGO_USER],
                                   password=os.environ[Mongo.MONGO_PASSWORD],
                                   database=os.environ[Mongo.MONGO_DATABASE],
                                   collection=os.environ[Mongo.MONGO_COLLECTION]))
