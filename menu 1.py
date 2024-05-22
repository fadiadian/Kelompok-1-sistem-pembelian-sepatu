class GudangSepatu:
    def _init_(self):
        self.stok_sepatu = {}  # Dictionary untuk menyimpan stok


     
    
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
        print("3. Tambah Produk")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            print("Daftar jenis sepatu:")
            print("1. RUNNING SHOES")
            print("2. SNEAKER SHOES")
            print("3. FLIP FLOPS")
            jenis = input("Input Jenis Sepatu:")

            if jenis == "1":
                print("Merk yang tersedia:")
                print("1. HOKA ARAHI 7")
                print("2. ASICS GEL-NIMBUS")
                print("3. NIKE ZOOM FLY")
                print("4. ADIDAS ADIZERO")
                merk = input ("Pilih merk:")

                if merk =="1":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                elif merk == "2":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                elif merk == "3":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                else :
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")

            if jenis == "2":
                print("Merk yang tersedia:")
                print("1. NEW BALANCE 550")
                print("2. NIKE AIR FORCE 1")
                print("3. ADIDAS YEEZY")
                print("4. ADIDAS SAMBA")
                merk = input ("Pilih merk:")

                if merk =="1":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                elif merk == "2":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                elif merk == "3":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                else :
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")

            if jenis == "3":
                print("Merk yang tersedia:")
                print("1. ADIDAS ADILETTE")
                print("2. NIKE BENASSI")
                merk = input ("Pilih merk:")

                if merk =="1":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
                elif merk == "2":
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Masukkan jumlah barang: "))
                     gudang.tambah_stok( jumlah, jenis, size, merk)
                     print ("Stok berhasil ditambahkan")
        if pilihan == "3":
            tambah_produk_baru = input("Masukkan Kode Barang, Kategori Sepatu, Merk & Tipe Sepatu: ")
            size_baru = int(input("Masukkan size produk baru: "))
            
        



        
                     
                
            
        
gudang = GudangSepatu()
handle_input(gudang)
   