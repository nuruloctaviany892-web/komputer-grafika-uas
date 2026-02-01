# UAS Grafika Komputer - Transformasi Objek 3D & 2D

Proyek ini dibuat untuk memenuhi tugas Ujian Akhir Semester (UAS) mata kuliah Grafika Komputer. Program ini mengimplementasikan berbagai teknik transformasi geometri pada objek Kubus 3D dan Persegi 2D secara interaktif menggunakan Python.

## Identitas Mahasiswa
* **Nama:** [NURUL OCTAVIANY]
* **NIM:** [23146097]

## Deskripsi Program
Program ini menggunakan library **Pygame** untuk manajemen jendela dan input, serta **PyOpenGL** untuk proses rendering grafis. Dalam satu layar, terdapat dua objek yang dimanipulasi secara independen:
1. **Kubus 3D (Wireframe)**: Menampilkan objek tiga dimensi yang dapat ditransformasi.
2. **Persegi 2D (Solid)**: Menampilkan objek dua dimensi berwarna hijau dengan fitur tambahan shearing dan refleksi.

## Kontrol Keyboard
Sesuai dengan instruksi tugas, berikut adalah pemetaan tombol untuk manipulasi objek:

### 1. Manipulasi Kubus 3D (Sisi Kiri)
| Tombol | Transformasi |
| :--- | :--- |
| **W** | Translasi ke Atas |
| **S** | Translasi ke Bawah |
| **A** | Rotasi Objek |
| **Q** | Memperbesar Skala |

### 2. Manipulasi Persegi 2D (Sisi Kanan)
| Tombol | Transformasi |
| :--- | :--- |
| **Panah Atas** | Translasi ke Atas |
| **Panah Bawah** | Translasi ke Bawah |
| **L** | Rotasi Objek |
| **U** | Mengubah Skala |
| **I** | Shearing (Pemiringan) |
| **O** | Refleksi (Pencerminan) |

## Cara Menjalankan Program
1. Pastikan Python sudah terinstal di komputer Anda.
2. Instal library yang diperlukan dengan perintah:
   ```bash
   pip install pygame PyOpenGL
