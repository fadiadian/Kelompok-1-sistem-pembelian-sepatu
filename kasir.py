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

# Fungsi untuk menangani input pengguna
def handle_input(gudang):
        print("Daftar jenis sepatu:")
        print("1. RUNNING SHOES")
        print("2. SNEAKER SHOES")
        print("3. FLIP FLOPS")
        pilih_jenis = input("Input Jenis Sepatu:")
        if pilih_jenis == "1": #jika memilih running shoes
                print("Merk yang tersedia:")
                print("1. HOKA ARAHI 7 ")
                print("2. ASICS GEL-NIMBUS")
                print("3. NIKE ZOOM FLY")
                print("4. ADIDAS ADIZERO")
                merk = input ("Pilih merk:")

                if merk =="1": #jika memilih hoka arahi 7
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                elif merk == "2": #jika memilih asics gel-nimbus
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                elif merk == "3": #jika memilih nike zoom fly
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                else : #pilihan adidas adizero
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
        elif pilih_jenis == "2": #jika memilih sneaker shoes
                print("Merk yang tersedia:")
                print("1. NEW BALANCE 550")
                print("2. NIKE AIR FORCE 1")
                print("3. ADIDAS YEEZY")
                print("4. ADIDAS SAMBA")
                merk = input ("Pilih merk:")

                if merk =="1": #jika memilih new balance 550
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                elif merk == "2": #jika memilih nike air force 1
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                elif merk == "3": #jika memilih adidas yeezy
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                else : #jika memilih adidas samba
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
        else : #pilihan flip flops
                print("Merk yang tersedia:")
                print("1. ADIDAS ADILETTE")
                print("2. NIKE BENASSI")
                merk = input ("Pilih merk:")

                if merk =="1": #jika memilih adidas adilette
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")
                else : #pilihan nike benassi
                     size = int(input("Masukkan ukuran sepatu (37-45): : "))
                     jumlah = int(input("Jumlah yang dibeli :"))
                     gudang.kurangi_sepatu( jumlah, pilih_jenis, size)
                     print ("Stok berhasil dikurangi")                    
gudang = GudangSepatu()
handle_input(gudang)
