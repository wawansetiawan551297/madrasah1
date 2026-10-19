# Absensi RFID MI Miftahul Athfal | Gondosuli

## Cara menjalankan di Windows
1. Ekstrak seluruh file ZIP ke satu folder.
2. Pastikan Python 3 sudah terpasang. Saat instalasi Python, centang "Add Python to PATH".
3. Klik dua kali `run.bat`. Komputer perlu internet saat pertama kali memasang Flask.
4. Tunggu sampai muncul alamat `http://127.0.0.1:5000`.
5. Buka Chrome dan kunjungi `http://127.0.0.1:5000` (jangan buka `index.html` langsung).
6. Login aplikasi: username `admin`, password `admin123`.
7. Tambahkan data guru/siswa dan kode kartu RFID pada menu masing-masing. Saat data disimpan, aplikasi akan menyinkronkan keadaan aplikasi ke SQLite.

## File penting
- `index.html`: antarmuka absensi.
- `app.py`: backend Flask dan API penyimpanan.
- `database_absensi_mi_miftahul_athfal.db`: database SQLite.
- `requirements.txt`: dependensi Python.
- `run.bat`: menjalankan aplikasi pada Windows.

## Catatan
- Ini paket awal untuk penggunaan lokal pada satu komputer. Data aplikasi disimpan sebagai JSON di tabel `app_state` pada SQLite agar seluruh fitur HTML lama bisa digunakan tanpa menulis ulang semua layar.
- Tabel relasional `teachers`, `students`, `attendance`, dan lainnya pada database disiapkan untuk pengembangan lanjutan, tetapi layar HTML saat ini belum menulis ke tabel-tabel relasional tersebut.
- Backend ini tidak memiliki autentikasi server yang kuat dan belum ditujukan untuk dibuka ke internet atau digunakan bersama-sama dari banyak komputer. Untuk penggunaan produksi, perlu login backend, kontrol akses, backup, dan pengujian.
- Pembaca RFID USB yang mengetik UID seperti keyboard dapat digunakan. Perangkat RFID yang memakai serial/driver khusus memerlukan integrasi tambahan.
- Jangan hapus file `.db` saat aplikasi berjalan. Tutup server dengan Ctrl+C sebelum memindahkan atau mencadangkan database.
