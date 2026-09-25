 # Stremio Vulnerbilities
---

This repo contains all of the vulnerbilities I have found inside of the [Stremio](https://www.stremio.com/) ecosystem.

## 08-28
This release contains a 0-click deeplink RCE, due to players allowing abritrary iframes in the link, and a vulnerbilitiy in play-external + other similiar features to leverage it to RCE.

**Reported**: 07-25  
**Fix made**: [IFrame Fix](https://github.com/Stremio/stremio-video/pull/162) 07-27, [RCE Fix](https://github.com/Stremio/stremio-shell-ng/pull/90) 07-27   
**Release**: [Tech Update #83](https://blog.stremio.com/stremio-tech-update-83-stremio-v5-stremio-web-updated/) 07-27

---

> GitHub [@BadPingHere](https://github.com/BadPingHere)&nbsp;&middot;&nbsp;
> Discord [BadPingHere](https://discord.com/users/736028271153512489)
