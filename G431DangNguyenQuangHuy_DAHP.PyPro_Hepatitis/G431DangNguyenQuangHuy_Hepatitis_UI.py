from tkinter import *
import G431DangNguyenQuangHuy_Hepatitis_Practice as huyPractice
from tkinter import scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import G431DangNguyenQuangHuy_Hepatitis_Game as gamehuy31
class HepatitisUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Hepatitis EDA 31_Đặng Nguyễn Quang Huy_21133036 Đồ Án HP Lập Trình Phân Tích Viêm Gan")
        self.root.geometry("350x450")
        self.root.iconbitmap("./G431DangNguyenQuangHuy_hepatitis/DNQuangHuy31.ico")
        self.root.resizable(False, False)
        self.root.config(background="#f5f5f5")

        # Create a label for the title
        title_label = Label(self.root, text="Hepatitis EDA", font=("Arial", 30, "bold"), fg="#0072c6", bg="#f5f5f5")
        title_label.pack(pady=30)

        # Create a frame for the buttons
        button_frame = Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=30)
        # Create a start button
        start_btn = Button(button_frame, text="Start EDA", command=self.phan_tich, height=3, width=15, font=("Arial", 10),
                        fg="#ffffff", bg="#0072c6", 
                        activebackground="#2196f3", activeforeground="#ffffff",relief=GROOVE)
        start_btn.pack(padx=10, pady=10)
        #Create Start Game
        vis_btn = Button(button_frame, text="Start Game", command=self.Run_Game, height=3, width=15, font=("Arial", 10),
                    fg="#ffffff", bg="#4caf50", activebackground="#2196f3",
                    activeforeground="#ffffff", relief=GROOVE)
        vis_btn.pack(padx=10, pady=10)
        # Create an exit button
        exit_btn = Button(button_frame, text="Exit", command=self.root.destroy, height=3, width=15, font=("Arial", 10),
                        fg="#ffffff", bg="#f44336", activebackground="#2196f3", 
                        activeforeground="#ffffff",relief=GROOVE)
        exit_btn.pack(padx=10, pady=10)
    def phan_tich(self):
        self.wd = Tk()
        self.wd.geometry("1200x650")
        self.wd.title("Hepatitis EDA 31_Đặng Nguyễn Quang Huy_21133036 Đồ Án HP Lập Trình Phân Tích Viêm Gan")
        self.wd.resizable(False, False)
        self.wd.iconbitmap("./G431DangNguyenQuangHuy_hepatitis/DNQuangHuy31.ico")
        # Title label
        self.title = Label(self.wd, text="DATA ANALYSIS HEPATITIS EDA", font=("Arial", 18, "bold"))
        self.title.pack(pady=10)
        # Frame2
        self.frame2 = Frame(self.wd, bg="#ECECEC", bd=2)
        self.frame2.pack(pady=7)
        # Attribute label
        self.huylblinput = Label(self.wd, text="Thuộc Tính Input", font=("Arial", 10, "bold"))
        self.huylblinput.place(x=12,y=100)
        self.huylbloutput = Label(self.wd, text="Thuộc Tính Output", font=("Arial", 10, "bold"))
        self.huylbloutput.place(x=12,y=68)
        # Listbox and label for displaying number of selected items
        self.listbox1 = Listbox(self.frame2, height=16, width=35, font=("Arial", 9, "bold"), selectmode=EXTENDED,bd=3)
        self.listbox1.pack(side=LEFT,padx=10)
        self.hienthi=Label(self.wd, text="Số lượng:",font=("Arial", 10, "bold"))
        self.hienthi.place(x=12,y=420)
        self.lblSoLuong = Label(self.wd, relief=SUNKEN, borderwidth=3, width=13, height=1
                                ,font=("Arial", 10, "bold"), fg="#0072c6",  bg="#ffffff")
        self.lblSoLuong.place(x=100,y=420)
        #Tạo Tree View
        self.style=ttk.Style(self.wd)
        self.style.theme_use("alt")
        self.style.configure('Treeview',background="white",rowheight=25,foreground="black",font=("Arial", 9))
        self.style.map('Treeview',background=[('selected','blue')])
        self.style.configure('Treeview.Heading', font=("Arial", 9, "bold"))
        self.tree = ttk.Treeview(self.wd, show="headings")
        
        #Đăng ký sự kiện
        # Scrolled text input
        self.textinput2 = scrolledtext.ScrolledText(self.frame2, height=25, width=170, bd=3,wrap="none")
        self.textinput2.pack(side=LEFT,padx=7)
        self.textinput1=scrolledtext.ScrolledText(self.wd, height=7, width=111, bd=3)
        self.textinput1.place(x=279,y=475)
        self.trees = ttk.Treeview(self.wd, show="headings")
        # Tạo figure và subplot cho đồ thị
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        # Tạo đối tượng FigureCanvasTkAgg để chứa đồ thị Z-score
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.textinput2)
        #Tạo đối Tượng Hình Vẽ
        self.cbbluachon=ttk.Combobox(self.wd)
        self.cbbluachon.configure(width=13,height=10,font=("Arial", 9, "bold"))
        self.cbbluachon.place(x=150,y=70)
        self.huy31 = huyPractice.Practice(self.textinput2,self.lblSoLuong,self.listbox1,self.tree,self.cbbluachon,self.ax,self.canvas,self.textinput1,self.trees)
        self.listbox1.bind("<Button-3>",self.huy31.ShowPopupMenu_Clicked) 
        self.tree.bind("<<TreeviewSelect>>",self.huy31.SelectValueTree_Clicked)
        # Request,Clear buttons and add buttons
        self.btnrequest = Button(self.wd, text="Request", height=2, width=6, command=self.huy31.PrintResult_Clicked, bg="#4CAF50", fg="#ffffff", font=("Arial", 10)
                                 , activebackground="yellow", activeforeground="black", relief=GROOVE,bd=3)
        self.btnrequest.place(x=10, y=500)
        self.btn = Button(self.wd, text="Clear", height=2, width=6, command=self.huy31.ClearTextBox_Clicked,font=("Arial", 10), activebackground="yellow", 
                          activeforeground="black", relief=GROOVE,bd=3)
        self.btn.place(x=210, y=500)
        self.Add = Button(self.wd, text="Add Cols", height=2, width=6,
                                 font=("Arial", 10),activebackground="yellow",
                                 activeforeground="black",relief=GROOVE,command= self.huy31.InsertData_Clicked,bd=3)
        self.Add.place(x=110,y=500)
        #Menu
        self.menubar = Menu(self.wd, borderwidth=1, relief="solid")
        # Menu File
        self.file_menu = Menu(self.menubar, tearoff=0,
                              font=("Arial", 9, "bold"))
        self.file_menu.add_command(label='File New', command=self.huy31.ReLoad_Clicked)
        self.file_menu.add_command(label='Load Data', command=self.huy31.PrintData_Clicked)
        self.file_menu.add_command(label='Describe', command=self.huy31.PrintDescribe)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.wd.destroy)
        # Menu Edit
        self.edit_menu = Menu(self.menubar, tearoff=0, font=("Arial", 9, "bold"))
        self.edit_menu.add_command(label="Check line null", command=self.huy31.PrintChecknull_Clicked)
        self.edit_menu.add_command(label="Find Common Value ", command=self.huy31.PrintPopularValue_Clicked)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Delete unimportant columns', command=self.huy31.PrintRemoveCo_Clicked)
        self.edit_menu.add_command(label="Replace row with common value", command=self.huy31.PrintChangeRow_Clicked)
        self.edit_menu.add_command(label="Delete Line with null value", command=self.huy31.PrintRemoveRow_Clicked)
        # Menu MaTrix
        self.matrix_menu = Menu(self.menubar, tearoff=0, font=("Arial", 9, "bold"))
        self.matrix_menu.add_command(label='MaTrix Zscore', command=self.huy31.PrintZscore_Clicked)
        self.matrix_menu.add_separator()
        self.matrix_menu.add_command(label="Draw chart Zscore Scatter",command=self.huy31.drawchartsca_Clicked)
        self.matrix_menu.add_command(label="Draw chart Zscore Line",command=self.huy31.drawchartLine_Clicked)
        self.matrix_menu.add_command(label="Remove Isolated",command=self.huy31.printIsolate_Clicked)
        #MenuminMAx
        self.MinMax_s= Menu(self.menubar, tearoff=0, font=("Arial", 9, "bold"))
        self.MinMax_s.add_command(label='Print MinMax_Scaler', command=self.huy31.PrintMinMaxScaler_Clicked)
        self.MinMax_s.add_separator()
        self.MinMax_s.add_command(label="Draw chart  Heatmap",command=self.huy31.draw_heatmap_Clicked)
        #MenuAtribute
        self.Featured = Menu(self.menubar, tearoff=0, font=("Arial", 9, "bold"))
        self.Featured.add_command(label='Choose filter Columns Kbest', command=self.huy31.ChoosefiltColumnsKbest_Clicked) 
        self.Featured.add_command(label='Choose filter Columns PCA', command=self.huy31.ChoosefiltColumnsPCA_Clicked) 
        self.Featured.add_command(label='Print  model model extract', command=self.huy31.ShowColumnsFeature_Clicked) 
        self.Featured.add_separator()
        self.Featured.add_command(label='Draw Attribute Characteristic Scatter', command=self.huy31.drawcharattributeScatter_Clicked) 
        self.Featured.add_command(label='Draw Attribute Characteristic Plot', command=self.huy31.drawcharattributePlot_Clicked) 
        self.Featured.add_command(label='Draw Attribute Characteristic Bar', command=self.huy31.drawcharattributeBar_Clicked) 
        # Add menus to menubar
        self.menubar.add_cascade(label='File', menu=self.file_menu, font=('Helvetica', 20))
        self.menubar.add_cascade(label='Edit', menu=self.edit_menu, font=('Helvetica', 20))
        self.menubar.add_cascade(label='MaTrix', menu=self.matrix_menu, font=('Helvetica', 20))
        self.menubar.add_cascade(label='MinMax_Scaler', menu=self.MinMax_s, font=('Helvetica', 20))
        self.menubar.add_cascade(label='Characteristic Attribute', menu=self.Featured, font=('Helvetica', 20))
        #chỉnh màu cho các widget 
        self.wd.config(background="#E8F8F5")
        self.title.config(fg="#34495E", bg="#E8F8F5")
        self.huylblinput.config(fg="#34495E", bg="#D6EAF8")
        self.huylbloutput.config(fg="#34495E", bg="#D6EAF8")
        self.listbox1.config(fg="#000000", bg="#FFFFFF")
        self.hienthi.config(fg="#34495E", bg="#D6EAF8")
        self.lblSoLuong.config(fg="#34495E", bg="#FFFFFF")
        self.frame2.config(bg="#D6EAF8")
        self.textinput2.config(fg="#000000", bg="#FFFFFF")
        self.textinput1.config(fg="#000000", bg="#FFFFFF")
        self.btnrequest.config(fg="#FFFFFF", bg="#3498DB")
        self.btn.config(fg="#FFFFFF", bg="#E74C3C")
        self.Add.config(fg="#FFFFFF", bg="#2ECC71")
        self.menubar.config(background="#FFFFFF", foreground="#34495E")
        self.file_menu.config(background="#FFFFFF", foreground="#34495E")
        self.edit_menu.config(background="#FFFFFF", foreground="#34495E")
        self.matrix_menu.config(background="#FFFFFF", foreground="#34495E")
        self.MinMax_s.config(background="#FFFFFF", foreground="#34495E")
        self.Featured.config(background="#FFFFFF", foreground="#34495E")
        self.wd.config(menu=self.menubar)
        self.wd.mainloop()
    def Run_Game(self):
        bg =  gamehuy31.Background()
        car =  gamehuy31.Car()
        obstacles =  gamehuy31.Obstacles()
        score =  gamehuy31.Score()
        thucthi=gamehuy31.Run()
        thucthi.gameStart(bg)
        while True:
                thucthi.gamePlay(bg, car, obstacles, score)
                thucthi.gameOver(bg, car, obstacles, score)
        