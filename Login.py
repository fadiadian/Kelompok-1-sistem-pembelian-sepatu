from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Praktikum Prokom\Tubes clone\Kelompok-1-sistem-pembelian-sepatu\assets\frame0")

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
    386.0,
    300.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
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
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=93.0,
    y=396.0,
    width=586.0,
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
    font=("Poppins Bold", 30 * -1)
)

canvas.create_text(
    73.0,
    239.0,
    anchor="nw",
    text="Masukkan Username",
    fill="#000000",
    font=("Poppins SemiBold", 20 * -1)
)

canvas.create_text(
    73.0,
    58.0,
    anchor="nw",
    text="Selamat datang!",
    fill="#0057FF",
    font=("Poppins Bold", 50 * -1)
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
    font=("Poppins SemiBold", 20 * -1)
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