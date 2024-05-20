class GudangSepatu:
    def _init_(self):
        self.stok_sepatu = {}  # Dictionary untuk menyimpan stok
    def tambah_sepatu(self, model, jumlah):
         if model in self.stok_sepatu:
            self.stok_sepatu[model] += jumlah
            self.stok_sepatu += jumlah