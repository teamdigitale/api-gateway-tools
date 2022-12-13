# Simple Keycloak JWT-Bearer configuration

This configuration shows how to create a keycloak authentication
with jwt-bearer.

1- create a keypair
2- publish your public key on the web via https
   in jwks format and with an `use` claim
3- configure your keycloak application to authenticate
   via jwt-bearer using the sample configuration
4- request a token signing the request with your
   private key
5- get the token
6- consume the token
