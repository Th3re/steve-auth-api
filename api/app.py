import logging
import connexion
import pymongo

from api.access.access_manager import AccessManager
from api.access.cache.memory_cache import MemoryAccessCache
from api.db.mongo import MongoStore
from api.environment import Environment
from swagger_ui_bundle import swagger_ui_3_path
from api.credentials.google_issuer import GoogleIssuer

logging.basicConfig(level=logging.DEBUG)

OPENAPI_SPEC_DIR = "openapi/"
API_SPEC = "api.yaml"

log = logging.getLogger(__name__)

env = Environment.read()
log.debug(f'ENV -- {env}')

issuer = GoogleIssuer(env.google)

mongo_client = pymongo.MongoClient(env.mongo.uri, username=env.mongo.user, password=env.mongo.password)

access_cache = MemoryAccessCache()
store = MongoStore(mongo_client, env.mongo.database, env.mongo.collection)
manager = AccessManager(access_cache, store, issuer)


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
