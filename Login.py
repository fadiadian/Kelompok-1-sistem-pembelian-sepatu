from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel
def regist():
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Praktikum Prokom\TUBES PRAKPROK!!!\registrasi\assets\frame0")


    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

    global window
    window = Toplevel()

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
        file=relative_to_assets("entry_1 blank.png"))
    entry_bg_1 = canvas.create_image(
        347.5,
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
        width=509.0,
        height=60.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2 blank.png"))
    entry_bg_2 = canvas.create_image(
        347.5,
        448.0,
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
        y=417.0,
        width=509.0,
        height=60.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3 blank.png"))
    entry_bg_3 = canvas.create_image(
        347.5,
        595.0,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        fg="#000716",
        highlightthickness=0,
        font=("Poppins Bold", 30 * -1)
    )
    entry_3.place(
        x=93.0,
        y=564.0,
        width=509.0,
        height=60.0
    )

    canvas.create_text(
        73.0,
        133.0,
        anchor="nw",
        text="Silakan mendaftar",
        fill="#000000",
        font=("Poppins Bold", 30 * -1, 'bold')
    )

    canvas.create_text(
        73.0,
        239.0,
        anchor="nw",
        text="Masukkan Email",
        fill="#000000",
        font=("Poppins SemiBold", 20 * -1, "bold")
    )

    canvas.create_text(
        73.0,
        58.0,
        anchor="nw",
        text="Selamat bergabung!",
        fill="#0057FF",
        font=("Poppins Bold", 50 * -1, "bold")
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1 reg.png"))
    image_1 = canvas.create_image(
        871.0,
        275.0,
        image=image_image_1
    )

    canvas.create_text(
        73.0,
        534.0,
        anchor="nw",
        text="Masukkan Sandi",
        fill="#000000",
        font=("Poppins SemiBold", 20 * -1, 'bold')
    )

    canvas.create_text(
        721.0,
        626.0,
        anchor="nw",
        text="Sudah punya akun? ",
        fill="#000000",
        font=("Poppins Regular", 20 * -1)
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1 login.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1.place(
        x=963.0,
        y=626.0,
        width=58.0,
        height=30.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2 signup.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    button_2.place(
        x=721.0,
        y=564.0,
        width=300.0,
        height=62.0
    )

    canvas.create_text(
        73.0,
        387.0,
        anchor="nw",
        text="Masukkan Nama",
        fill="#000000",
        font=("Poppins SemiBold", 20 * -1, 'bold')
    )
    window.resizable(False, False)
    window.mainloop()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Praktikum Prokom\TUBES PRAKPROK!!!\Uni Login\assets\frame0")

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
