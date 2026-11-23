# Run via python serve.py

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from runpy import run_path
from ssl import PROTOCOL_TLS_SERVER, SSLContext
from tempfile import TemporaryDirectory
from threading import Thread
from urllib.parse import quote, urlsplit

PORT = 8067
TLS_PORT = 8068
PAGE = Path(__file__).with_name("poc.html").read_bytes()
ASSETS = Path(__file__).resolve().parent.parent / "hlsv2-write"
MEDIA = {
    "/base.mp4": ((ASSETS / "base.mp4").read_bytes(), "video/mp4"),
    "/base.srt": ((ASSETS / "base.srt").read_bytes(), "application/x-subrip"),
}

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.serve(True)

    def do_HEAD(self):
        self.serve(False)

    def serve(self, send_body):
        path = urlsplit(self.path).path
        if path == "/":
            host = self.headers.get("Host", "")
            if not host:
                self.send_error(400)
                return
            upstream = (f"https://127.0.0.1:{TLS_PORT}" if host.startswith(("127.0.0.1:", "localhost:"))
                        else f"https://{host}")
            target = ("http://127.0.0.1:11470/proxy/" + quote("d=" + upstream, safe="") + "/poc.html")
            self.send_response(302)
            self.send_header("Location", target)
            self.send_header("Cache-Control", "no-store")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if path == "/poc.html":
            body, mime = PAGE, "text/html; charset=utf-8"
        elif path in MEDIA:
            body, mime = MEDIA[path]
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if send_body:
            self.wfile.write(body)

if __name__ == "__main__":
    with TemporaryDirectory() as temp:
        tls_server = ThreadingHTTPServer(("127.0.0.1", TLS_PORT), Handler)
        context = SSLContext(PROTOCOL_TLS_SERVER)
        tls_server.socket = context.wrap_socket(tls_server.socket, server_side=True)
        landing_server = ThreadingHTTPServer(("127.0.0.1", PORT), Handler)
        Thread(target=tls_server.serve_forever, daemon=True).start()
        print(f"Serving on http://127.0.0.1:{PORT}/. To test that a non-local url can redirect to this, use a cloudflare tunnel with this command")
        print("cloudflared tunnel --url http://127.0.0.1:8067")
        try:
            landing_server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            landing_server.server_close()
            tls_server.shutdown()
            tls_server.server_close()
