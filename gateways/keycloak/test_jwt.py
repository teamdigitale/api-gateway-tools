import json
from os import environ
from pathlib import Path
from time import time
from uuid import uuid4

from jwcrypto import jwk, jws
from jwcrypto.common import json_encode
from requests import get, post

keypair_pem = Path("jwks.pem")


realm = "ioggstream"
client_id = "jwt-client"
client_secret = "b90d8bd8-22d6-4b7b-b8b1-eeea7821e7b2"
password = "test"

url = f"http://localhost:8080/auth/realms/{realm}/protocol/openid-connect/token"

headers = {"Content-Type": "application/x-www-form-urlencoded"}


def harn_request_token(formdata):
    ret = post(url=url, data=formdata, headers=headers)
    print(ret.content)

    t = ret.json()["access_token"]
    d = yaml.load(b64_decode((t.split(".")[1] + "===").encode()))
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
        json_encode({"alg": "RS256"}),
        json_encode({"kid": keypair.thumbprint()}),
    )
    sig = token.serialize(compact=True)
    return sig


def test_client_jwt():
    keypair = jwk.JWK.from_pem(Path("jwks.pem").read_bytes())

    client_assertion = create_jwt(
        {
            "iss": "antani",
            "sub": client_id,
            "jti": str(uuid4()),
            "aud": "http://localhost:8080/auth/realms/ioggstream",
        },
        keypair=keypair,
    )
    formdata = {
        "grant_type": "client_credentials",
        "client_id": "myclient",
        #  "scope": "email profile",
        # "resource": "https://localhost:8080/",
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
        "scope": "email",
        "resource": "https://localhost:8080/"
        # "username": "ioggstream",
        # "password": "test",
    }
    harn_request_token(formdata)
