from tkinter import *

class SimpleDialog(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.geometry("400x150")
        self.master.config(bg="#f9f9f9")
        self.master.title("Voice Assistant MoNo-Huy31")
        self.master.resizable(False, False)
        self.create_widgets()
    def create_widgets(self):
        self.label = Label(self.master, text="Nhập lệnh của bạn:", font=("Arial", 12), bg="#f9f9f9", fg="#333333")
        self.label.pack(pady=10)
        self.textbox = Entry(self.master, width=50, bg='#ffffff', fg='#333333', font=('Arial', 12), relief='solid')
        self.textbox.pack(pady=5)
        self.button = Button(self.master, text="Nhập lệnh", command=self.get_command, bg='#0099cc', fg='#ffffff', font=('Arial', 14), relief='raised')
        self.button.pack(pady=5)
    def get_command(self):
        self.command = self.textbox.get()
        self.master.withdraw()  # đóng cửa sổ dialog
        self.master.quit()  # dừng chương trình
    def set_command(self):
        self.master.mainloop()
        return self.command