import pandas as pd

def tambah_baris_baru(file_path):
    # Membaca file Excel yang sudah ada
    df = pd.read_excel(file_path)

    # Meminta input manual untuk data baru dari pengguna
    jenis = input("Masukkan jenis: ")
    series = input("Masukkan series: ")
    ukuran = input("Masukkan ukuran: ")
    jumlah = input("Masukkan jumlah: ")
    harga = input("Masukkan harga: ")
    merek = input("Masukkan merek: ")

    # Membuat dictionary dengan data baru
    new_data = {
        'jenis': jenis,
        'series': series,
        'ukuran': ukuran,
        'jumlah': jumlah,
        'harga': harga,
        'merek': merek
    }

    # Mengonversi dictionary ke DataFrame
    new_row = pd.DataFrame([new_data])

    # Menambahkan data baru ke DataFrame menggunakan concat
    df = pd.concat([df, new_row], ignore_index=True)

    # Menulis kembali DataFrame ke file Excel
    df.to_excel(file_path, index=False)

    print("Baris baru berhasil ditambahkan ke file Excel.")

# Panggil fungsi dengan path file Excel
file_path = 'database.xlsx'
tambah_baris_baru(file_path)