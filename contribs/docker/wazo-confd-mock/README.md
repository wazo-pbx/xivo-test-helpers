# wazo-confd mock

This is the required files to build a docker image to be used as a wazo-confd mock
for integration tests.

## Usage

This mock exposes an interface similar to the official wazo-confd with a few exceptions.

1. New endpoints have been added to customize the responses:

* `POST /_set_response`
* `GET /_requests`
* `POST /_reset`

## Customisation

Certificates can be customized and placed in the following location:

`server.crt` `/usr/local/share/ssl/confd/server.crt`
`server.key` `/usr/local/share/ssl/confd/server.key`


## How to generate certificates

openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -nodes -config openssl.cfg -days 3650
