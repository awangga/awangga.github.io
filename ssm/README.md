Secara singkat: **Tidak secara harfiah, namun sangat berkaitan erat.**
*Fly-by-wire* (FBW) adalah **arsitektur sistem** (perangkat keras dan perangkat lunak), sedangkan *State Space Model* (Model Ruang Keadaan) adalah **kerangka matematika** yang digunakan di dalam perangkat lunak komputer FBW tersebut untuk mengendalikan pesawat.
Untuk memahami hubungannya, mari kita bedah bagaimana keduanya bekerja sama:
### 1. Peran Komputer dalam *Fly-by-Wire*
Pada pesawat konvensional, tuas kendali yang dipegang pilot terhubung langsung dengan kabel baja ke sayap atau ekor pesawat. Pada sistem *fly-by-wire*, tuas kendali mengirimkan sinyal elektronik ke **Flight Control Computer (FCC)**. Komputer inilah yang memutuskan seberapa jauh sirip pesawat (aktuator) harus bergerak agar pesawat terbang sesuai keinginan pilot, namun tetap aman dan stabil.
### 2. Di Mana *State Space Model* Digunakan?
Agar komputer bisa mengambil keputusan yang tepat dalam sepersekian detik, komputer memerlukan model matematika dari dinamika pesawat tersebut. Di sinilah *State Space Model* masuk.
Pesawat terbang adalah sistem yang sangat kompleks. Pesawat bisa bergerak ke banyak arah (pitch, roll, yaw), dipengaruhi oleh banyak faktor (kecepatan angin, ketinggian, berat), dan digerakkan oleh banyak tuas kendali secara bersamaan. Dalam teori kendali (Control Theory), sistem seperti ini disebut **MIMO (Multiple-Input Multiple-Output)**.
*State Space Model* adalah cara paling efektif untuk merepresentasikan sistem MIMO ini ke dalam bentuk matriks matematika yang bisa dihitung oleh komputer FBW.
### 3. Representasi Matematis Pesawat
Dalam algoritma komputer *fly-by-wire*, dinamika pesawat biasanya dimodelkan menggunakan persamaan *State Space* linier (atau dilinearisasi) berikut:
$$ \dot{x}(t) = A x(t) + B u(t) $$
$$ y(t) = C x(t) + D u(t) $$
Dalam konteks pesawat terbang:
 * **x(t) (State Vector / Variabel Keadaan):** Kondisi pesawat saat ini. Contohnya: kecepatan sudut (*pitch rate, roll rate*), sudut orientasi (*attitude*), ketinggian, dan kecepatan pesawat.
 * **u(t) (Input Vector):** Perintah dari pilot atau sistem auto-pilot, seperti seberapa besar defleksi *elevator*, *aileron*, atau *rudder*.
 * **y(t) (Output Vector):** Data yang terbaca oleh sensor (seperti giroskop dan altimeter) yang diteruskan kembali ke komputer.
 * **Matriks A, B, C, D:** Karakteristik fisik dan aerodinamika dari desain pesawat itu sendiri.
### Mengapa *State Space* Wajib Ada di Pesawat Modern?
Banyak pesawat tempur modern (seperti F-16 atau Eurofighter Typhoon) dirancang agar **secara aerodinamis tidak stabil** untuk membuatnya sangat lincah bermanuver. Manusia tidak akan mampu menerbangkannya secara manual karena pesawat akan langsung lepas kendali.
Komputer *fly-by-wire* menggunakan algoritma yang dirancang dari *State Space Model* (seperti *Linear Quadratic Regulator* atau kendali tangguh/*robust control*) untuk membaca sensor (*states*) ribuan kali per detik, menghitung persamaan matriksnya, dan menggerakkan sirip pesawat secara otomatis untuk menjaga pesawat tetap stabil di udara, bahkan sebelum pilot menyadari adanya perubahan arah angin.



Mohon maaf atas hal tersebut. Berikut adalah perbaikan penulisan persamaan *State Space Model* yang seharusnya tampil:
Sebagai pengingat singkat dari persamaan di atas:
 * x(t) melambangkan *State Vector* (variabel keadaan pesawat saat ini, seperti sudut orientasi dan kecepatan).
 * u(t) melambangkan *Input Vector* (perintah dari pilot, seperti defleksi *elevator* atau *aileron*).
 * y(t) melambangkan *Output Vector* (data yang terbaca oleh sistem sensor).
 * Matriks A, B, C, D mewakili karakteristik fisik dan aerodinamika pesawat itu sendiri.




\dot{x} (dibaca "*x dot*") adalah simbol matematika yang melambangkan **turunan pertama terhadap waktu** atau **laju perubahan**.
Dalam kalkulus dan fisika (khususnya menggunakan notasi Newton), titik di atas sebuah variabel digunakan sebagai jalan pintas untuk menuliskan seberapa cepat variabel tersebut berubah seiring berjalannya waktu, atau yang biasa ditulis sebagai \frac{dx}{dt}.
Untuk memahaminya di dunia nyata, mari kita lihat analoginya pada pesawat:
 * **Jika x adalah Posisi:** Maka \dot{x} adalah **Kecepatan** (seberapa cepat posisinya berubah).
 * **Jika x adalah Kecepatan:** Maka \dot{x} adalah **Percepatan** (seberapa cepat kecepatannya bertambah atau berkurang).
 * **Jika x adalah Sudut Kemiringan (*Pitch/Roll*):** Maka \dot{x} adalah **Kecepatan Sudut** (seberapa cepat moncong pesawat atau sayapnya sedang berputar).
**Maknanya dalam Sistem Pesawat (*Fly-by-Wire*)**
Ketika komputer *fly-by-wire* melihat persamaan \dot{x}(t) = A x(t) + B u(t), komputer tersebut sedang membaca kalimat instruksi yang berbunyi:
> *"Bagaimana kondisi pesawat ini akan berubah di detik berikutnya (\dot{x}) ditentukan oleh gabungan dari kondisi pesawat saat ini (x) dan tarikan tuas/input dari pilot saat ini (u)."*
> 
Dengan mengetahui nilai \dot{x} ribuan kali per detik, komputer bisa memprediksi pergerakan pesawat di masa depan dan melakukan koreksi pada sirip-sirip pesawat sebelum pesawat tersebut kehilangan keseimbangan.
