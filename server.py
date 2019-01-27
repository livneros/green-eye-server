import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

import Main


# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)

        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body.decode('utf8').replace("'", '"'))
        images_paths = Main.run(post_body["n_clusters"])
        json_string = json.dumps({"images_paths": images_paths})
        self._set_headers()
        self.wfile.write(bytearray(json_string, "utf8"))
        return



def run(port):
    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('0.0.0.0', int(port))
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server on port ', port)
    httpd.serve_forever()


if __name__ == '__main__':
    if sys.argv.__len__() > 1:
        run(sys.argv[1])
    else:
        run(8080)
