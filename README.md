# Kancil Menjelajah Angka

Gim belajar matematika berbasis web untuk anak usia 5–15 tahun, dirancang untuk iPad. Peta pembelajarannya berbentuk planet dari TK B sampai SMP (ranah OSN Matematika). Planet berikutnya baru terbuka kalau prasyaratnya sudah dikuasai.

Dibuat oleh Ramli Jainal Muttaqin, S.Pd. (ramli-labs).

## Isi saat ini

| Usia | Planet | Status |
|---|---|---|
| 5–6 (TK B) | Planet Wortel: pecah bilangan sampai 10 | Bisa dimainkan |
| 5–6 (TK B) | Planet Sepuluh: pasangan 10, tambah-kurang sampai 20 | Bisa dimainkan (prasyarat: Wortel) |
| 5–6 (TK B) | Planet Roket: papan 100, hitung loncat, nilai tempat | Bisa dimainkan |
| 6–15 | Planet 4–19 (Puluhan sampai Bukti) | Ada di peta, isi menyusul |

## Aturan naik level

- Tiap planet punya 3 tingkat: Dibantu, Sedikit bantuan, Mandiri.
- Satu tingkat dikuasai kalau minimal 8 dari 10 jawaban terakhir benar pada percobaan pertama, tersebar di minimal 2 misi.
- Planet dikuasai saat tingkat Mandiri dikuasai. Planet lain terbuka hanya kalau semua prasyaratnya dikuasai.
- 3 kali salah beruntun membuat soal turun satu tingkat. Kalau sudah di tingkat 1, anak diarahkan ke planet prasyarat.
- Tantangan bintang terbuka setelah sebuah planet dikuasai.

## Memasang di iPad

1. Buka alamat GitHub Pages repo ini di **Safari**.
2. Ketuk tombol **Bagikan** (kotak dengan panah ke atas), lalu pilih **Tambah ke Layar Utama**.
3. Buka gim dari ikon Kancil di Layar Utama. Gim tampil layar penuh dan tetap bisa dibuka tanpa internet.

Instruksi suara memakai suara bawaan iPad. Kalau suaranya belum berbahasa Indonesia, buka **Pengaturan › Aksesibilitas › Konten Lisan › Suara › Bahasa Indonesia**, lalu unduh salah satu suara.

## Data kemajuan

Kemajuan hanya tersimpan di perangkat yang dipakai, tidak dikirim ke server mana pun. Untuk membuat cadangan, buka **Orang tua › Data kemajuan › Simpan cadangan**. File cadangan masuk ke app Files › Unduhan. Untuk mengembalikannya, pilih **Pulihkan dari file**.

## Struktur repo

```
index.html      gim lengkap (satu file)
manifest.json   data aplikasi untuk Layar Utama
sw.js           service worker untuk mode offline
icons/          ikon aplikasi
fonts/          Fredoka & Atkinson Hyperlegible (SIL Open Font License)
tools/build.py  membangun index.html dari versi pengembangan
```

Setiap kali `index.html` diperbarui, naikkan `VERSION` di `sw.js` (misalnya `kancil-v2`) supaya iPad mengambil versi baru.
