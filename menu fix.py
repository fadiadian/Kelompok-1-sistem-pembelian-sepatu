import pandas as pd

class GudangSepatu:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_sepatu = self._baca_data_dari_excel()

    def _baca_data_dari_excel(self):
        try:
            # Coba membaca sheet 'Persediaan1'
            print(f"Membaca data dari file: {self.file_path}")
            df = pd.read_excel(self.file_path, sheet_name='Persediaan1')
            if df.empty:
                print("Sheet 'Persediaan1' kosong atau tidak sesuai format.")
            else:
                print("Sheet 'Persediaan1' berhasil dibaca.")
                print(df.head())  # Menampilkan beberapa baris pertama untuk verifikasi
            df = df.set_index(['jenis', 'merek', 'series', 'ukuran'])
            return df
        except FileNotFoundError:
            print(f"File {self.file_path} tidak ditemukan.")
            return pd.DataFrame(columns=['jenis', 'merek', 'series', 'ukuran', 'jumlah', 'harga']).set_index(['jenis', 'merek', 'series', 'ukuran'])
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
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
        print(f"{jumlah} {series} ukuran {ukuran} telah ditambahkan ke stok dengan harga {harga}.")

    def kurangi_sepatu(self, jenis, merek, series, ukuran, jumlah):
        if (jenis, merek, series, ukuran) in self.data_sepatu.index and self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] >= jumlah:
            self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] -= jumlah
            if self.data_sepatu.at[(jenis, merek, series, ukuran), 'jumlah'] == 0:
                self.data_sepatu = self.data_sepatu.drop((jenis, merek, series, ukuran))
            self._tulis_data_ke_excel()
            print(f"{jumlah} {series} ukuran {ukuran} telah dikurangi dari stok.")
        else:
            print(f"Stok {series} ukuran {ukuran} tidak tersedia atau jumlah tidak mencukupi.")

    def trade_in(self, jenis_lama, merek_lama, series_lama, ukuran_lama, jenis_baru, merek_baru, series_baru, ukuran_baru, harga_baru):
        if (jenis_lama, merek_lama, series_lama, ukuran_lama) in self.data_sepatu.index:
            harga_lama = self.data_sepatu.at[(jenis_lama, merek_lama, series_lama, ukuran_lama), 'harga']
            potongan_harga = harga_lama * 0.70
            harga_setelah_potongan = max(harga_baru - potongan_harga, 0)
            print(f'Potongan harga untuk trade-in: {potongan_harga}')
            print(f'Harga sepatu baru setelah potongan: {harga_setelah_potongan}')

            self.kurangi_sepatu(jenis_lama, merek_lama, series_lama, ukuran_lama, 1)
            self.tambah_sepatu(jenis_baru, merek_baru, series_baru, ukuran_baru, 1, harga_setelah_potongan)
            print(f'Sepatu lama {series_lama} ukuran {ukuran_lama} telah di trade-in dengan sepatu baru {series_baru} ukuran {ukuran_baru}.')
        else:
            print(f'Stok sepatu lama {series_lama} ukuran {ukuran_lama} tidak tersedia.')

    def tampilkan_stok(self):
        print("Menampilkan stok sepatu:")
        print(self.data_sepatu)

# Fungsi untuk menangani input pengguna
def handle_input(gudang):
    print("1. Tampilkan Stok Sepatu")
    print("2. Kasir")
    print("3. Tambah Stok Sepatu")
    print("4. Trade-In")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        gudang.tampilkan_stok()

    elif pilihan == "2":
        jenis_list = list(gudang.data_sepatu.index.get_level_values('jenis').unique())
        print("Daftar jenis sepatu:")
        for idx, jenis in enumerate(jenis_list, 1):
            print(f"{idx}. {jenis}")
        pilih_jenis_idx = int(input("Input Jenis Sepatu:"))
        if 1 <= pilih_jenis_idx <= len(jenis_list):
            pilih_jenis = jenis_list[pilih_jenis_idx - 1]
            merek_list = list(gudang.data_sepatu.loc[pilih_jenis].index.get_level_values('merek').unique())
            print("merek yang tersedia:")
            for idx, merek in enumerate(merek_list, 1):
                print(f"{idx}. {merek}")

            merek_idx = int(input("Pilih merek:"))
            if 1 <= merek_idx <= len(merek_list):
                merek = merek_list[merek_idx - 1]
                series_list = list(gudang.data_sepatu.loc[(pilih_jenis, merek)].index.get_level_values('series').unique())
                print(f"Series yang tersedia untuk {merek}:")
                for idx, series in enumerate(series_list, 1):
                    print(f"{idx}. {series}")

                pilih_series_idx = int(input("Pilih series:"))
                if 1 <= pilih_series_idx <= len(series_list):
                    series = series_list[pilih_series_idx - 1]
                    ukuran_list = list(gudang.data_sepatu.loc[(pilih_jenis, merek, series)].index.get_level_values('ukuran').unique())
                    print(f"Ukuran yang tersedia untuk {series}:")
                    for idx, ukuran in enumerate(ukuran_list, 1):
                        print(f"{idx}. {ukuran}")

                    pilih_ukuran_idx = int(input("Pilih ukuran:"))
                    if 1 <= pilih_ukuran_idx <= len(ukuran_list):
                        ukuran = ukuran_list[pilih_ukuran_idx - 1]
                        jumlah = int(input("Jumlah yang dibeli: "))
                        gudang.kurangi_sepatu(pilih_jenis, merek, series, ukuran, jumlah)
                        print("Stok berhasil dikurangi")
                    else:
                        print("Pilihan ukuran tidak valid.")
                else:
                    print("Pilihan series tidak valid.")
            else:
                print("Pilihan merek tidak valid.")
        else:
            print("Pilihan jenis sepatu tidak valid.")

    elif pilihan == "3":
        jenis_list = list(gudang.data_sepatu.index.get_level_values('jenis').unique())
        print("Daftar jenis sepatu:")
        for idx, jenis in enumerate(jenis_list, 1):
            print(f"{idx}. {jenis}")
        pilih_jenis_idx = int(input("Input Jenis Sepatu:"))
        if 1 <= pilih_jenis_idx <= len(jenis_list):
            pilih_jenis = jenis_list[pilih_jenis_idx - 1]
            merek_list = list(gudang.data_sepatu.loc[pilih_jenis].index.get_level_values('merek').unique())
            print("merek yang tersedia:")
            for idx, merek in enumerate(merek_list, 1):
                print(f"{idx}. {merek}")

            merek_idx = int(input("Pilih merek:"))
            if 1 <= merek_idx <= len(merek_list):
                merek = merek_list[merek_idx - 1]
                series_list = list(gudang.data_sepatu.loc[(pilih_jenis, merek)].index.get_level_values('series').unique())
                print(f"Series yang tersedia untuk {merek}:")
                for idx, series in enumerate(series_list, 1):
                    print(f"{idx}. {series}")

                pilih_series_idx = int(input("Pilih series:"))
                if 1 <= pilih_series_idx <= len(series_list):
                    series = series_list[pilih_series_idx - 1]
                    ukuran = int(input("Masukkan ukuran sepatu (37-45): "))
                    jumlah = int(input("Jumlah sepatu yang ditambahkan: "))
                    harga = float(input("Masukkan harga sepatu: "))
                    gudang.tambah_sepatu(pilih_jenis, merek, series, ukuran, jumlah, harga)
                    print("Stok berhasil ditambahkan")
                else:
                    print("Pilihan series tidak valid.")
            else:
                print("Pilihan merek tidak valid.")
        else:
            print("Pilihan jenis sepatu tidak valid.")

    elif pilihan == "4":
        jenis_list = list(gudang.data_sepatu.index.get_level_values('jenis').unique())
        print("Daftar jenis sepatu lama:")
        for idx, jenis in enumerate(jenis_list, 1):
            print(f"{idx}. {jenis}")
        pilih_jenis_lama_idx = int(input("Input Jenis Sepatu Lama:"))
        if 1 <= pilih_jenis_lama_idx <= len(jenis_list):
            pilih_jenis_lama = jenis_list[pilih_jenis_lama_idx - 1]
            merek_list = list(gudang.data_sepatu.loc[pilih_jenis_lama].index.get_level_values('merek').unique())
            print("merek yang tersedia:")
            for idx, merek in enumerate(merek_list, 1):
                print(f"{idx}. {merek}")

            merek_lama_idx = int(input("Pilih merek sepatu lama:"))
            if 1 <= merek_lama_idx <= len(merek_list):
                merek_lama = merek_list[merek_lama_idx - 1]
                series_list_lama = list(gudang.data_sepatu.loc[(pilih_jenis_lama, merek_lama)].index.get_level_values('series').unique())
                print(f"Series yang tersedia untuk {merek_lama}:")
                for idx, series in enumerate(series_list_lama, 1):
                    print(f"{idx}. {series}")

                pilih_series_lama_idx = int(input("Pilih series sepatu lama:"))
                if 1 <= pilih_series_lama_idx <= len(series_list_lama):
                    series_lama = series_list_lama[pilih_series_lama_idx - 1]
                    ukuran_lama = int(input("Masukkan ukuran sepatu lama (37-45): "))

                    print("Daftar jenis sepatu baru:")
                    for idx, jenis in enumerate(jenis_list, 1):
                        print(f"{idx}. {jenis}")
                    pilih_jenis_baru_idx = int(input("Input Jenis Sepatu Baru:"))
                    if 1 <= pilih_jenis_baru_idx <= len(jenis_list):
                        pilih_jenis_baru = jenis_list[pilih_jenis_baru_idx - 1]
                        merek_list_baru = list(gudang.data_sepatu.loc[pilih_jenis_baru].index.get_level_values('merek').unique())
                        print("merek yang tersedia:")
                        for idx, merek in enumerate(merek_list_baru, 1):
                            print(f"{idx}. {merek}")

                        merek_baru_idx = int(input("Pilih merek sepatu baru:"))
                        if 1 <= merek_baru_idx <= len(merek_list_baru):
                            merek_baru = merek_list_baru[merek_baru_idx - 1]
                            series_list_baru = list(gudang.data_sepatu.loc[(pilih_jenis_baru, merek_baru)].index.get_level_values('series').unique())
                            print(f"Series yang tersedia untuk {merek_baru}:")
                            for idx, series in enumerate(series_list_baru, 1):
                                print(f"{idx}. {series}")

                            pilih_series_baru_idx = int(input("Pilih series sepatu baru:"))
                            if 1 <= pilih_series_baru_idx <= len(series_list_baru):
                                series_baru = series_list_baru[pilih_series_baru_idx - 1]
                                ukuran_baru = int(input("Masukkan ukuran sepatu baru (37-45): "))
                                harga_baru = float(input("Masukkan harga sepatu baru: "))
                                gudang.trade_in(pilih_jenis_lama, merek_lama, series_lama, ukuran_lama, pilih_jenis_baru, merek_baru, series_baru, ukuran_baru, harga_baru)
                                print("Trade-in berhasil.")
                            else:
                                print("Pilihan series tidak valid.")
                        else:
                            print("Pilihan merek tidak valid.")
                    else:
                        print("Pilihan jenis sepatu tidak valid.")
                else:
                    print("Pilihan series tidak valid.")
            else:
                print("Pilihan merek tidak valid.")
        else:
            print("Pilihan jenis sepatu tidak valid.")
    else:
        print("Pilihan tidak valid.")

# Pastikan file Excel memiliki sheet yang sesuai
gudang = GudangSepatu('Persediaan1.xlsx')
handle_input(gudang)


           

