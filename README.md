# Masih Pemula

Konten:
1. Machine Learning [CS229_ML](./CS229_ML)

## Trend Terkini Kecerdasan Buatan
1. Adaptive Learning
2. Federated Learning
3. Self-Supervised Learning

### Adaptive Learning

Sering juga disebut sebagai active learning atau human in the loop machine learning

## Federated Learning

Berhubungan dengan keamanan data, pemberlakukan pembobotan model yang valid dengan sistem insentif

## Self-Supervised Learning

### Utamanya di augmentation/masking policy  

Tepat, tapi khusus untuk metode tertentu (terutama di gambar/visi). Dalam metode SSL seperti Contrastive Learning (misal: SimCLR), augmentasi (seperti cropping, rotasi, ubah warna) adalah jantung utamanya. Tapi di data teks (NLP), SSL biasanya tidak pakai augmentasi seperti itu, melainkan teknik menyembunyikan kata (masking).

### ada ukuran2 statistik

Model belajar menggunakan fungsi matematis dan statistik (seperti Contrastive Loss atau InfoNCE loss) untuk mengukur jarak seberapa "mirip" atau "jauh" representasi data yang dia pelajari.

### Training tanpa data, fine-tune menggunakan sedikit label.

Jika training dengan sedikit data itu namanya Semi-Supervised Learning.
Dalam fase belajar utama SSL (pre-training), TIDAK ADA manual label dari manusia sama sekali (0%).

Yang sering terjadi adalah: Setelah model SSL selesai belajar tanpa label dan menjadi "pintar" mengenali pola, model tersebut kemudian di-fine-tune untuk tugas spesifik menggunakan data yang sedikit ada labelnya. Jadi, proses sedikit label itu terjadi setelah SSL selesai, bukan bagian dari SSL itu sendiri.

### SSL intinya belajar memsupervisi sendiri

Model menyembunyikan atau memanipulasi sebagian dari data tersebut, lalu mencoba memprediksi bagian yang disembunyikan menggunakan bagian yang tersisa. Secara garis besar, ada dua cara paling populer bagaimana SSL melakukan ini:

#### Cara A: Memprediksi Bagian yang Hilang (*Generative / Masking*)
Ini paling sering dipakai di teks (seperti ChatGPT atau BERT) dan belakangan mulai populer di gambar (*Masked Autoencoders*).
* **Logikanya:** Seperti mengisi teka-teki rumpang atau *fill-in-the-blank*.
* **Prosesnya:**
    1. Ambil kalimat asli: "Budi pergi ke *pasar* untuk membeli sayur."
    2. Model menghapus satu kata secara acak: "Budi pergi ke **[MASK]** untuk membeli sayur."
    3. Model ditantang untuk menebak kata yang hilang.
    4. Karena kalimat aslinya sudah ada di *database*, sistem otomatis tahu kunci jawabannya adalah "pasar". Jika tebakan model salah, ia akan mengoreksi dirinya sendiri. **Tidak butuh manusia untuk melabeli kata per kata.**

#### Cara B: Mencocokkan Kesamaan (*Contrastive Learning*)
Ini cara yang memakai "augmentation policy" yang kamu sebutkan tadi, sangat populer untuk data berupa gambar atau suara.
* **Logikanya:** Belajar mengenali bahwa satu objek tetaplah objek yang sama meskipun dilihat dari sudut pandang, warna, atau potongan yang berbeda.
* **Prosesnya:**
    1. Ambil satu foto asli (misalnya foto anjing). Model tidak tahu itu gambar anjing, dia cuma tahu itu "Gambar A".
    2. Sistem membuat **dua versi augmentasi** dari Gambar A: satu di-*zoom* di bagian hidung, satu lagi diubah jadi hitam-putih.
    3. Ambil "Gambar B" secara acak dari database (misalnya foto mobil).
    4. Tugas model adalah **menarik** nilai matematika dari dua versi "Gambar A" agar berdekatan (karena berasal dari sumber yang sama), dan **mendorong** nilainya menjauh dari "Gambar B".
    5. **Kunci jawabannya:** Sistem secara otomatis tahu versi mana yang harus didekatkan karena sistem sendirilah yang membuat versi augmentasi tersebut. Lagi-lagi, tidak butuh label dari manusia.

**Kesimpulan:**
Dengan memecahkan "teka-teki" (menebak kata yang hilang atau mencocokkan gambar yang diaugmentasi) pada jutaan data yang tidak berlabel, model akhirnya mengerti tata bahasa, konteks, garis, warna, dan struktur visual secara mendalam. 
