from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import csv

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Praktikum Prokom\Tubes clone\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#=============  V  verifikasi dan proses login  V  =================
def verifikasi_login(username, password):
    with open('databaseuser/logindatabase.csv', mode='r') as file:
        reader = csv.DictReader(file) 
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return True
    return False

def proses_login():
    username = entry_username.get()
    password = entry_pw.get()
    
    if verifikasi_login(username, password):
        messagebox.showinfo("Sukses", "Login berhasil!") #kalo main menu udah jadi masukin di baris setelah ini
        main()
    else:
        messagebox.showerror("Error", "Nama pengguna atau kata sandi salah")

#=============  A  verifikasi dan proses login  A  =================

def program_awal():
    window = Tk()
    global entry_username, entry_pw

    window.geometry("1080x720")
    window.configure(bg="#FFFFFF")

    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=720,
        width=1080,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        386.0,
        300.0,
        image=entry_image_1
    )
    entry_username = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 30 * -1)
    )
    entry_username.place(
        x=93.0,
        y=269.0,
        width=586.0,
        height=60.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        386.0,
        427.0,
        image=entry_image_2
    )
    entry_pw = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins", 30 * -1), show="*"
    )
    entry_pw.place(
        x=93.0,
        y=396.0,
        width=586.0,
        height=60.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_login = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=proses_login,
        relief="flat"
    )
    button_login.place(
        x=163.0,
        y=549.0,
        width=753.0,
        height=62.0
    )

    canvas.create_text(
        73.0,
        133.0,
        anchor="nw",
        text="Silakan login",
        fill="#000000",
        font=("Poppins Bold", 30 * -1, 'bold')
    )

    canvas.create_text(
        73.0,
        239.0,
        anchor="nw",
        text="Masukkan Username",
        fill="#000000",
        font=("Poppins SemiBold", 20 * -1, 'bold')
    )

    canvas.create_text(
        73.0,
        58.0,
        anchor="nw",
        text="Selamat datang!",
        fill="#0057FF",
        font=("Poppins Bold", 50 * -1, 'bold')
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        903.0,
        363.0,
        image=image_image_1
    )

    canvas.create_text(
        73.0,
        366.0,
        anchor="nw",
        text="Masukkan Sandi",
        fill="#000000",
        font=("Poppins SemiBold", 20 * -1, 'bold')
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=549.0,
        y=458.0,
        width=150.0,
        height=30.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2.png"))
    image_2 = canvas.create_image(
        917.0,
        82.0,
        image=image_image_2
    )
    window.resizable(False, False)
    window.mainloop()

# main ini nanti dimasukin ke login 
def main():
    window = Tk()

    window.geometry("1080x720")
    window.configure(bg = "#000000")


    canvas = Canvas(
        window,
        bg = "#000000",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1_main.png"))
    image_1 = canvas.create_image(
        207.0,
        71.0,
        image=image_image_1
    )

    canvas.create_text(
        85.0,
        32.0,
        anchor="nw",
        text="Menu",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1)
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("image_2_main.png"))
    image_2 = canvas.create_image(
        53.0,
        92.0,
        image=image_image_2
    )

    image_image_3 = PhotoImage(
        file=relative_to_assets("image_3_main.png"))
    image_3 = canvas.create_image(
        53.0,
        51.0,
        image=image_image_3
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1_main.png"))
    entry_bg_1 = canvas.create_image(
        175.5,
        91.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=97.5,
        y=79.0,
        width=156.0,
        height=23.0
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("image_4_main.png"))
    image_4 = canvas.create_image(
        207.0,
        425.0,
        image=image_image_4
    )

    canvas.create_text(
        53.0,
        164.0,
        anchor="nw",
        text="Stok saat ini",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, 'bold')
    )

    canvas.create_text(
        53.0,
        218.0,
        anchor="nw",
        text="Sepatu_1",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        53.0,
        258.0,
        anchor="nw",
        text="Sepatu_2",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        298.0,
        anchor="nw",
        text="Sepatu_3",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        338.0,
        anchor="nw",
        text="Sepatu_4",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        378.0,
        anchor="nw",
        text="Sepatu_5",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        55.0,
        418.0,
        anchor="nw",
        text="Sepatu_6",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        498.0,
        anchor="nw",
        text="Sepatu_8",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        53.0,
        458.0,
        anchor="nw",
        text="Sepatu_7",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        266.0,
        218.0,
        anchor="nw",
        text="51",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        266.0,
        258.0,
        anchor="nw",
        text="52",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        267.0,
        298.0,
        anchor="nw",
        text="53",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        267.0,
        338.0,
        anchor="nw",
        text="54",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        267.0,
        378.0,
        anchor="nw",
        text="55",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        268.0,
        418.0,
        anchor="nw",
        text="56",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        267.0,
        498.0,
        anchor="nw",
        text="58",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        266.0,
        458.0,
        anchor="nw",
        text="57",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    image_image_5 = PhotoImage(
        file=relative_to_assets("image_5_main.png"))
    image_5 = canvas.create_image(
        739.0,
        360.0,
        image=image_image_5
    )

    image_image_6 = PhotoImage(
        file=relative_to_assets("image_6_main.png"))
    image_6 = canvas.create_image(
        749.0,
        132.0,
        image=image_image_6
    )

    canvas.create_text(
        495.0,
        115.0,
        anchor="nw",
        text="Menampilkan data dan katalog sepatu\nyang pernah terdaftar di database",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        495.0,
        82.0,
        anchor="nw",
        text="Daftar Produk",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1, 'bold')
    )

    image_image_7 = PhotoImage(
        file=relative_to_assets("image_7_main.png"))
    image_7 = canvas.create_image(
        926.0,
        88.0,
        image=image_image_7
    )

    canvas.create_text(
        477.0,
        16.0,
        anchor="nw",
        text="Toko",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, 'bold')
    )

    image_image_8 = PhotoImage(
        file=relative_to_assets("image_8_main.png"))
    image_8 = canvas.create_image(
        755.0,
        398.0,
        image=image_image_8
    )

    image_image_9 = PhotoImage(
        file=relative_to_assets("image_9_main.png"))
    image_9 = canvas.create_image(
        755.0,
        304.0,
        image=image_image_9
    )

    canvas.create_text(
        693.0,
        368.0,
        anchor="nw",
        text="Update stok",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1, 'bold')
    )

    canvas.create_text(
        675.0,
        398.0,
        anchor="nw",
        text="Menambah atau\nmengurangi stok\nyang ada",
        fill="#FFFFFF",
        font=("Poppins", 15 * -1)
    )

    image_image_10 = PhotoImage(
        file=relative_to_assets("image_10_main.png"))
    image_10 = canvas.create_image(
        947.0,
        398.0,
        image=image_image_10
    )

    image_image_11 = PhotoImage(
        file=relative_to_assets("image_11_main.png"))
    image_11 = canvas.create_image(
        947.0,
        308.0,
        image=image_image_11
    )

    canvas.create_text(
        868.0,
        398.0,
        anchor="nw",
        text="Untuk menambah\nproduk baru",
        fill="#FFFFFF",
        font=("Poppins", 15 * -1)
    )

    canvas.create_text(
        885.0,
        368.0,
        anchor="nw",
        text="Produk baru",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1, 'bold')
    )

    image_image_12 = PhotoImage(
        file=relative_to_assets("image_12_main.png"))
    image_12 = canvas.create_image(
        562.0,
        398.0,
        image=image_image_12
    )

    image_image_13 = PhotoImage(
        file=relative_to_assets("image_13_main.png"))
    image_13 = canvas.create_image(
        562.0,
        308.0,
        image=image_image_13
    )

    canvas.create_text(
        485.0,
        398.0,
        anchor="nw",
        text="Untuk memproses\ntransaksi\npembayaran",
        fill="#FFFFFF",
        font=("Poppins", 15 * -1)
    )

    canvas.create_text(
        536.0,
        368.0,
        anchor="nw",
        text="Kasir",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1, 'bold')
    )

    canvas.create_text(
        482.0,
        222.0,
        anchor="nw",
        text="Fitur",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, 'bold')
    )

    image_image_14 = PhotoImage(
        file=relative_to_assets("image_14_main.png"))
    image_14 = canvas.create_image(
        756.0,
        621.0,
        image=image_image_14
    )

    canvas.create_text(
        502.0,
        604.0,
        anchor="nw",
        text="Tukar-Tambah sepatu lamamu\ndengan sepatu baru",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        502.0,
        574.0,
        anchor="nw",
        text="Trade in",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1, 'bold')
    )

    image_image_15 = PhotoImage(
        file=relative_to_assets("image_15_main.png"))
    image_15 = canvas.create_image(
        934.0,
        576.0,
        image=image_image_15
    )

    canvas.create_text(
        483.0,
        508.0,
        anchor="nw",
        text="Unggulan",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, 'bold')
    )
    window.resizable(False, False)
    window.mainloop()


program_awal()