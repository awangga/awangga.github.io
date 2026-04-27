# Panduan Simulasi Dasar Paper Vaswani

Sebuah aplikasi web interaktif (simulasi) dalam satu file HTML yang menggabungkan CSS (Tailwind) dan JavaScript. Simulasi ini memecah arsitektur Transformer menjadi langkah-langkah visual yang mudah dicerna, mulai dari *Input* hingga *Self-Attention* yang menjadi inti dari makalah tersebut.

### Penjelasan:
1. **Navigasi Langkah-demi-Langkah**: Saya membuat arsitektur Transformer menjadi 6 langkah linier. Pemula tidak akan kewalahan karena informasinya diberikan sedikit demi sedikit.
2. **Visualisasi Abstrak menjadi Konkrit**:
   * **Embedding & Positional Encoding**: Saya menganimasikan bagaimana kata berubah menjadi array, lalu ditambah ikon gelombang matematika untuk mewakili Posisi.
   * **Query, Key, Value**: Dipecah menjadi 3 kotak warna berbeda untuk membantu mengingat fungsinya (merah muda, kuning, hijau).
   * **Self-Attention**: Saya menggunakan ilustrasi SVG garis lengkung (*bezier curve*) di mana ketebalan garis mewakili bobot *Attention*. Di sana, animasi titik bergerak menunjukkan bagaimana informasi dari kata "sungai" mengalir masuk dan memperjelas makna kata "Bank".
3. **Bahasa Sederhana**: Saya menggunakan analogi "Bank sungai" vs "Bank uang" yang sangat intuitif untuk menjelaskan *kenapa* Self-Attention itu penting.
4. **Desain Modern (Satu File)**: Dibangun dengan gaya "Dark Mode" (seperti tampilan terminal/hacker) menggunakan Tailwind CSS dan Vanilla JS agar semuanya ringan dan berjalan seketika di dalam satu file.

Anda bisa mencoba menekan tombol **Preview** untuk langsung mencoba simulasinya! Jika ada bagian tertentu yang ingin diperdalam, beritahu saya.
