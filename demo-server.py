from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

server_address = ('localhost', 4443)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(
    certfile="pki/issued/demo-api/server-fullchain.cert.pem",
    keyfile="pki/issued/demo-api/server.key.pem"
)

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Server läuft auf https://localhost:4443")
httpd.serve_forever()
