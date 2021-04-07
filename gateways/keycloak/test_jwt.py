import json
from os import environ
from pathlib import Path
from time import time
from uuid import uuid4

from jwcrypto import jwk, jws
from jwcrypto.common import json_encode
from requests import get, post
import yaml
from base64 import b64decode
from http.server import BaseHTTPRequestHandler, HTTPServer
from multiprocessing import Process

keypair_pem = Path("jwks.pem")


realm = "ioggstream"
client_id = "jwt-client"
client_secret = "b90d8bd8-22d6-4b7b-b8b1-eeea7821e7b2"
password = "secret"

realm_url = f"http://localhost:8080/auth/realms/{realm}"
url = f"{realm_url}/protocol/openid-connect/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}


def create_keypair_pem():
    kp = jwk.JWK.generate(kty="RSA", size=4096)
    keypair_pem.write_bytes(
        kp.export_to_pem(private_key=True, password=None) + kp.export_to_pem()
    )


def create_jwks(keypair, overwrite=False):
    keypair_json = Path("jwks.json")
    if keypair_json.exists() and not overwrite:
        raise OSError(f"File already exists {keypair_json}")
    jwks = {"keys": []}
    my_key = keypair.export_public(as_dict=True)
    my_key["use"] = "sig"  # Keycloak wants a restricted key scope.
    jwks["keys"].append(my_key)
    keypair_json.write_text(json.dumps(jwks))


def setup_enviroment():
    create_keypair_pem()
    create_jwks()


def harn_request_token(formdata):
    ret = post(url=url, data=formdata, headers=headers)
    print(ret.content)

    t = ret.json()["access_token"]
    d = yaml.safe_load(b64decode((t.split(".")[1] + "===").encode()))
    print(yaml.dump(d, indent=True))


def create_jwt(payload, keypair, kid=None):
    now = int(time())
    payload.update(
        {"iat": now - 1, "exp": now + 1000,}
    )
    token = jws.JWS(json_encode(payload))
    token.add_signature(
        keypair,
        None,
        json_encode({"alg": "RS256", "kid": keypair.thumbprint()}),
    )
    sig = token.serialize(compact=True)
    return sig


def test_client_jwt():
    keypair = jwk.JWK.from_pem(Path("jwks.pem").read_bytes())

    client_assertion = create_jwt(
        {
            "iss": client_id,
            "sub": client_id,
            "jti": str(uuid4()),
            "aud": realm_url,
        },
        keypair=keypair,
    )
    formdata = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        #  "scope": "email profile",
        "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
        "client_assertion": client_assertion,
    }
    print(formdata)
    harn_request_token(formdata)


def test_client_secret():

    formdata = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        # "username": "ioggstream",
        # "password": "test",
    }
    harn_request_token(formdata)
