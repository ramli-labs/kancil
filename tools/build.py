#!/usr/bin/env python3
"""Bangun index.html mandiri (GitHub Pages / PWA) dari versi artifact Claude.

Pakai:  python3 tools/build.py <path-artifact.html>
Hasil:  index.html di akar repo.
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
src = pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")

def sub(old, new, text, count=1):
    if old not in text:
        sys.exit(f"build gagal: potongan tidak ditemukan:\n{old[:120]}")
    return text.replace(old, new, count)

# 1. Buang <title>, meta khusus Claude, dan tautan Google Fonts (font disimpan lokal).
src = re.sub(r'<title>.*?</title>\s*', '', src, count=1, flags=re.S)
src = re.sub(r'<meta name="claude:[^>]*>\s*', '', src)
src = re.sub(r'<link rel="(preconnect|stylesheet)" href="https://fonts\.[^>]*>\s*', '', src)

# 2. Font lokal + reset dasar yang dulu disediakan pembungkus artifact.
FONTS = """@font-face{font-family:"Fredoka";font-weight:500;font-display:swap;src:url(fonts/fredoka-latin-500-normal.woff2) format("woff2")}
@font-face{font-family:"Fredoka";font-weight:600;font-display:swap;src:url(fonts/fredoka-latin-600-normal.woff2) format("woff2")}
@font-face{font-family:"Fredoka";font-weight:700;font-display:swap;src:url(fonts/fredoka-latin-700-normal.woff2) format("woff2")}
@font-face{font-family:"Atkinson Hyperlegible";font-weight:400;font-display:swap;src:url(fonts/atkinson-hyperlegible-latin-400-normal.woff2) format("woff2")}
@font-face{font-family:"Atkinson Hyperlegible";font-weight:700;font-display:swap;src:url(fonts/atkinson-hyperlegible-latin-700-normal.woff2) format("woff2")}
html{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);background:#131936}
*,*::before,*::after{box-sizing:inherit}
body{margin:0}
img{max-width:100%}
[hidden]{display:none!important}
"""
src = sub("<style>\n", "<style>\n" + FONTS, src)

# 3. Nama bawaan dibuat umum (repo publik). Nama anak diisi lewat Pengaturan.
src = sub("name:'Aruna',settings", "name:'Penjelajah',settings", src)
src = sub("||'Aruna';save();}", "||'Penjelajah';save();}", src)

# 4. Ganti sinkron akun Claude dengan penyimpanan perangkat saja.
start = src.index("const cap=name=>")
end = src.index("document.addEventListener('visibilitychange'")
STANDALONE = """const dlP=Promise.resolve(null);
let ready=false;
function setReady(){
  if(ready)return;ready=true;
  const b=$('#startBtn');b.disabled=false;b.textContent='Mulai';
  $('#startHello').textContent='Halo, '+state.name+'!';
}
setReady();
try{if(navigator.storage&&navigator.storage.persist)navigator.storage.persist();}catch(e){}
"""
src = src[:start] + STANDALONE + src[end:]

# 5. Cadangan: unduh file biasa (di iPad masuk ke app Files › Unduhan).
src = sub("$('#exportBox').innerHTML=",
  "try{const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([json],{type:'application/json'}));a.download=fn;document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove();},1500);}catch(err){}\n    $('#exportBox').innerHTML=", src)
src = sub("dmsg('Simpan teks ini di catatan atau email ke diri sendiri.');",
  "dmsg('File cadangan diunduh (cek app Files › Unduhan). Teks di atas bisa disalin sebagai cadangan kedua.');", src)

# 6. Daftarkan service worker untuk mode offline.
src = sub("window.__kancil=", "if('serviceWorker' in navigator){window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));}\nwindow.__kancil=", src)

HEAD = """<!doctype html>
<html lang="id">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>Kancil Menjelajah Angka</title>
<meta name="description" content="Gim belajar matematika untuk anak usia 5–15 tahun dengan peta planet dan prasyarat.">
<meta name="theme-color" content="#131936">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Kancil">
<link rel="manifest" href="manifest.json">
<link rel="icon" href="icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
</head>
<body>
"""
out = HEAD + src.strip() + "\n</body>\n</html>\n"
(ROOT / "index.html").write_text(out, encoding="utf-8")
print("index.html ditulis:", len(out), "byte")
