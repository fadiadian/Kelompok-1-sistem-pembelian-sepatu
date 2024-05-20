from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
def regist():
    
    OUTPUT_PATH = Path(__file__).parent

    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\TUBES PROKOM\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")

    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Tubes Prokom\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")
 

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import csv
 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Kuliah\smt 2\TUBES FROKOM\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")

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


OUTPUT_PATH = Path(__file__).parent

ASSETS_PATH = OUTPUT_PATH / Path(r"D:\TUBES PROKOM\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")

ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Tubes Prokom\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")
 

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1080x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    325.5,
    300.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Bold", 30 * -1)
)
entry_1.place(
    x=93.0,
    y=269.0,
    width=465.0,
    height=60.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    325.5,
    427.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("Poppins Bold", 30 * -1)
)
entry_2.place(
    x=93.0,
    y=396.0,
    width=465.0,
    height=60.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=208.0,
    y=564.0,
    width=583.0,
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
    text="Masukkan Email",
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
    808.0,
    282.0,
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

canvas.create_text(
    380.0,
    626.0,
    anchor="nw",
    text="Belum punya akun? ",
    fill="#000000",
    font=("Poppins Regular", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: regist(),
    relief="flat"
)
button_2.place(
    x=598.0,
    y=626.0,
    width=162.0,
    height=30.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=428.0,
    y=458.0,
    width=150.0,
    height=30.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=760.0,
    y=564.0,
    width=149.0,
    height=62.0
)
window.resizable(False, False)
window.mainloop()

program_awal()
 
