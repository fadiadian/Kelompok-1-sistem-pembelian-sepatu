import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app=customtkinter.CTk()
app.geometry("600x440")
app.title("Login")



img1=ImageTk.PhotoImage(Image.open("background_sepatu.jpg"))
l1=customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, width=220, placeholader_text="Log into your account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)   

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50, y=165)

l2=customtkinter.CTkLabel(master=frame, text="Forget password", font=("Century Gothic", 12))
l2.place(x=156, y=195)

app.mainloop