import pandas as pd
import time
import random
from PIL import Image
import openpyxl

# Waktu dan tanggal pemesanan
waktu_pemesanan = time.strftime("%d-%m-%Y %H:%M", time.localtime())

# Nomor antrian
nomer_antrian = random.randint(10000, 99999)

# Variabel global untuk menyimpan nama pelanggan, metode pembayaran, dan pesanan
nama_customer = ""
metode_bayar = ""
pesanan = []
file_path = "Persediaan1.xlsx"

def baca_data_dari_excel(file_path):
    try:
        print(f"Membaca data dari file: {file_path}")
        df = pd.read_excel(file_path, sheet_name='Persediaan1')
        df = pd.DataFrame(df)
        df = df.sort_index()
        return df
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])

def tulis_data_ke_excel(file_path, data_sepatu):
    with pd.ExcelWriter(file_path, mode="a", engine='openpyxl', if_sheet_exists='replace') as writer:
        data_sepatu.to_excel(writer, sheet_name='Persediaan1', index=False)

def tambah_sepatu(file_path, data_sepatu, jenis, merek, series, ukuran, jumlah, harga):
    existing_row = data_sepatu[
        (data_sepatu['jenis'] == jenis) &
        (data_sepatu['merek'] == merek) &
        (data_sepatu['series'] == series) &
        (data_sepatu['ukuran'] == ukuran)
    ]

    if not existing_row.empty:
        idx = existing_row.index[0]
        data_sepatu.at[idx, 'jumlah'] += jumlah
        data_sepatu.at[idx, 'harga'] = harga
    else:
        new_row = pd.DataFrame({'jenis': [jenis], 'merek': [merek], 'series': [series], 'ukuran': [ukuran], 'jumlah': [jumlah], 'harga': [harga]}, index=[0])
        data_sepatu = pd.concat([data_sepatu, new_row], ignore_index=True)
    
    data_sepatu = data_sepatu.sort_values(by=['jenis', 'merek', 'series', 'ukuran'])
    tulis_data_ke_excel(file_path, data_sepatu)
    print(f"{jumlah} sepatu {series} ukuran {ukuran} berhasil ditambahkan dengan harga {harga}.")

def kurangi_sepatu(file_path, data_sepatu, jenis, merek, series, ukuran, jumlah):
    existing_row = data_sepatu[
        (data_sepatu['jenis'] == jenis) &
        (data_sepatu['merek'] == merek) &
        (data_sepatu['series'] == series) &
        (data_sepatu['ukuran'] == ukuran)
    ]

    if not existing_row.empty:
        idx = existing_row.index[0]
        if data_sepatu.at[idx, 'jumlah'] >= jumlah:
            data_sepatu.at[idx, 'jumlah'] -= jumlah
            tulis_data_ke_excel(file_path, data_sepatu)
            print(f"{jumlah} sepatu {series} ukuran {ukuran} berhasil dikurangi.")
        else:
            print(f"Stok tidak mencukupi untuk {series} ukuran {ukuran}.")
    else:
        print(f"Sepatu {series} ukuran {ukuran} tidak ditemukan.")

def tampilkan_stok(data_sepatu):
    print("Stok sepatu saat ini:")
    print(data_sepatu)

def tampilkan_menu_dari_data(data_sepatu, jenis_menu):
    df_filtered = data_sepatu[data_sepatu['jenis'] == jenis_menu]
    menu_list = []
    count = 1
    for index, row in df_filtered.iterrows():
        jenis = row['jenis']
        merek = row['merek']
        series = row['series']
        ukuran = row['ukuran']
        harga = row['harga']
        jumlah = row['jumlah']
        print(f"Pilihan {count}:")
        print(f"  Merek: {merek}")
        print(f"  Series: {series}")
        print(f"  Ukuran: {ukuran}")
        print(f"  Harga: {harga}")
        print(f"  Jumlah: {jumlah}")
        print("=========================================")
        menu_list.append((jenis, merek, series, ukuran, harga, jumlah))
        count += 1
    return menu_list

def input_customer():
    global nama_customer
    nama_customer = input("Masukkan Nama Anda: ")

def hitung_subtotal():
    total = 0
    for item in pesanan:
        total += item['harga'] * item['kuantitas']
    return total

def tampilkan_rincian_dan_subtotal():
    print("\nRincian Pesanan Anda:")
    print("=========================================")
    for item in pesanan:
        print(f"Nama Menu  : {item['merek']} {item['series']}")
        print(f"Harga      : {item['harga']}")
        print(f"Kuantitas  : {item['kuantitas']}")
        print(f"Total      : {item['harga'] * item['kuantitas']}")
        print("-----------------------------------------")
    total = hitung_subtotal()
    print(f"Subtotal   : {total}")
    print("=========================================\n")

def pilih_metode():
    print("========Pilih Metode Pembayaran=========")
    print("1. Tunai\n2. Qris\n3. Transfer")
    metode_bayar = int(input("Pilih metode pembayaran: "))
    if metode_bayar == 1:
        return "Tunai"
    elif metode_bayar == 2:
        return "QRIS"
    elif metode_bayar == 3:
        return "Transfer"
    else:
        return "Tidak valid"

def bayar_tunai():
    total = hitung_subtotal()
    print("Silahkan ambil nota dan siapkan uang sebesar Rp", total, " lalu transaksi di kasir")

def bayar_qris():
    total = hitung_subtotal()
    print("Silahkan bayar sebesar Rp", total)
    qris = Image.open("qris.jpg")
    qris.show()

def bayar_transfer():
    total = hitung_subtotal()
    print("1. Bank Mandiri\n2. Bank Rakyat Indonesia\n3. Bank Negara Indonesia\n4. Bank BCA\n5. Bank CIMB Niaga")
    rekening_tujuan = int(input("Pilih jenis bank: "))
    if rekening_tujuan == 1:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 104976349648 a.n. Fadia Dian Ambarrizka")
    elif rekening_tujuan == 2:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 6632 0102 3871 530 a.n. Ferrel Rafi Elian")
    elif rekening_tujuan == 3:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 1786806019 a.n. Atha Nabilah Aurellia")
    elif rekening_tujuan == 4:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 7240491014 a.n. Diaz Mondrian")
    elif rekening_tujuan == 5:
        print("Bayar pesanan anda sebesar Rp", total, "ke rekening tujuan 707638220000 a.n. Alifianatha Reyhan")
    else:
        print("Maaf, kode tidak valid")

def rincian_nota():
    for item in pesanan:
        print(f"{item['series']}")
        print(f"            {item['kuantitas']} X    @{item['harga']}       {item['harga'] * item['kuantitas']}")
        print("------------------------------------")
    total = hitung_subtotal()
    print(f"                 Subtotal   : {total}")
    print("====================================\n")

def nota_pembelian():
    print("              EINS FOOTWEAR              ")
    print("         Kota, Provinsi, Indonesia       ")
    print("             Nomor Antrian               ")
    print(f"                {nomer_antrian}         ")
    print("=========================================")
    print(f"Nama Customer    : {nama_customer}")
    print(f"Waktu Pemesanan  : {waktu_pemesanan}")
    print(f"Metode Pembayaran: {metode_bayar}")
    print("=========================================")
    rincian_nota()

def pilih_menu():
    print("============SELAMAT DATANG DI EINS FOOTWEAR============")
    print("1. Lihat Stok Sepatu")
    print("2. Tambah Stok Sepatu")
    print("3. Tambah Sepatu Baru")
    print("4. Trade-in Sepatu")
    print("5. Beli Sepatu")
    print("6. Tampilkan Pesanan dan Subtotal")
    print("7. Selesaikan dan Bayar")
    print("8. Batal")
    print("====================================================")
    menu_choice = int(input("Pilih menu: "))
    return menu_choice

def lihat_stok(data_sepatu):
    tampilkan_stok(data_sepatu)

def tambah_stok_sepatu(data_sepatu):
    jenis = input("Masukkan jenis sepatu: ")
    menu_list = tampilkan_menu_dari_data(data_sepatu, jenis)
    if menu_list:
        choice = int(input("Pilih sepatu yang ingin ditambahkan stoknya (masukkan nomor pilihan): "))
        if 1 <= choice <= len(menu_list):
            chosen_item = menu_list[choice - 1]
            jumlah = int(input("Masukkan jumlah sepatu yang ditambahkan: "))
            tambah_sepatu(file_path, data_sepatu, chosen_item[0], chosen_item[1], chosen_item[2], chosen_item[3], jumlah, chosen_item[4])
        else:
            print("Nomor pilihan tidak valid.")
    else:
        print("Jenis sepatu tidak ditemukan.")

def tambah_sepatu_baru(data_sepatu):
    jenis = input("Masukkan jenis sepatu: ")
    merek = input("Masukkan merek sepatu: ")
    series = input("Masukkan series sepatu: ")
    ukuran = int(input("Masukkan ukuran sepatu: "))
    jumlah = int(input("Masukkan jumlah sepatu yang ditambahkan: "))
    harga = float(input("Masukkan harga sepatu: "))
    tambah_sepatu(file_path, data_sepatu, jenis, merek, series, ukuran, jumlah, harga)

def trade_in_sepatu(data_sepatu):
    jenis = input("Masukkan jenis sepatu yang akan di trade-in: ")
    merek = input("Masukkan merek sepatu yang akan di trade-in: ")
    series = input("Masukkan series sepatu yang akan di trade-in: ")
    ukuran = int(input("Masukkan ukuran sepatu yang akan di trade-in: "))
    jumlah = int(input("Masukkan jumlah sepatu yang akan di trade-in: "))
    harga_tradein = float(input("Masukkan harga sepatu trade-in: "))
    kurangi_sepatu(file_path, data_sepatu, jenis, merek, series, ukuran, jumlah)
    jenis_baru = input("Masukkan jenis sepatu baru: ")
    merek_baru = input("Masukkan merek sepatu baru: ")
    series_baru = input("Masukkan series sepatu baru: ")
    ukuran_baru = int(input("Masukkan ukuran sepatu baru: "))
    jumlah_baru = int(input("Masukkan jumlah sepatu baru: "))
    harga_baru = float(input("Masukkan harga sepatu baru: "))
    tambah_sepatu(file_path, data_sepatu, jenis_baru, merek_baru, series_baru, ukuran_baru, jumlah_baru, harga_baru)

def beli_sepatu(data_sepatu):
    jenis = input("Masukkan jenis sepatu: ")
    menu_list = tampilkan_menu_dari_data(data_sepatu, jenis)
    if menu_list:
        choice = int(input("Pilih sepatu yang ingin dibeli (masukkan nomor pilihan): "))
        if 1 <= choice <= len(menu_list):
            chosen_item = menu_list[choice - 1]
            while True:
                try:
                    quantity = int(input("Masukkan kuantitas: "))
                    if quantity > 0:
                        break
                    else:
                        print("Kuantitas harus lebih dari 0. Silakan coba lagi.")
                except ValueError:
                    print("Masukkan angka yang valid untuk kuantitas.")
            
            print("\nAnda memilih :")
            print(f"Nama Menu  : {chosen_item[2]}")
            print(f"Harga      : {chosen_item[4]}")
            print(f"Kuantitas  : {quantity}\n")
            
            pesanan.append({
                'jenis': jenis,
                'merek': chosen_item[1],
                'series': chosen_item[2],
                'ukuran': chosen_item[3],
                'harga': chosen_item[4],
                'kuantitas': quantity
            })
        else:
            print("Nomor pilihan tidak valid.")
    else:
        print("Jenis sepatu tidak ditemukan.")

def tampilkan_pesanan_dan_subtotal():
    tampilkan_rincian_dan_subtotal()

def selesaikan_dan_bayar(data_sepatu):
    global metode_bayar
    metode_bayar = pilih_metode()
    if metode_bayar in ["Tunai", "QRIS", "Transfer"]:
        if metode_bayar == "Tunai":
            bayar_tunai()
        elif metode_bayar == "QRIS":
            bayar_qris()
        elif metode_bayar == "Transfer":
            bayar_transfer()

        kurangi_stok_setelah_pembayaran(file_path, data_sepatu)
        nota_pembelian()
        return True
    else:
        print("Metode pembayaran tidak valid")
        return False

def batal():
    print("Pesanan dibatalkan")

def main_program():
    global metode_bayar
    input_customer()
    data_sepatu = baca_data_dari_excel(file_path)
    while True:
        lihat_menu = pilih_menu()
        if lihat_menu == 1:
            lihat_stok(data_sepatu)
        elif lihat_menu == 2:
            tambah_stok_sepatu(data_sepatu)
        elif lihat_menu == 3:
            tambah_sepatu_baru(data_sepatu)
        elif lihat_menu == 4:
            trade_in_sepatu(data_sepatu)
        elif lihat_menu == 5:
            beli_sepatu(data_sepatu)
        elif lihat_menu == 6:
            tampilkan_pesanan_dan_subtotal()
        elif lihat_menu == 7:
            if selesaikan_dan_bayar(data_sepatu):
                break
        elif lihat_menu == 8:
            batal()
            break
        else:
            print("Menu tidak valid")

def kurangi_stok_setelah_pembayaran(file_path, data_sepatu):
    for item in pesanan:
        jenis, merek, series, ukuran = item['jenis'], item['merek'], item['series'], item['ukuran']
        jumlah = item['kuantitas']
        kurangi_sepatu(file_path, data_sepatu, jenis, merek, series, ukuran, jumlah)

if __name__ == "__main__":
    main_program()

