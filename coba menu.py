from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import csv
import os
import pandas as pd
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Praktikum Prokom\Tubes clone\Kelompok-1-sistem-pembelian-sepatu\assets\frame0") #ini kynya udah gak kepake, soalnya udah pakai path absolut

def relative_to_assets(path: str) -> str:
    # Mengembalikan path absolut
    return os.path.join(os.getcwd(), 'Kelompok-1-sistem-pembelian-sepatu', 'assets', 'frame0', path)

def menu():
    global random_data
    window_2 = Tk()

    window_2.geometry("1080x720")
    window_2.configure(bg = "#01041A")

    canvas = Canvas(
        window_2,
        bg = "#01041A",
        height = 720,
        width = 1080,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    csv_file_path = os.path.join(os.getcwd(), 'Kelompok-1-sistem-pembelian-sepatu', 'Persediaan1.xlsx')  # Ganti dengan path file CSV Anda
    all_data = read_data_from_csv(csv_file_path)
    random_data = all_data.sample(n=8)
    canvas.place(x = 0, y = 0)
    image_image_1 = PhotoImage(
        file=relative_to_assets("menu_image_1.png"))
    image_1 = canvas.create_image(
        207.0,
        71.0,
        image=image_image_1
    )

    canvas.create_text(
        85.0,
        38.0, #32
        anchor="nw",
        text="Menu",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1) #25
    )

    menu_button_image_1 = PhotoImage(
        file=relative_to_assets("menu_button_1.png"))
    menu_button_1 = Button(
        image=menu_button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("menu_button_1 clicked"),
        relief="flat",
        bg="#1A1E3E",
        activebackground="#1A1E3E"
    )
    menu_button_1.place(
        x=41.0,
        y=80.0,
        width=25.0,
        height=25.0
    )

    image_image_2 = PhotoImage(
        file=relative_to_assets("menu_image_2.png"))
    image_2 = canvas.create_image(
        53.0,
        51.0,
        image=image_image_2
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("menu_entry_1.png"))
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

    image_image_3 = PhotoImage(
        file=relative_to_assets("menu_image_3.png"))
    image_3 = canvas.create_image(
        207.0,
        425.0,
        image=image_image_3
    )

    canvas.create_text(
        53.0,
        164.0,
        anchor="nw",
        text="Stok saat ini",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, "bold")
    )
    canvas.create_text(
        53.0,
        218.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[0]} {random_data['Seri'].values[0]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        53.0,
        258.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[1]} {random_data['Seri'].values[1]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        298.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[2]} {random_data['Seri'].values[2]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        338.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[3]} {random_data['Seri'].values[3]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        378.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[4]} {random_data['Seri'].values[4]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        55.0,
        418.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[5]} {random_data['Seri'].values[5]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        54.0,
        498.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[6]} {random_data['Seri'].values[7]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        53.0,
        458.0,
        anchor="nw",
        text=f"{random_data['Merek'].values[7]} {random_data['Seri'].values[7]} ",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        218.0,
        anchor="nw",
        text="51",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        258.0,
        anchor="nw",
        text="52",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        298.0,
        anchor="nw",
        text="53",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        338.0,
        anchor="nw",
        text="54",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        378.0,
        anchor="nw",
        text="55",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        418.0,
        anchor="nw",
        text="56",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        498.0,
        anchor="nw",
        text="58",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    canvas.create_text(
        350.0,
        458.0,
        anchor="nw",
        text="57",
        fill="#FFFFFF",
        font=("Poppins", 20 * -1)
    )

    image_image_4 = PhotoImage(
        file=relative_to_assets("menu_image_4.png"))
    image_4 = canvas.create_image(
        739.0,
        360.0,
        image=image_image_4
    )

    menu_button_image_2 = PhotoImage(
        file=relative_to_assets("menu_button_2.png"))
    menu_button_2 = Button(
        image=menu_button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("menu_button_2 clicked"),
        relief="flat",
        bg="#1A1E3E",
        activebackground="#1A1E3E"
    )
    menu_button_2.place(
        x=484.0,
        y=69.0,
        width=548.9635009765625,
        height=127.0
    )

    canvas.create_text(
        477.0,
        26.0, #16
        anchor="nw",
        text="Toko",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, "bold")
    )

    menu_button_image_3 = PhotoImage(
        file=relative_to_assets("menu_button_3.png"))
    menu_button_3 = Button(
        image=menu_button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("menu_button_3 clicked"),
        relief="flat",
        bg="#1A1E3E",
        activebackground="#1A1E3E"
    )
    menu_button_3.place(
        x=675.0,
        y=241.0,
        width=160.0,
        height=241.0
    )

    menu_button_image_4 = PhotoImage(
        file=relative_to_assets("menu_button_4.png"))
    menu_button_4 = Button(
        image=menu_button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("menu_button_4 clicked"),
        relief="flat",
        bg="#1A1E3E",
        activebackground="#1A1E3E"
    )
    menu_button_4.place(
        x=867.0,
        y=250.0,
        width=160.0,
        height=232.0
    )

    menu_button_image_5 = PhotoImage(
        file=relative_to_assets("menu_button_5.png"))
    menu_button_5 = Button(
        image=menu_button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("menu_button_5 clicked"),
        relief="flat",
        bg="#1A1E3E",
        activebackground="#1A1E3E"
    )
    menu_button_5.place(
        x=482.0,
        y=250.0,
        width=160.0,
        height=232.0
    )

    canvas.create_text(
        482.0,
        222.0,
        anchor="nw",
        text="Fitur",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, "bold")
    )

    menu_button_image_6 = PhotoImage(
        file=relative_to_assets("menu_button_6.png"))
    menu_button_6 = Button(
        image=menu_button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("menu_button_6 clicked"),
        relief="flat",
        bg="#1A1E3E",
        activebackground="#1A1E3E"
    )
    menu_button_6.place(
        x=485.0,
        y=558.0,
        width=544.0,
        height=140.0 #height=127.0
    )

    canvas.create_text(
        483.0,
        508.0,#498
        anchor="nw",
        text="Lainnya",
        fill="#FFFFFF",
        font=("Poppins", 25 * -1, "bold")
    )
    window_2.resizable(False, False)
    window_2.mainloop()

menu()