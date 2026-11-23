# Hlsv2-write

This write abuses a vulnerability in subtitles and how they are sent to players, allowing a log file to be placed in an attacker controlled location with semi-attacker controlled bytes. The poc writes a .bat file that opens calc.exe when ran in the windows public folder. This is reachable from a web player link (https://web.stremio.com/#/player/...) or a deeplink (stremio:///player/...).

# Proxy

This abuses the fact that the streaming server has a proxy mechanic, allowing it to render and execute attacker controlled html. This mean an attacker-controlled html file can be rendered and executed on the user's computer. Chained with the new write and previously reported rce, simply visiting a url like 'http://127.0.0.1:11470/proxy/https://evil.com" can lead to RCE and writes. Since visiting a url like that may be a tad suspicious, you can simply have a url 302 redirect to that url, so visiting https://attacker.com is enough to fall victim to this drive-by attack.