class GudangSepatu:
    def _init_(self):
        self.stok_sepatu = {}  # Dictionary untuk menyimpan stok
    def tambah_sepatu(self, model, jumlah):
         if model in self.stok_sepatu:
            self.stok_sepatu[model] += jumlah
            self.stok_sepatu += jumlah
         else:
            self.stok_sepatu[model] = jumlah
            self.stok_sepatu = jumlah
            print(f"{jumlah} {model} telah ditambahkan ke stok.")

    def kurangi_sepatu(self, model, jumlah):
        if model in self.stok_sepatu and self.stok_sepatu[model] >= jumlah:
            self.stok_sepatu[model] -= jumlah
            print(f"{jumlah} {model} telah dikurangi dari stok.")
        else:
            print(f"Stok {model} tidak tersedia.")

    def tampilkan_stok(self):
        """Menampilkan stok sepatu yang tersedia."""
        print("Stok Gudang Sepatu:")
        for model, jumlah in self.stok_sepatu.items():
            print(f"{model}: {jumlah}")

    


# Fungsi untuk menangani input pengguna
def handle_input(gudang):
        print("\nMenu:")
        print("1. Tambah Stok Sepatu")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            print("Daftar jenis sepatu:")
            print("1. RUNNING SHOES")
            print("2. SNEAKER SHOES")
            print("3. FLIP FLOPS")
            pilih_jenis = input("Input Jenis Sepatu:")

            if pilih_jenis == "1":
                print("Merk yang tersedia:")
                print("1. HOKA ARAHI 7")
                print("2. ASICS GEL-NIMBUS")
                print("3. NIKE ZOOM FLY")
                print("4. ADIDAS ADIZERO")
                merk = input ("Pilih merk:")

                if merk =="1":
                     size = int(input("Masukkan jumlah: "))
                     gudang.tambah_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil ditambahkan")

                print("Size tersedia:")
                print("41")
                print("42")
                size = input ("Pilih size")
                
                if size =="42":
                     jumlah = int(input("Masukkan jumlah: "))
                     gudang.tambah_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil ditambahkan")
            
        
gudang = GudangSepatu()
handle_input(gudang)
   