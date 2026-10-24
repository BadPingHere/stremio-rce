# Stremio Vulnerbilities

This repo contains all of the vulnerbilities I have found inside of the [Stremio](https://www.stremio.com/) ecosystem.

## 08-28
This release contains a 1-click deeplink RCE, due to players allowing abritrary iframes in the link, and a vulnerbilitiy in play-external + other similiar features to leverage it to RCE.

**Reported**: RCE & Methods to reach it 07-25
**Fix made**: [IFrame Fix](https://github.com/Stremio/stremio-video/pull/162) 07-27, [RCE Fix](https://github.com/Stremio/stremio-shell-ng/pull/90) 07-27   
**Release**: [Tech Update #83](https://blog.stremio.com/stremio-tech-update-83-stremio-v5-stremio-web-updated/) 07-27

## 10-23
This release contains an arbitrary origin in-frame, allowing attacker-controlled scripts to be ran on the top-level. This was leveraged for arbitrary write. 

**Reported**: Write 07-25, Arbitrary origin 08-13  
**Fix made**: [Write](https://github.com/Stremio/stremio-shell-ng/pull/93) 09-02, [Arbitrary Origin](https://github.com/Stremio/stremio-shell-ng/pull/97/changes/68b65263f8dfcbe32857069343601aa152e0be28) 09-20
**Release**: [Tech Update #85](https://blog.stremio.com/stremio-tech-update-85-stremio-desktop-and-stremio-web-update/) 09-23  

---

> GitHub [@BadPingHere](https://github.com/BadPingHere)&nbsp;&middot;&nbsp;
> Discord [BadPingHere](https://discord.com/users/736028271153512489)
