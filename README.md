# Bike Sharing Data Analysis

## Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda menggunakan *Bike Sharing Dataset* yang mencakup periode tahun 2011–2012. Proyek bertujuan untuk memahami pola permintaan penyewaan sepeda berdasarkan waktu, musim, dan kondisi cuaca melalui proses *data wrangling*, *exploratory data analysis* (EDA), visualisasi data, serta penyusunan rekomendasi berdasarkan hasil analisis.

Selain analisis melalui notebook, proyek ini dilengkapi dengan dashboard interaktif berbasis Streamlit untuk memudahkan pengguna mengeksplorasi data dan memahami pola penyewaan sepeda.

## Tujuan Analisis

Analisis ini berfokus pada dua pertanyaan utama:

1. Bagaimana perubahan rata-rata penyewaan sepeda harian berdasarkan bulan dan musim selama tahun 2011–2012?
2. Bagaimana perbedaan rata-rata penyewaan sepeda harian berdasarkan kondisi cuaca selama periode tersebut?

Hasil analisis diharapkan dapat memberikan gambaran mengenai periode dengan permintaan tinggi maupun rendah serta membantu merumuskan rekomendasi untuk pengelolaan layanan penyewaan sepeda.

## Dataset

Dataset yang digunakan adalah `day.csv`, yang berisi catatan penyewaan sepeda harian dengan total awal 731 baris dan 16 kolom.

Beberapa variabel yang digunakan dalam analisis meliputi:

| Variabel | Deskripsi |
| --- | --- |
| `dteday` | Tanggal pengamatan |
| `season` | Kategori musim |
| `mnth` | Bulan pengamatan |
| `weathersit` | Kategori kondisi cuaca |
| `temp` | Suhu dalam skala ternormalisasi |
| `hum` | Kelembapan dalam skala ternormalisasi |
| `windspeed` | Kecepatan angin dalam skala ternormalisasi |
| `casual` | Jumlah penyewaan oleh pengguna kasual |
| `registered` | Jumlah penyewaan oleh pengguna terdaftar |
| `cnt` | Total penyewaan sepeda harian |

## Struktur Proyek

```text
BikeSharingSubmission/
├── data/
│   └── day.csv
├── app.py
├── notebook.ipynb
├── requirements.txt
└── README.md
```

Keterangan:

- `data/day.csv`: dataset yang digunakan untuk analisis.
- `app.py`: kode sumber dashboard interaktif Streamlit.
- `notebook.ipynb`: notebook yang berisi proses analisis data, mulai dari pemeriksaan dan pembersihan data hingga visualisasi serta kesimpulan.
- `requirements.txt`: daftar pustaka Python yang dibutuhkan untuk menjalankan proyek.
- `README.md`: dokumentasi proyek.

## Tahapan Analisis

### 1. Data Wrangling

Memuat dataset, memeriksa struktur dan kualitas data, serta menangani masalah data yang ditemukan berdasarkan hasil pemeriksaan.

### 2. Exploratory Data Analysis (EDA)

Mengeksplorasi distribusi penyewaan sepeda dan membandingkan rata-rata penyewaan berdasarkan bulan, musim, serta kondisi cuaca.

### 3. Visualization and Explanatory Analysis

Menyajikan hasil eksplorasi melalui visualisasi yang membantu memperlihatkan tren penyewaan dan perbedaan permintaan antarkategori.

### 4. Conclusion and Recommendation

Merangkum temuan utama dan menyusun rekomendasi yang dapat dipertimbangkan dalam pengelolaan ketersediaan sepeda dan perencanaan operasional.

## Temuan Utama

Berdasarkan hasil analisis pada dataset:

- **Berdasarkan tahun:** rata-rata penyewaan harian meningkat dari 3.405,76 pada tahun 2011 menjadi 5.599,93 pada tahun 2012, atau sekitar 64,43%.
- **Berdasarkan bulan:** rata-rata penyewaan harian tertinggi terjadi pada bulan Juni, sebesar 5.772,37, sedangkan rata-rata terendah terjadi pada bulan Januari, sebesar 2.176,34.
- **Berdasarkan musim:** Summer memiliki rata-rata penyewaan harian tertinggi sebesar 5.644,30, sedangkan Winter memiliki rata-rata terendah sebesar 2.604,13.
- **Berdasarkan cuaca:** kategori Clear / Few Clouds memiliki rata-rata penyewaan harian tertinggi sebesar 4.876,79, sedangkan Light Rain / Snow memiliki rata-rata terendah sebesar 1.803,29.

Temuan tersebut menunjukkan bahwa jumlah penyewaan bervariasi berdasarkan waktu, musim, dan kondisi cuaca. Namun, hasil perbandingan ini menunjukkan hubungan dalam data dan tidak membuktikan bahwa satu faktor tertentu menjadi satu-satunya penyebab perubahan permintaan.

## Rekomendasi

1. **Perencanaan ketersediaan sepeda:** menyiapkan ketersediaan sepeda dan kapasitas operasional yang memadai pada periode dengan rata-rata penyewaan tinggi.
2. **Antisipasi perubahan musiman:** menggunakan pola permintaan bulanan dan musiman sebagai salah satu dasar perencanaan operasional.
3. **Pertimbangan kondisi cuaca:** mempertimbangkan kondisi cuaca dalam perencanaan ketersediaan sepeda dan penyampaian informasi layanan kepada pengguna.
4. **Evaluasi secara berkala:** memperbarui analisis menggunakan data terbaru agar rekomendasi tetap relevan dengan pola penggunaan saat ini.

Rekomendasi tersebut merupakan usulan berdasarkan pola yang ditemukan dalam dataset, sehingga penerapannya sebaiknya disesuaikan dengan kondisi operasional dan data yang lebih terkini.

## Menjalankan Dashboard

Dashboard dikembangkan menggunakan Python dan Streamlit.

### Prasyarat

- Python telah terinstal.
- Seluruh file proyek tersedia di dalam folder `BikeSharingSubmission`.
- Koneksi internet tersedia saat menginstal pustaka yang diperlukan.

### Langkah Menjalankan

1. Buka folder proyek melalui Visual Studio Code.
2. Buka terminal melalui menu **Terminal → New Terminal**.
3. Pastikan terminal berada di folder `BikeSharingSubmission`.
4. Aktifkan virtual environment jika belum aktif:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instal pustaka yang dibutuhkan:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Jalankan dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

7. Buka alamat lokal berikut di browser jika tidak terbuka otomatis:

   `http://localhost:8501`

Jika virtual environment sudah aktif, perintah aktivasi tidak perlu dijalankan kembali. Pastikan file `data/day.csv` tersedia karena dashboard menggunakan dataset tersebut.

## Teknologi yang Digunakan

- **Python** — bahasa pemrograman untuk analisis data.
- **Pandas** — pemrosesan dan manipulasi data.
- **Matplotlib dan Seaborn** — pembuatan visualisasi data di notebook.
- **Plotly Express** — pembuatan visualisasi interaktif pada dashboard.
- **Streamlit** — pengembangan dashboard interaktif.

## Batasan Analisis

Analisis ini menggunakan data historis tahun 2011–2012. Oleh karena itu, pola yang ditemukan belum tentu menggambarkan kondisi penyewaan sepeda saat ini. Analisis juga berfokus pada perbandingan deskriptif sehingga tidak dapat digunakan untuk menyimpulkan hubungan sebab-akibat secara langsung.

## Penutup

Proyek ini menunjukkan bagaimana analisis data dan visualisasi dapat digunakan untuk memahami pola penyewaan sepeda. Hasilnya dapat menjadi dasar awal untuk mendukung pengambilan keputusan terkait perencanaan ketersediaan sepeda, dengan tetap mempertimbangkan keterbatasan dataset dan kebutuhan evaluasi menggunakan data terbaru.
