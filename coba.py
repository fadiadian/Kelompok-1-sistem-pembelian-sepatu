import pandas as pd
import time
import random
from PIL import Image

# Global variables
waktu_pemesanan = time.strftime("%d-%m-%Y %H:%M", time.localtime())
nomer_antrian = random.randint(10000, 99999)
nama_customer = ""
metode_bayar = ""
pesanan = []

class GudangSepatu:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_sepatu = self._baca_data_dari_excel()

    def _baca_data_dari_excel(self):
        try:
            df = pd.read_excel(self.file_path, sheet_name='Persediaan1')
            df = df.set_index(['jenis', 'merek', 'series', 'ukuran'])
            df = df.sort_index()
            return df
        except FileNotFoundError:
            return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])
        except Exception as e:
            print(f"Error: {e}")
            return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])

    def _tulis_data_ke_excel(self):
        with pd.ExcelWriter(self.file_path, mode='a', if_sheet_exists='replace') as writer:
            self.data_sepatu.to_excel(writer, sheet_name='Persediaan1')

    def tambah_sepatu(self, jenis, merek, series, ukuran, jumlah, harga):
        if (jenis, merek, series, ukuran) in self.data_sepatu.index:
            self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] += jumlah
        else:
            new_row = pd.DataFrame({'jumlah': [jumlah], 'harga': [harga]}, index=pd.MultiIndex.from_tuples([(jenis, merek, series, ukuran)], names=['jenis', 'merek', 'series', 'ukuran']))
            self.data_sepatu = pd.concat([self.data_sepatu, new_row])
        self._tulis_data_ke_excel()

    def kurangi_sepatu(self, jenis, merek, series, ukuran, jumlah):
        if (jenis, merek, series, ukuran) in self.data_sepatu.index:
            if self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] >= jumlah:
                self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] -= jumlah
                if self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] == 0:
                    self.data_sepatu = self.data_sepatu.drop((jenis, merek, series, ukuran))
                self._tulis_data_ke_excel()
                return True
            else:
                print(f"Stok tidak mencukupi untuk {merek} {series} ukuran {ukuran}")
                return False
        else:
            print(f"{merek} {series} ukuran {ukuran} tidak ditemukan di gudang")
            return False

def tambah_pesanan(gudang, jenis, pilihan, quantity):
    sepatu_terpilih = gudang.data_sepatu.loc[jenis].iloc[pilihan - 1]
    pesanan.append({
        'jenis': jenis,
        'merek': sepatu_terpilih.name[0],
        'series': sepatu_terpilih.name[1],
        'ukuran': sepatu_terpilih.name[2],
        'harga': sepatu_terpilih['harga'],
        'kuantitas': quantity
    })

def pilih_metode_bayar(metode):
    global metode_bayar
    metode_bayar = metode

def kurangi_stok_setelah_pembayaran(gudang):
    for item in pesanan:
        gudang.kurangi_sepatu(item['jenis'], item['merek'], item['series'], item['ukuran'], item['kuantitas'])

# Example of a main function to tie it together (this would be replaced by GUI event handlers)
def main():
    gudang = GudangSepatu("path_to_excel_file.xlsx")
    nama_customer = input("Nama Customer: ")
    while True:
        pilihan = input("Menu: 1. Tambah Pesanan 2. Pembayaran 3. Keluar\n")
        if pilihan == "1":
            jenis = input("Jenis Sepatu: ")
            print(gudang.data_sepatu.loc[jenis])
            pilihan_sepatu = int(input("Pilih sepatu: "))
            quantity = int(input("Jumlah: "))
            tambah_pesanan(gudang, jenis, pilihan_sepatu, quantity)
        elif pilihan == "2":
            metode = input("Metode Pembayaran (Tunai/QRIS/Transfer): ")
            pilih_metode_bayar(metode)
            if metode in ["Tunai", "QRIS", "Transfer"]:
                kurangi_stok_setelah_pembayaran(gudang)
                print("Pembayaran berhasil")
                break
        elif pilihan == "3":
            print("Keluar")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()
