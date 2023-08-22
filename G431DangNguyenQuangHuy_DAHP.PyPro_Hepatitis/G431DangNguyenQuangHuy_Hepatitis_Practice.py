from tkinter import *  
import G431DangNguyenQuangHuy_Hepatitis_Process_Chart as huyprocess
import G431DangNguyenQuangHuy_Hepatitis_Mono as huy31_auto
class Practice(huyprocess. Chart):
    def __init__(self,text,lbl,lbox,tree,cbbluachon,ax1,canvas1,textinput,treesel):
       super().__init__(text,lbl,lbox,tree,cbbluachon,ax1,canvas1)
       self.textinput=textinput
       self.treesel=treesel
    def PrintResult_Clicked(self):
        string=huy31_auto.Command().upper().strip()
        commands = {
        "DỮ LIỆU": self.PrintData_Clicked,
        "CỘT": self.PrintRemoveCo_Clicked,
        "THAY THẾ HÀNG": self.PrintChangeRow_Clicked,
        "HÀNG": self.PrintRemoveRow_Clicked,
        "Lấy Mô Tả":self.PrintDescribe,
        "Kiểm Tra Rỗng":self.PrintChecknull_Clicked,
        "Tìm Giá Trị Phổ Biến":self.PrintPopularValue_Clicked,
        "Tạo Mới":self.ReLoad_Clicked,
        "giá trị cá biệt":self.printIsolate_Clicked,
        "NỘI DUNG":self.ClearTextBox_Clicked,
        "Vẽ Biểu Đồ Đường":self.drawchartLine_Clicked,
        "Xuất Ma Trận":self.PrintZscore_Clicked,
        "Vẽ Biểu Đồ Khác":self.drawchartsca_Clicked,
        "Chuẩn Hoá Rời Rạc":self.PrintMinMaxScaler_Clicked,
        "Trích Lọc K":self.ChoosefiltColumnsKbest_Clicked,
        "Trích Lọc P":self.ChoosefiltColumnsPCA_Clicked,
        "Hiển thị kết quả":self.ShowColumnsFeature_Clicked,
        "Xoá Biểu Đồ":self.delete_chart_Clicked,
        "Vẽ cột đặc trưng":self.drawcharattributeScatter_Clicked
        }
        dem=1
        for key in commands:
            if key.upper().strip() in string:
                command_func = commands[key]
                command_func()
                self.Showtext("\n" + string)
                self.CompleteCommand()
                break
            elif dem==len(commands):
                str=huy31_auto.Mono_Speak("Bạn nói gì tôi không hiểu,Bạn hãy nói lại đi !")
                self.Showtext("\n" + string+"\n" +str )
            else:
                dem+=1
                continue
    def CompleteCommand(self):
        huy31_auto.Mono_Speak("tôi đã hoàn thành nó rồi ,thưa ngài")
    def ClearTextBox_Clicked(self):
        self.text.delete(1.0,END)
        self.textinput.delete(1.0,END)
        self.RemoveTree_Clicked(self.tree)
        self.delete_chart_Clicked()
    def Showtext(self,data):
        self.textinput.insert(END,data)
        self.textinput.insert(END,"\n")
    def SelectValueTree_Clicked(self, event):
        self.RemoveTree_Clicked(self.treesel)
        self.textinput.delete(1.0,END)
        selected_items = self.tree.selection()
        if selected_items:
            selected_item = selected_items[0]
            values = self.tree.item(selected_item, 'values')
            columns = self.tree["columns"]
            self.treesel['columns']=columns
            column_names = [self.tree.heading(col)["text"] for col in columns]
            for col in column_names:
                self.treesel.heading(col,text=col)
                self.treesel.column(col, width=63)
            self.textinput.insert(1.0,"Bạn Đã Chọn:")
            self.treesel.insert("","end",values=values)
            self.treesel.place(x=284,y=510,height=50)
        else:
            self.textinput.insert(1.0,"Bạn Chưa Chọn Gì")



        