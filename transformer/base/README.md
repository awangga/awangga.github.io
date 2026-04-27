# Panduan Simulasi Dasar Paper Vaswani

Sebuah aplikasi web interaktif (simulasi) dalam satu file HTML yang menggabungkan CSS (Tailwind) dan JavaScript. Simulasi ini memecah arsitektur Transformer menjadi langkah-langkah visual yang mudah dicerna, mulai dari *Input* hingga *Self-Attention* yang menjadi inti dari makalah tersebut.

## Contoh penggunakan kata bank

<img width="1440" height="1800" alt="image" src="https://github.com/user-attachments/assets/44468880-a610-4afb-9741-519ef971ac44" />


Pertanyaan yang sangat tajam! Anda baru saja menyentuh **alasan utama mengapa mekanisme *Self-Attention* pada Transformer itu sangat jenius.**

Benar sekali, pemahaman pertama kita tentang kata "Bank" pastilah sebuah gedung tempat kita menyimpan uang. 

Namun, dalam bahasa Inggris, kata ***"Bank"*** memiliki makna ganda (ambigu):
1. **Institusi keuangan** (contoh: *"I went to the bank to get some money"*).
2. **Tepian/bantaran sungai** (contoh: *"I sat on the river bank"*).

**Kenapa contoh ini digunakan dalam simulasi AI?**

Bagi kecerdasan buatan model lama, kata "Bank" direpresentasikan dengan angka yang sama persis, tidak peduli apa konteks kalimatnya. Akibatnya, komputer sering salah menerjemahkan kalimat karena tidak tahu "Bank" mana yang dimaksud.

Di sinilah **Self-Attention** (seperti pada Langkah 4 dan 5 di simulasi) bersinar:
Saat Transformer memproses kalimat *"Bank di sungai itu indah"*, ia tidak membaca kata itu sendirian. Kata "Bank" akan melihat kata-kata di sekitarnya dan menemukan kata **"sungai"**. 

Model tersebut kemudian akan melakukan kalkulasi (*Scaled Dot-Product Attention*) dan menyadari: *"Aha! Karena ada kata sungai dengan bobot kecocokan yang tinggi, maka kata 'Bank' di sini pasti merujuk pada tepi sungai, BUKAN gedung keuangan!"*

*(Catatan: Dalam bahasa Indonesia sehari-hari, kita memang menyebutnya "tepi/bantaran sungai", bukan "bank sungai". Tetapi contoh kata "Bank" sengaja dipertahankan di simulasi ini karena kalimat tersebut adalah contoh paling legendaris yang digunakan oleh para ilmuwan AI di seluruh dunia untuk mendemonstrasikan bagaimana Transformer bisa "memahami" konteks kalimat layaknya manusia manusia!)*

## Penjelasan:
1. **Navigasi Langkah-demi-Langkah**: Saya membuat arsitektur Transformer menjadi 6 langkah linier. Pemula tidak akan kewalahan karena informasinya diberikan sedikit demi sedikit.
2. **Visualisasi Abstrak menjadi Konkrit**:
   * **Embedding & Positional Encoding**: Saya menganimasikan bagaimana kata berubah menjadi array, lalu ditambah ikon gelombang matematika untuk mewakili Posisi.
   * **Query, Key, Value**: Dipecah menjadi 3 kotak warna berbeda untuk membantu mengingat fungsinya (merah muda, kuning, hijau).
   * **Self-Attention**: Saya menggunakan ilustrasi SVG garis lengkung (*bezier curve*) di mana ketebalan garis mewakili bobot *Attention*. Di sana, animasi titik bergerak menunjukkan bagaimana informasi dari kata "sungai" mengalir masuk dan memperjelas makna kata "Bank".
3. **Bahasa Sederhana**: Saya menggunakan analogi "Bank sungai" vs "Bank uang" yang sangat intuitif untuk menjelaskan *kenapa* Self-Attention itu penting.
4. **Desain Modern (Satu File)**: Dibangun dengan gaya "Dark Mode" (seperti tampilan terminal/hacker) menggunakan Tailwind CSS dan Vanilla JS agar semuanya ringan dan berjalan seketika di dalam satu file.

Anda bisa mencoba menekan tombol **Preview** untuk langsung mencoba simulasinya! Jika ada bagian tertentu yang ingin diperdalam, beritahu saya.
