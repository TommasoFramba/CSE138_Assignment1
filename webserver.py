####################
# Course: CSE138
# Date: Fall 2021
# Assignment: 1
# Tommaso Framba
# This program implements a simple HTTP interface with specified
# responses to GET and POST requests.
###################

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
import os.path

#handle requests
class helloHandler(BaseHTTPRequestHandler):

    #handle get requests
    def do_GET(self):
        parsed_path = urlparse(self.path).path.split("/")
        if len(parsed_path) == 2:
            if parsed_path[1] == 'hello':
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(r"""{"message":"world"}""""".encode("utf8"))
            elif parsed_path[1] == 'test':
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(r"""{"message":"test is successful"}""""".encode("utf8"))
        elif len(parsed_path) == 3:
            if parsed_path[1] == 'hello':
                self.send_response(405)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write('Method not allowed'.encode("utf8"))

    #handle post requests
    def do_POST(self):
        parsed_path = urlparse(self.path).path.split("/")
        if len(parsed_path) == 2:
            if parsed_path[1] == 'hello':
                self.send_response(405)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write('Method not allowed'.encode("utf8"))
            elif parsed_path[1] == 'test':
                queryPath = urlparse(self.path).query
                if len(queryPath) != 0:
                    if len(queryPath) > 4 and queryPath[0:4] == 'msg=':
                        self.send_response(200)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write((r"""{"message":"%s"}""""" % queryPath[4:]).encode("utf8"))
                    else:
                        self.send_response(400)
                        self.send_header("Content-type", "text/html")
                        self.end_headers()
                        self.wfile.write('Bad Request Unknown Query'.encode("utf8"))
                else:
                    self.send_response(400)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    self.wfile.write('Bad Request'.encode("utf8"))
        elif len(parsed_path) == 3:
            if parsed_path[1] == 'hello':
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write((r"""{"message":"Hi, %s."}"""""%parsed_path[2]).encode("utf8"))

#start and run server on port 8090
def main():
    PORT = 8090
    server = HTTPServer(('', PORT), helloHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()
