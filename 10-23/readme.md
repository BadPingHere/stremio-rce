# Arbitrary Origin + Write

The bug was in the metadata of a show, where a link would not properly open the external link popup inside of the browser, allowing the untrusted website to get top-level access. With this, it could escalate to any number of vulnerbilties, with one being the arbitrary write. This write was made possible by mpv-command having excessive control of arguments, allowing javascript to call the function with loadfile, which allowed it to create a file anywhere, with any extension. With the data of it being partially attacker-controlled, it can be made to run commands on run with the right file extension.

---

> GitHub [@BadPingHere](https://github.com/BadPingHere)&nbsp;&middot;&nbsp;
> Discord [BadPingHere](https://discord.com/users/736028271153512489)
