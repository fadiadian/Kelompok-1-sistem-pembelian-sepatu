import pandas as pd

class GudangSepatu:
    def __init__(self, file_path):
        self.file_path = file_path
        self.stok_sepatu = self._baca_stok_dari_csv()

    def _baca_stok_dari_csv(self):
        try:
            df = pd.read_csv(self.file_path)
            df = df.set_index(['model', 'series', 'ukuran'])
            return df
        except FileNotFoundError:
            return pd.DataFrame(columns=['model', 'series', 'ukuran', 'jumlah']).set_index(['model', 'series', 'ukuran'])

    def _tulis_stok_ke_csv(self):
        self.stok_sepatu.to_csv(self.file_path)

    def tambah_sepatu(self, model, series, ukuran, jumlah):
        if (model, series, ukuran) in self.stok_sepatu.index:
            self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] += jumlah
        else:
            new_row = pd.DataFrame({'jumlah': [jumlah]}, index=pd.MultiIndex.from_tuples([(model, series, ukuran)], names=['model', 'series', 'ukuran']))
            self.stok_sepatu = pd.concat([self.stok_sepatu, new_row])
        self._tulis_stok_ke_csv()
        print(f"{jumlah} {model} {series} ukuran {ukuran} telah ditambahkan ke stok.")

    def kurangi_sepatu(self, model, series, ukuran, jumlah):
        if (model, series, ukuran) in self.stok_sepatu.index and self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] >= jumlah:
            self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] -= jumlah
            if self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] == 0:
                self.stok_sepatu = self.stok_sepatu.drop((model, series, ukuran))
            self._tulis_stok_ke_csv()
            print(f"{jumlah} {model} {series} ukuran {ukuran} telah dikurangi dari stok.")
        else:
            print(f"Stok {model} {series} ukuran {ukuran} tidak tersedia atau jumlah tidak mencukupi.")

# Fungsi untuk menangani input pengguna
def handle_input(gudang):
    print("1. Kasir")
    print("2. Tambah Stok Sepatu")
    print("3. Tambah Produk")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        print("Daftar jenis sepatu:")
        print("1. RUNNING SHOES")
        print("2. SNEAKER SHOES")
        print("3. FLIP FLOPS")
        pilih_jenis = input("Input Jenis Sepatu:")
            
        series_dict = {
            "1": {
                "1": ["HOKA", ["ARAHI 7"]],
                "2": ["ASICS", ["GEL-NIMBUS"]],
                "3": ["NIKE", ["ZOOM FLY"]],
                "4": ["ADIDAS", ["ADIZERO"]]
            },
            "2": {
                "1": ["NEW BALANCE", ["550"]],
                "2": ["NIKE", ["AIR FORCE 1"]],
                "3": ["ADIDAS", ["YEEZY", "SAMBA"]],
            },
            "3": {
                "1": ["ADIDAS", ["ADILETTE"]],
                "2": ["NIKE", ["BENASSI"]]
            }
        }

        if pilih_jenis in series_dict:
            print("Merk yang tersedia:")
            for key, value in series_dict[pilih_jenis].items():
                print(f"{key}. {value[0]}")

            merk = input("Pilih merk:")

            if merk in series_dict[pilih_jenis]:
                model, series_list = series_dict[pilih_jenis][merk]
                print(f"Series yang tersedia untuk {model}:")
                for idx, series in enumerate(series_list, 1):
                    print(f"{idx}. {series}")
                
                pilih_series = int(input("Pilih series:"))
                if 1 <= pilih_series <= len(series_list):
                    series = series_list[pilih_series - 1]
                    size = int(input("Masukkan ukuran sepatu (37-45): "))
                    jumlah = int(input("Jumlah yang dibeli: "))
                    gudang.kurangi_sepatu(model, series, size, jumlah)
                    print("Stok berhasil dikurangi")
                else:
                    print("Pilihan series tidak valid.")
            else:
                print("Pilihan merk tidak valid.")
        else:
            print("Pilihan jenis sepatu tidak valid.")

gudang = GudangSepatu('Persediaan.csv')
handle_input(gudang)
