import random
import string
import pandas as pd

def generate_kode(length=10):
    characters = string.ascii_uppercase + string.digits
    kode = ''.join(random.choices(characters, k=length))
    return kode

def generate_ids_for_shoes(shoes_data, output_file):
    ids = []
    for shoe in shoes_data:
        jenis, merek, series, ukuran = shoe 
        kode = generate_kode()
        ids.append([jenis, merek, series, ukuran, kode])

    df = pd.DataFrame(ids, columns=['jenis', 'merek', 'series', 'ukuran', 'kode'])
    df.to_excel(output_file, index=False)

if __name__ == "__main__":
    # Data sepatu dalam format: (Brand, Type, Size)
    shoes_data = [
        ("Running","Hoka", "Arahi 7", 37),
        ("Running","Hoka", "Arahi 7", 38),
        ("Running","Hoka", "Arahi 7", 39),
        ("Running","Hoka", "Arahi 7", 40),
        ("Running","Hoka", "Arahi 7", 41),
        ("Running","Hoka", "Arahi 7", 42),
        ("Running","Hoka", "Arahi 7", 43),
        ("Running","Hoka", "Arahi 7", 44),
        ("Running","Hoka", "Arahi 7", 45),
        ("Running","Asics", "Gel-Nimbus", 37),
        ("Running","Asics", "Gel-Nimbus", 38),
        ("Running","Asics", "Gel-Nimbus", 39),
        ("Running","Asics", "Gel-Nimbus", 40),
        ("Running","Asics", "Gel-Nimbus", 41),
        ("Running","Asics", "Gel-Nimbus", 42),
        ("Running","Asics", "Gel-Nimbus", 43),
        ("Running","Asics", "Gel-Nimbus", 44),
        ("Running","Asics", "Gel-Nimbus", 45),
        ("Running","Nike", "Zoom Fly", 37),
        ("Running","Nike", "Zoom Fly", 38),
        ("Running","Nike", "Zoom Fly", 39),
        ("Running","Nike", "Zoom Fly", 40),
        ("Running","Nike", "Zoom Fly", 41),
        ("Running","Nike", "Zoom Fly", 42),
        ("Running","Nike", "Zoom Fly", 43),
        ("Running","Nike", "Zoom Fly", 44),
        ("Running","Nike", "Zoom Fly", 45),
        ("Running","Adidas", "Adizero", 37),
        ("Running","Adidas", "Adizero", 38),
        ("Running","Adidas", "Adizero", 39),
        ("Running","Adidas", "Adizero", 40),
        ("Running","Adidas", "Adizero", 41),
        ("Running","Adidas", "Adizero", 42),
        ("Running","Adidas", "Adizero", 43),
        ("Running","Adidas", "Adizero", 44),
        ("Running","Adidas", "Adizero", 45),
        ("Sneaker","New Balance", "550", 37),
        
        ("Adidas", "Casual", 40),
        ("Puma", "Sport", 41),
        ("Reebok", "Running", 43),
        ("New Balance", "Casual", 42),
        # Tambahkan data sepatu lainnya sesuai kebutuhan
    ]

    # Nama file Excel output
    output_file = "shoes_ids.xlsx"

    # Panggil fungsi untuk menghasilkan ID dan menyimpan ke file Excel
    generate_ids_for_shoes(shoes_data, output_file)
    print(f"Kode ID sepatu telah disimpan di {output_file}")
