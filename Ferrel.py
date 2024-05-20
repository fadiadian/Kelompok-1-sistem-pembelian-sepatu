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
            print(f"Stok {model} tidak cukup untuk dikurangi.")

    def tampilkan_stok(self):
        """Menampilkan stok sepatu yang tersedia."""
        print("Stok Gudang Sepatu:")
        for model, jumlah in self.stok_sepatu.items():
            print(f"{model}: {jumlah}")

# Contoh penggunaan
gudang = GudangSepatu()
gudang.tambah_sepatu('Nike Air', 10)
gudang.tambah_sepatu('Adidas Yeezy', 5)
gudang.kurangi_sepatu('Nike Air', 3)
gudang.tampilkan_stok()


