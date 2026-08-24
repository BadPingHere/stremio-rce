# Proof of Concept for Stremio RCE

This repository is a proof-of-concept for Remote Code Exection in Stremio Shell Newgen, fixed in [pull request #90](https://github.com/Stremio/stremio-shell-ng/pull/90). It uses Cross-Site Scripting to escalate to RCE.

Url-creator.js - This script will generate a stremio:// deeplink that will link directly to a custom Video Player. Once opened, it will execute its payload. There are 4 options, using 3 bugs. 'External' uses the fact that open-external does not properly validate the urls given, allowing for simple code execution. Option 'vlc' and 'potplayer' work the same, however are in play-external, rather than open-external. 'unc' uses a untested window.open payload to download and run a file from a webdav server.

If you are a user, I reccomemend making sure you are on shell verison 5.0.24 or above, available to check via the settings menu in Stremio.

---

> GitHub [@BadPingHere](https://github.com/BadPingHere)&nbsp;&middot;&nbsp;
> Discord [BadPingHere](https://discord.com/users/736028271153512489)
