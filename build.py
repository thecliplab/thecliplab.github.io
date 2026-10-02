"""Costruisce index.html della pagina link-in-bio di The Clip Lab da template.html.
Per aggiungere una clip: aggiungi una riga in CLIPS (id YouTube Short, titolo) e rilancia."""
from pathlib import Path

D = Path(__file__).parent
YT = "https://www.youtube.com/@TheClipLabClips"
TT = "https://www.tiktok.com/@thecliplabclips"
IG = "https://www.instagram.com/thecliplabclips"
CLIPS = [  # dalla più recente
    ("PlzwF8RaY6s", "The CIA made him pretend to be gay 😂"),
    ("T9nYZeexhtg", "Ex-CIA spy: they can hear you through your smart TV 😳"),
]
ICO = {
    "ICO_TT": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 5.82A4.28 4.28 0 0 1 15.54 3h-3.09v12.4a2.59 2.59 0 1 1-2.59-2.6c.27 0 .53.04.78.12V9.77a5.76 5.76 0 1 0 4.9 5.7V9.09a7.3 7.3 0 0 0 4.27 1.37V7.4a4.28 4.28 0 0 1-3.21-1.58z"/></svg>',
    "ICO_YT": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1c.4-1.6.5-4.8.5-4.8s0-3.2-.5-4.8zM9.8 15.1V8.9l5.4 3.1-5.4 3.1z"/></svg>',
    "ICO_IG": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
    "ICO_ARROW": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
}
PLAY = '<svg viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg>'

clips = "\n".join(
    f'    <a class="clip" href="https://www.youtube.com/shorts/{vid}" target="_blank" rel="noopener">'
    f'<img src="https://i.ytimg.com/vi/{vid}/oardefault.jpg" onerror="this.src=\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\'" alt="" loading="lazy">'
    f'<span class="shade"></span><span class="play">{PLAY}</span><p>{title}</p></a>'
    for vid, title in CLIPS)

html = (D / "template.html").read_text(encoding="utf-8")
for k, v in {**ICO, "YT": YT, "TT": TT, "IG": IG, "CLIPS": clips}.items():
    html = html.replace("{{" + k + "}}", v)
assert "{{" not in html
(D / "index.html").write_text(html, encoding="utf-8")
print("index.html", len(html), "byte")
