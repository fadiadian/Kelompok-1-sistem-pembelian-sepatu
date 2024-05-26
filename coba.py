import pandas as pd
import os

# Baca file XLSX
file_path = os.path.join(os.getcwd(), 'Kelompok-1-sistem-pembelian-sepatu', 'Persediaan.xlsx')
df = pd.read_excel(file_path)
def _baca_stok_dari_csv(self):
        try:
            df = pd.read_csv(self.file_path)
            df = df.set_index(['model', 'series', 'ukuran'])
            return df
        except FileNotFoundError:
            return pd.DataFrame(columns=['model', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['model', 'series', 'ukuran'])

def _tulis_stok_ke_csv(self):
        self.stok_sepatu.to_csv(self.file_path)
def tambah_sepatu(self, model, series, ukuran, jumlah, harga):
        if (model, series, ukuran) in self.stok_sepatu.index:
            self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] += jumlah
        else:
            new_row = pd.DataFrame({'jumlah': [jumlah], 'harga' : [harga]}, index=pd.MultiIndex.from_tuples([(model, series, ukuran)], names=['model', 'series', 'ukuran']))
            self.stok_sepatu = pd.concat([self.stok_sepatu, new_row])
        self._tulis_stok_ke_csv()
        print(f"{jumlah} {model} {series} ukuran {ukuran} telah ditambahkan ke stok dengan harga {harga}.")
kode_produk = str(input("Masukkan kode produk: "))
print_produk_info(df, kode_produk)
