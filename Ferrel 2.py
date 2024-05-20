# Program Pencatatan Logistik Gudang Sepatu

class GudangSepatu:
    def __init__(self):
        self.stok_sepatu = {}  # Dictionary untuk menyimpan stok

    def tambah_sepatu(self, model, jumlah):
        """Menambahkan sepatu ke dalam stok."""
        if model in self.stok_sepatu:
            self.stok_sepatu[model] += jumlah
        else:
            self.stok_sepatu[model] = jumlah
        print(f"{jumlah} {model} telah ditambahkan ke stok.")

    def kurangi_sepatu(self, model, jumlah):
        """Mengurangi sepatu dari stok."""
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
def handle_user_input(gudang):
    while True:
        print("\nMenu:")
        print("1. Tambah Sepatu")
        print("2. Kurangi Sepatu")
        print("3. Tampilkan Stok")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            jenis = int(input("Masukkan jenis : "))
            model = int(input("Masukkan nama barang: "))
            jumlah = int(input("Masukkan jumlah: "))
            gudang.tambah_sepatu(model, jumlah)
        elif pilihan == '2':
            jenis = int(input("Masukkan jenis : "))
            model = int(input("Masukkan nama barang: "))
            jumlah = int(input("Masukkan jumlah: "))
            gudang.kurangi_sepatu(model, jumlah)
        elif pilihan == '3':
            gudang.tampilkan_stok()
        elif pilihan == '4':
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


gudang = GudangSepatu()
handle_user_input(gudang)

