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

    def kurangi_sepatu(self, model, series, ukuran, jumlah):
        if (model, series, ukuran) in self.stok_sepatu.index and self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] >= jumlah:
            self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] -= jumlah
            if self.stok_sepatu.at[(model, series, ukuran), 'jumlah'] == 0:
                self.stok_sepatu = self.stok_sepatu.drop((model, series, ukuran))
            self._tulis_stok_ke_csv()
            print(f"{jumlah} {model} {series} ukuran {ukuran} telah dikurangi dari stok.")
        else:
            print(f"Stok {model} {series} ukuran {ukuran} tidak tersedia atau jumlah tidak mencukupi.")
    
    def trade_in(self, model_lama, series_lama, ukuran_lama, model_baru, series_baru, ukuran_baru, harga_baru) :
        if (model_lama, series_lama, ukuran_lama) in self.stok_sepatu.index:
            harga_lama = self.stok_sepatu.at[(model_lama, series_lama, ukuran_lama), 'harga']
            potongan_harga = harga_lama * 0.70
            harga_setelah_potongan = max(harga_baru - potongan_harga, 0)
            print(f'Potongan harga untuk trade-in: {potongan_harga}')
            print(f'Harga sepatu baru setelah potongan: {harga_setelah_potongan}')

            self.kurangi_sepatu(model_lama, series_lama, ukuran_lama, 1)
            self.tambah_sepatu(model_baru, series_baru, ukuran_baru, 1, harga_setelah_potongan)
            print(f'Sepatu {model_lama} {series_lama} ukuran {ukuran_lama} telah di trade-in dengan sepatu {model_baru} {series_baru} ukuran {ukuran_baru}.')
        else :
            print(f'Stok sepatu lama {model_lama} {series_lama} ukuran {ukuran_lama} tidak tersedia.')

# Fungsi untuk menangani input pengguna
def handle_input(gudang):
    print("1. Kasir")
    print("2. Tambah Stok Sepatu")
    print("3. Tambah Produk")
    print("4. Trade-In")
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
        
    elif pilihan == "2":
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
                    gudang.tambah_sepatu(model, series, size, jumlah)
                    print("Stok berhasil ditambahkan")
                else:
                    print("Pilihan series tidak valid.")
            else:
                print("Pilihan merk tidak valid.")
        else:
            print("Pilihan jenis sepatu tidak valid.")

    elif pilihan == "4" :
        print("Daftar jenis sepatu lama:")
        print("1. RUNNING SHOES")
        print("2. SNEAKER SHOES")
        print("3. FLIP FLOPS")
        pilih_jenis_lama = input("Input Jenis Sepatu Lama:")

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

        if pilih_jenis_lama in series_dict:
            print("Merk yang tersedia:")
            for key, value in series_dict[pilih_jenis_lama].items():
                print(f"{key}. {value[0]}")

            merk_lama = input("Pilih merk sepatu lama:")

            if merk_lama in series_dict[pilih_jenis_lama]:
                model_lama, series_list_lama = series_dict[pilih_jenis_lama][merk_lama]
                print(f"Series yang tersedia untuk {model_lama}:")
                for idx, series in enumerate(series_list_lama, 1):
                    print(f"{idx}. {series}")

                pilih_series_lama = int(input("Pilih series sepatu lama:"))
                if 1 <= pilih_series_lama <= len(series_list_lama):
                    series_lama = series_list_lama[pilih_series_lama - 1]
                    ukuran_lama = int(input("Masukkan ukuran sepatu lama (37-45): "))

                    print("Daftar jenis sepatu baru:")
                    print("1. RUNNING SHOES")
                    print("2. SNEAKER SHOES")
                    print("3. FLIP FLOPS")
                    pilih_jenis_baru = input("Input Jenis Sepatu Baru:")

                    if pilih_jenis_baru in series_dict:
                        print("Merk yang tersedia:")
                        for key, value in series_dict[pilih_jenis_baru].items():
                            print(f"{key}. {value[0]}")

                        merk_baru = input("Pilih merk sepatu baru:")

                        if merk_baru in series_dict[pilih_jenis_baru]:
                            model_baru, series_list_baru = series_dict[pilih_jenis_baru][merk_baru]
                            print(f"Series yang tersedia untuk {model_baru}:")
                            for idx, series in enumerate(series_list_baru, 1):
                                print(f"{idx}. {series}")

                            pilih_series_baru = int(input("Pilih series sepatu baru:"))
                            if 1 <= pilih_series_baru <= len(series_list_baru):
                                series_baru = series_list_baru[pilih_series_baru - 1]
                                ukuran_baru = int(input("Masukkan ukuran sepatu baru (37-45): "))
                                harga_baru = float(input("Masukkan harga sepatu baru: "))
                                gudang.trade_in(model_lama, series_lama, ukuran_lama, model_baru, series_baru, ukuran_baru, harga_baru)
                                print("Trade-in berhasil.")
                            else:
                                print("Pilihan series tidak valid.")
                        else:
                            print("Pilihan merk tidak valid.")
                    else:
                        print("Pilihan jenis sepatu tidak valid.")
                else:
                    print("Pilihan series tidak valid.")
            else:
                print("Pilihan merk tidak valid.")
        else:
            print("Pilihan jenis sepatu tidak valid.")
    else:
        print("Pilihan tidak valid.")
        

gudang = GudangSepatu('Persediaan.csv')
handle_input(gudang)
if __name__ == "__name__":
    gudang = GudangSepatu('Persediaan.csv')
    handle_input(gudang)