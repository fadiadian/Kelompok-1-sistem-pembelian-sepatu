import pandas as pd

df_sepatu = pd.DataFrame(columns=['Jenis', 'Merek', 'Ukuran', 'Harga'])

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

def trade_in() :
    global df_sepatu
    tampilkan_stok()
    indeks = int(input('Masukkan nomor sepatu yang ingin ditukar :')) - 1

    if 0 <= indeks < len(df_sepatu):
        harga_trade_in = df_sepatu.loc[indeks, "Harga"]
        potongan_harga = harga_trade_in * 0.70
        print(f"Anda akan mendapatkan potongan harga sebesar {potongan_harga} untuk sepatu baru!\n")
        df_sepatu = df_sepatu.drop(index=indeks).reset_index(drop=True)
    else:
        print("Nomor sepatu tidak valid.\n")
