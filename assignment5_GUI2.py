import tkinter as tk
from tkinter import messagebox
import sqlite3



# Fungsi untuk menentukan prediksi prodi berdasarkan nilai tertinggi
def predict_prodi(nilai):
    nama_prodi = ["Kedokteran", "Astronomi", "Inggris", "Matematika", "Teknik Nuklir", "Sejarah", "Ekonomi", "Geografi", "Bahasa_Indonesia", "Seni"]
    max_index = nilai.index(max(nilai))
    return nama_prodi[max_index]

# Fungsi untuk tombol submit
def submit_nilai():
    # Ambil nilai dari input pengguna
    nama_siswa = entry_nama.get()
    nilai = [int(entry.get()) for entry in nilai_entries]

    # Prediksi prodi berdasarkan nilai tertinggi
    prediksi_prodi = predict_prodi(nilai)

    # Menampilkan hasil prediksi
    messagebox.showinfo("Hasil Prediksi prodi", f"Prediksi prodi untuk {nama_siswa}: {prediksi_prodi}")





    # Menyimpan data ke SQLite
    conn = sqlite3.connect("predikprodi_GUI2.db")
    cursor = conn.cursor()
    # Membuat tabel jika belum ada
    cursor.execute('''
        Create TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            matematika INTEGER,
            kimia INTEGER,
            sejarah INTEGER,
            ekonomi INTEGER,
            geografi INTEGER,
            bahasa_indonesia INTEGER,
            seni INTEGER,
            prediksi_prodi TEXT
        )
    ''')

    # Menambahkan data ke tabel
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, matematika, kimia, sejarah, ekonomi, geografi, bahasa_indonesia, Seni, prediksi_prodi)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', tuple([nama_siswa] + nilai + [prediksi_prodi]))

    # Commit perubahan dan tutup koneksi
    conn.commit()
    conn.close()

    #Menghapus entry setelah disubmit 
    entry_nama.delete(0, 'end')
    for entry in nilai_entries:
        entry.delete(0, 'end')

    


# Membuat GUI tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("440x670+480+60")

label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Stallman Round", 36))
label_judul.pack()

# Membuat label dan entry untuk input nama siswa
frame_input=tk.Frame(root)
frame_input.pack(pady=7)
label_nama = tk.Label(frame_input, text="Nama Siswa:")
label_nama.pack()
entry_nama = tk.Entry(frame_input)
entry_nama.pack()
frame_input=tk.Frame(root)
frame_input.pack(pady = 2)
label_nama = tk.Label(frame_input, text="Masukan Nilai : ")
label_nama.pack()
# Membuat label dan entry untuk setiap mata pelajaran
nilai_entries = []
mata_pelajaran = ["Biologi", "Fisika", "Inggris", "Matematika", "Kimia", "Sejarah", "Ekonomi", "Geografi", "Bahasa_Indonesia", "Seni"]

for i, mata_pelajaran in enumerate(mata_pelajaran):
    frame_input=tk.Frame(root)
    frame_input.pack(pady=2)
    label = tk.Label(frame_input, text=f"Nilai {mata_pelajaran}:")
    label.pack(padx = 5)
    entry = tk.Entry(frame_input)
    entry.pack(padx =5 )
    nilai_entries.append(entry)
    

# Membuat tombol submit
submit_button = tk.Button(root, text="SUBMIT",font=("Agency FB", 16), command=submit_nilai)
submit_button.pack(pady= 15)

# Menjalankan loop GUI
root.mainloop()
