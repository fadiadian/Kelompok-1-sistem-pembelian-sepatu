import pandas as pd

class GudangSepatu:
    def __init__(self, file_path):
        self.file_path = file_path
        self.stok_sepatu = self._baca_stok_dari_csv()

    def _baca_stok_dari_csv(self):
        try:
            df = pd.read_csv(self.file_path)
            df = df.set_index(['model', 'ukuran'])
            return df
        except FileNotFoundError:
            return pd.DataFrame(columns=['model', 'ukuran', 'jumlah']).set_index(['model', 'ukuran'])

    def _tulis_stok_ke_csv(self):
        self.stok_sepatu.to_csv(self.file_path)

    def tambah_sepatu(self, model, ukuran, jumlah):
        if (model, ukuran) in self.stok_sepatu.index:
            self.stok_sepatu.at[(model, ukuran), 'jumlah'] += jumlah
        else:
            new_row = pd.DataFrame({'jumlah': [jumlah]}, index=pd.MultiIndex.from_tuples([(model, ukuran)], names=['model', 'ukuran']))
            self.stok_sepatu = pd.concat([self.stok_sepatu, new_row])
        self._tulis_stok_ke_csv()
        print(f"{jumlah} {model} ukuran {ukuran} telah ditambahkan ke stok.")

    def kurangi_sepatu(self, model, ukuran, jumlah):
        if (model, ukuran) in self.stok_sepatu.index and self.stok_sepatu.at[(model, ukuran), 'jumlah'] >= jumlah:
            self.stok_sepatu.at[(model, ukuran), 'jumlah'] -= jumlah
            if self.stok_sepatu.at[(model, ukuran), 'jumlah'] == 0:
                self.stok_sepatu = self.stok_sepatu.drop((model, ukuran))
            self._tulis_stok_ke_csv()
            print(f"{jumlah} {model} ukuran {ukuran} telah dikurangi dari stok.")
        else:
            print(f"Stok {model} ukuran {ukuran} tidak tersedia atau jumlah tidak mencukupi.")

# Fungsi untuk menangani input pengguna
def handle_input(gudang):
    print("Daftar jenis sepatu:")
    print("1. RUNNING SHOES")
    print("2. SNEAKER SHOES")
    print("3. FLIP FLOPS")
    pilih_jenis = input("Input Jenis Sepatu:")
    if pilih_jenis == "1":  # jika memilih running shoes
        print("Merk yang tersedia:")
        print("1. HOKA ARAHI 7")
        print("2. ASICS GEL-NIMBUS")
        print("3. NIKE ZOOM FLY")
        print("4. ADIDAS ADIZERO")
        merk = input("Pilih merk:")

        if merk in ["1", "2", "3", "4"]:
            merk_dict = {
                "1": "HOKA ARAHI 7",
                "2": "ASICS GEL-NIMBUS",
                "3": "NIKE ZOOM FLY",
                "4": "ADIDAS ADIZERO"
            }
            model = merk_dict[merk]
            size = int(input("Masukkan ukuran sepatu (37-45): "))
            jumlah = int(input("Jumlah yang dibeli: "))
            gudang.kurangi_sepatu(model, size, jumlah)
            print("Stok berhasil dikurangi")

    elif pilih_jenis == "2":  # jika memilih sneaker shoes
        print("Merk yang tersedia:")
        print("1. NEW BALANCE 550")
        print("2. NIKE AIR FORCE 1")
        print("3. ADIDAS YEEZY")
        print("4. ADIDAS SAMBA")
        merk = input("Pilih merk:")

        if merk in ["1", "2", "3", "4"]:
            merk_dict = {
                "1": "NEW BALANCE 550",
                "2": "NIKE AIR FORCE 1",
                "3": "ADIDAS YEEZY",
                "4": "ADIDAS SAMBA"
            }
            model = merk_dict[merk]
            size = int(input("Masukkan ukuran sepatu (37-45): "))
            jumlah = int(input("Jumlah yang dibeli: "))
            gudang.kurangi_sepatu(model, size, jumlah)
            print("Stok berhasil dikurangi")

    elif pilih_jenis == "3":  # jika memilih flip flops
        print("Merk yang tersedia:")
        print("1. ADIDAS ADILETTE")
        print("2. NIKE BENASSI")
        merk = input("Pilih merk:")

        if merk in ["1", "2"]:
            merk_dict = {
                "1": "ADIDAS ADILETTE",
                "2": "NIKE BENASSI"
            }
            model = merk_dict[merk]
            size = int(input("Masukkan ukuran sepatu (37-45): "))
            jumlah = int(input("Jumlah yang dibeli: "))
            gudang.kurangi_sepatu(model, size, jumlah)
            print("Stok berhasil dikurangi")

gudang = GudangSepatu('stok_sepatu.csv')
handle_input(gudang)
