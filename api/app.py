import logging
import pymongo
import connexion

from api.access.access_manager import AccessManager
from api.libs.cache.memory import MemoryAccessCache
from api.contacts.contacts_manager import ContactsManager
from api.db.mongo import MongoStore
from api.environment import Environment
from swagger_ui_bundle import swagger_ui_3_path
from api.credentials.google_issuer import GoogleIssuer as GoogleCredentialsIssuer
from api.contacts.google_issuer import GoogleIssuer as GoogleContactsIssuer

logging.basicConfig(level=logging.DEBUG)

OPENAPI_SPEC_DIR = "openapi/"
API_SPEC = "api.yaml"

log = logging.getLogger(__name__)

env = Environment.read()
log.debug(f'ENV -- {env}')

token_issuer = GoogleCredentialsIssuer(env.google)
contacts_issuer = GoogleContactsIssuer()

mongo_client = pymongo.MongoClient(env.mongo.uri, username=env.mongo.user, password=env.mongo.password)

access_cache = MemoryAccessCache()
store = MongoStore(mongo_client, env.mongo.database, env.mongo.collection)
access_manager = AccessManager(access_cache, store, token_issuer)
contacts_manager = ContactsManager(store, contacts_issuer)


def main():
    options = {"swagger_path": swagger_ui_3_path}
    app = connexion.FlaskApp(
        __name__, specification_dir=OPENAPI_SPEC_DIR, options=options
    )
    app.add_api(
        API_SPEC,
        arguments={"title": "Location API"}
    )
    app.run(port=env.server.port)
