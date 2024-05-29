import pandas as pd
import time
import random
from PIL import Image

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Waktu dan tanggal pemesanan
waktu_pemesanan = time.strftime("%d-%m-%Y %H:%M", time.localtime())

# Nomor antrian
nomer_antrian = random.randint(10000, 99999)

# Variabel global untuk menyimpan nama pelanggan, metode pembayaran, dan pesanan
nama_customer = ""
metode_bayar = ""
pesanan = []

def baca_data_dari_excel(file_path):
    try:
        print(f"Membaca data dari file: {file_path}")
        df = pd.read_excel(file_path, sheet_name='Persediaan1')
        df = df.set_index(['jenis', 'merek', 'series', 'ukuran'])
        df = df.sort_index()
        return df
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan.")
        return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])

def tulis_data_ke_excel(df, file_path):
    with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(writer, sheet_name='Persediaan1')

def tambah_sepatu(data_sepatu, file_path, jenis, merek, series, ukuran, jumlah, harga):
    if (jenis, merek, series, ukuran) in data_sepatu.index:
        data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] += jumlah
    else:
        new_row = pd.DataFrame({'jumlah': [jumlah], 'harga': [harga]}, index=pd.MultiIndex.from_tuples([(jenis, merek, series, ukuran)], names=['jenis', 'merek', 'series', 'ukuran']))
        data_sepatu = pd.concat([data_sepatu, new_row])
    data_sepatu = data_sepatu.sort_index()
    tulis_data_ke_excel(data_sepatu, file_path)
    print(f"{jumlah} sepatu {series} ukuran {ukuran} berhasil ditambahkan dengan harga {harga}.")
    return data_sepatu

def kurangi_sepatu(data_sepatu, file_path, jenis, merek, series, ukuran, jumlah):
    if (jenis, merek, series, ukuran) in data_sepatu.index:
        if data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] >= jumlah:
            data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] -= jumlah
            if data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] == 0:
                data_sepatu = data_sepatu.drop((jenis, merek, series, ukuran))
            data_sepatu = data_sepatu.sort_index()
            tulis_data_ke_excel(data_sepatu, file_path)
            print(f"{jumlah} sepatu {series} ukuran {ukuran} berhasil dikurangi.")
        else:
            print(f"Stok tidak mencukupi untuk {series} ukuran {ukuran}.")
    else:
        print(f"Tidak ada stok untuk {series} ukuran {ukuran}.")
    return data_sepatu

def tampilkan_stok(data_sepatu):
    print("Stok sepatu saat ini:")
    print(data_sepatu)

def tampilkan_menu_dari_data(data_sepatu, jenis_menu):
    df_filtered = data_sepatu.xs(jenis_menu, level='jenis', drop_level=False)
    if df_filtered.empty:
        print(f"Tidak ada data untuk jenis sepatu: {jenis_menu}")
        return []
    menu_list = []
    count = 1
    for index, row in df_filtered.iterrows():
        jenis, merek, series, ukuran = index
        print(f"Pilihan {count}:")
        print(f"  Merek: {merek}")
        print(f"  Series: {series}")
        print(f"  Ukuran: {ukuran}")
        print(f"  Harga: {row['harga']}")
        print(f"  Jumlah: {row['jumlah']}")
        print("=========================================")
        menu_list.append((jenis, merek, series, ukuran, row['harga'], row['jumlah']))
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
        print(f"Nama Menu  : {item['series']}")
        print(f"Harga      : {item['harga']}")
        print(f"Kuantitas  : {item['kuantitas']}")
        print(f"Total      : {item['harga'] * item['kuantitas']}")
        print("-----------------------------------------")
    total = hitung_subtotal()
    print(f"Subtotal   : {total}")
    print("=========================================\n")

def pilih_metode():
    global metode_bayar
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
        print(f"            {item['kuantitas']} X    @{item['harga']}       {item['harga'] *   item['kuantitas']}")
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
    print("7. Selesaikan Pembelian dan Cetak Nota")
    print("8. Batalkan Pesanan")
    _choice = int(input("Pilih menu: "))
    return _choice

def kasir_dan_nota(data_sepatu, file_path):
    global metode_bayar
    metode_bayar = pilih_metode()
    if metode_bayar in ["Tunai", "QRIS", "Transfer"]:
        if metode_bayar == "Tunai":
            bayar_tunai()
        elif metode_bayar == "QRIS":
            bayar_qris()
        elif metode_bayar == "Transfer":
            bayar_transfer()

        data_sepatu = kurangi_stok_setelah_pembayaran(data_sepatu, file_path)
        nota_pembelian()
    else:
        print("Metode pembayaran tidak valid")
    return data_sepatu

def kurangi_stok_setelah_pembayaran(data_sepatu, file_path):
    for item in pesanan:
        jenis, merek, series, ukuran = item['jenis'], item['merek'], item['series'], item['ukuran']
        jumlah = item['kuantitas']
        data_sepatu = kurangi_sepatu(data_sepatu, file_path, jenis, merek, series, ukuran, jumlah)
    return data_sepatu

def beli_sepatu(data_sepatu, file_path):
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
    return data_sepatu

def main_program():
    input_customer()
    file_path = "Persediaan1.xlsx"
    data_sepatu = baca_data_dari_excel(file_path)
    while True:
        lihat_menu = pilih_menu()
        if lihat_menu == 1:
            tampilkan_stok(data_sepatu)
        elif lihat_menu == 2:
            jenis = input("Masukkan jenis sepatu: ")
            menu_list = tampilkan_menu_dari_data(data_sepatu, jenis)
            if menu_list:
                choice = int(input("Pilih sepatu yang ingin ditambahkan stoknya (masukkan nomor pilihan): "))
                if 1 <= choice <= len(menu_list):
                    chosen_item = menu_list[choice - 1]
                    jumlah = int(input("Masukkan jumlah sepatu yang ditambahkan: "))
                    data_sepatu = tambah_sepatu(data_sepatu, file_path, *chosen_item[:-2], jumlah, chosen_item[-2])
                else:
                    print("Nomor pilihan tidak valid.")
            else:
                print("Jenis sepatu tidak ditemukan.")
        elif lihat_menu == 3:
            jenis = input("Masukkan jenis sepatu: ")
            merek = input("Masukkan merek sepatu: ")
            series = input("Masukkan series sepatu: ")
            ukuran = int(input("Masukkan ukuran sepatu: "))
            jumlah = int(input("Masukkan jumlah sepatu yang ditambahkan: "))
            harga = float(input("Masukkan harga sepatu: "))
            data_sepatu = tambah_sepatu(data_sepatu, file_path, jenis, merek, series, ukuran, jumlah, harga)
        elif lihat_menu == 4:
            jenis = input("Masukkan jenis sepatu yang akan di trade-in: ")
            merek = input("Masukkan merek sepatu yang akan di trade-in: ")
            series = input("Masukkan series sepatu yang akan di trade-in: ")
            ukuran = int(input("Masukkan ukuran sepatu yang akan di trade-in: "))
            jumlah = int(input("Masukkan jumlah sepatu yang akan di trade-in: "))
            harga_tradein = float(input("Masukkan harga sepatu trade-in: "))
            data_sepatu = kurangi_sepatu(data_sepatu, file_path, jenis, merek, series, ukuran, jumlah)
            jenis_baru = input("Masukkan jenis sepatu baru: ")
            merek_baru = input("Masukkan merek sepatu baru: ")
            series_baru = input("Masukkan series sepatu baru: ")
            ukuran_baru = int(input("Masukkan ukuran sepatu baru: "))
            jumlah_baru = int(input("Masukkan jumlah sepatu baru: "))
            harga_baru = float(input("Masukkan harga sepatu baru: "))
            data_sepatu = tambah_sepatu(data_sepatu, file_path, jenis_baru, merek_baru, series_baru, ukuran_baru, jumlah_baru, harga_baru)
        elif lihat_menu == 5:
            data_sepatu = beli_sepatu(data_sepatu, file_path)
        elif lihat_menu == 6:
            tampilkan_rincian_dan_subtotal()
        elif lihat_menu == 7:
            data_sepatu = kasir_dan_nota(data_sepatu, file_path)
            break
        elif lihat_menu == 8:
            print("Pesanan dibatalkan")
            break
        else:
            print("Menu tidak valid")

if __name__ == "__main__":
    main_program()
