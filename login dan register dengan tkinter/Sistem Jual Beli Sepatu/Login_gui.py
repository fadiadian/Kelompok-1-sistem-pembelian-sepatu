from tkinter import *
import tkinter.messagebox as msg

class LoginRegisterUser :
    def __init__(self, gui, header) :
        self.gui = gui
        self.gui.geometry('400x350')
        self.gui.title(header)
        self.gui.resizable(True, True)
        self.main_screen()

    def login(self) :
        screen1 = Toplevel(app)
        screen1.title('Login')
        screen1.geometry('350x160')
        Label(screen1, text='Username').pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text='Password').pack()
        self.entryPass = Entry(screen1, show='*', width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text='Lihat Password', variable=self.check, command=self.open_password)
        self.showPass.pack(expand=False, fill=BOTH, padx=10,pady=5)
        self.btnLogin = Button(screen1, text='Login', command=self.do_login).pack(side=LEFT, expand=True, fill=BOTH, padx=10,pady=5)
        self.btnRegister = Button(screen1, text='Register', command=self.register).pack(side=LEFT, expand=True, fill=BOTH, padx=10,pady=5)
        self.btnCancel = Button(screen1, text='Cancel', command=self.close_gui).pack(side=LEFT, expand=True, fill=BOTH, padx=10,pady=5)
    def register(self) :
        self.gui.withdraw()
        screen1 = Toplevel(app)
        screen1.title('Register')
        screen1.geometry('350x2000')
        Label(screen1, text='Nama').pack()
        self.entryUserName = Entry(screen1, width=30)
        self.entryUserName.pack()
        Label(screen1, text='Username').pack()
        self.entryUser = Entry(screen1, width=30)
        self.entryUser.pack()
        Label(screen1, text='Password').pack()
        self.entryPass = Entry(screen1, show='*', width=30)
        self.entryPass.pack()
        self.check = IntVar()
        self.showPass = Checkbutton(screen1, text='Lihat Password', variable=self.check, command=self.open_password)
        self.showPass.pack(expand=False, fill=BOTH, padx=10,pady=5)
        self.btnRegister = Button(screen1, text='Register', command=self.register_user).pack(side=LEFT, expand=True, fill=BOTH, padx=10,pady=5)
        self.btnLogin = Button(screen1, text='Login', command=self.login).pack(side=LEFT, expand=True, fill=BOTH, padx=10,pady=5)
        self.btnCancel = Button(screen1, text='Cancel', command=self.close_gui).pack(side=LEFT, expand=True, fill=BOTH, padx=10,pady=5)
    def register_user(self):
        get_name = self.entryUserName.get()
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        try :
            with open('D:\Kuliah\smt 2\Prakprokom\Sistem Jual Beli Sepatu\database.txt', 'a') as file :
                file.write("\n"+get_name+","+get_username+","+get_password)
                msg.showinfo('Registrasi Sukses', 'Registrasi berhasil, silahkan login', parent=self.gui)
                self.gui.deiconify()
                screen1.destroy()
        except IOError :
            msg.showerror('Error', 'Gagal menulis ke database', parent=self.gui)
    def do_login(self) :
        get_username = self.entryUser.get()
        get_password = self.entryPass.get()
        try :
            with open(r'D:\Kuliah\smt 2\Prakprokom\Sistem Jual Beli Sepatu\database.txt', 'r') as file :
                for line in file :
                    parts = line.strip().split(',')
                    if len(parts) == 3 :
                        nama, username, password = parts
                        if get_username == username and get_password == password :
                            msg.showinfo('Berhasil Login', f'Selamat Datang {nama}', parent=self.gui)
                            self.close_gui
                            return
                msg.showerror('Gagal', 'Username atau Password yang Anda Masukkan Salah, Silahkan Periksa Kembali', parent=self.gui)
        except IOError :
            msg.showerror('Error', 'Gagal Membaca dari Database', parent=self.gui)
    def open_password(self) :
        show = self.check.get()
        if show == 1 : 
            self.entryPass['show'] = ''
        else :
            self.entryPass['show'] = '*'
    def close_gui(self) :
        self.gui.destroy()
    def main_screen(self) :
        Label(text='Selamat Datang di Sistem Jual-Beli Sepatu', bg='blue', width='300', height='2', font=('calibri', 16), fg='white').pack() 
        Label(text='').pack()
        Button(text='Login User', height='2', width='30', command=self.login).pack()
        Label(text='').pack()
        Button(text='Register User', height='2', width='30', command=self.register).pack() 
if __name__ == '__main__' :
    app = Tk()
    start = LoginRegisterUser(app, 'Jual-Beli Sepatu')
    app.mainloop()
