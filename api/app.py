import logging
import connexion

from api.environment import read_environment
from swagger_ui_bundle import swagger_ui_3_path
from api.credentials.google_issuer import GoogleIssuer

logging.basicConfig(level=logging.DEBUG)

OPENAPI_SPEC_DIR = "openapi/"
API_SPEC = "api.yaml"

env = read_environment()
log = logging.getLogger(__name__)
log.debug(f'ENV -- {env}')
issuer = GoogleIssuer(env.google_credentials)


def main():
    options = {"swagger_path": swagger_ui_3_path}
    app = connexion.FlaskApp(
        __name__, specification_dir=OPENAPI_SPEC_DIR, options=options
    )
    app.add_api(
        API_SPEC,
        arguments={"title": "Location API"}
    )
    app.run(port=env.port)
