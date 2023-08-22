import pandas as DNQuangHuy31_pd 
import numpy as DNQuangHuy31_np
from scipy import stats
from sklearn import preprocessing 
from sklearn.feature_selection import SelectKBest,chi2
from sklearn.decomposition import PCA
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import *
class Process():
    def __init__(self,text,lbl,lbox,tree,cbbluachon):
        self.text=text
        self.lbl=lbl
        self.lbox=lbox
        self.tree=tree
        self.cbbluachon=cbbluachon
        self.temp=self.ReadFile()
        self.zscore=None
        self.zscore_value=None
        self.numbercolumns=None
        self.listitemdrop=[]
        self.listcolumns=[]
        self.listfeatures=[]
        self.column_order = {0:"Category",1:"ALB",2:"ALP",3:"ALT",4:"AST",
                             5:"BIL",6:"CHE",7:"CHOL",8:"CREA",9:"GGT",10:"PROT",11:"Age",12:"Sex",13:"Unnamed: 0"}
    def ReadFile(self):
        data = DNQuangHuy31_pd.read_csv('./G431DangNguyenQuangHuy_hepatitis.csv')
        data['Sex'] =data['Sex'].map({'m': 0, 'f': 1})
        data['Category'] = data['Category'].map({'0=Blood Donor': 0, '0s=suspect Blood Donor': 0,
        "1=Hepatitis" : 1, "2=Fibrosis" : 1, "3=Cirrhosis" : 1})
        return data
    def MinMaxScaler(self):
        DNQuangHuy31_Scaler=preprocessing.MinMaxScaler()
        self.temp=self.temp.select_dtypes(include=DNQuangHuy31_np.number)
        DNQuangHuy31_Scaler.fit(self.temp)
        #Chuẩn hoá giá trị min max cho tập data frame
        self.temp=DNQuangHuy31_pd.DataFrame(DNQuangHuy31_Scaler.transform(self.temp),index=self.temp.index,columns=self.temp.columns)
        return self.temp
        #rời rạc dữ liệu
    def RemoveColumns(self):
        if   len(self.listitemdrop)==0:
            self.AddItemOut(self.temp.columns)
            return  self.temp
        else:
            self.temp=self.temp.drop(columns=self.listitemdrop,axis=1)
            self.listitemdrop.clear()
            self.AddItemOut(self.temp.columns)
            return self.temp
    def AddItemOut(self,listco):
            self.cbbluachon['values']=list(listco)
    def Checknull(self):
        df31=self.temp.isnull().sum()
        return df31
    def FindPopularValue(self):
        dictitem = {}
        for col in self.temp.columns.to_list():
            popularvalue = self.temp[col].mode()[0]
            dictitem[col] = popularvalue
        df_result = DNQuangHuy31_pd.DataFrame(list(dictitem.items()), columns=['Column', 'PopularValue'])
        return df_result
    def ChangeValues(self):
        self.temp=self.temp.fillna(self.temp.mode().iloc[0])
        return self.temp
    def RemoveRow(self):
        self.temp=self.temp.dropna(how='any')
        return self.temp
    def Zscore(self):
        self.zscore=DNQuangHuy31_np.abs(stats.zscore(self.temp))
        return self.zscore
    def describe(self):
        df31=self.temp.describe()
        return df31
    def RemoveIsolated(self):
        if self.zscore_value is  None:
                self.zscore_value = simpledialog.askfloat("Z-score", "Enter the Z-score value:", minvalue=None)
                self.temp =  self.temp[(self.zscore < self.zscore_value).all(axis=1)].reset_index().drop(columns=['index'])
                return self.temp 
        return self.temp
    def filterextractPCA(self, inp, out, col):
        X = self.temp[inp]
        y = self.temp[[out]]

        pca = PCA(n_components=col)
        pca.fit(X)
        X_pca = pca.transform(X)

        # Lấy tên các cột ban đầu
        column_names = X.columns

        # Lấy ma trận trọng số từ PCA và lấy cột tương ứng với từng thành phần chính
        weight_matrix = pca.components_
        feature_columns = []
        for i in range(col):
            component = weight_matrix[i]
            feature_column = column_names[DNQuangHuy31_np.argmax(abs(component))]
            feature_columns.append(feature_column)
        columnsE = pca.explained_variance_ratio_
        self.listfeatures.append(feature_columns)
        self.ResultFilter(X_pca, y, columnsE)

    def filterextractSKBEST(self,inp,out,col):
        X=self.temp[inp]
        y=self.temp[[out]]
        selectorhuy31=SelectKBest(chi2,k=col)
        selectorhuy31.fit(X,y)
        Xhuy31=selectorhuy31.transform(X)
        columnsE=X.columns[selectorhuy31.get_support(indices=True)]
        self.listfeatures.append(columnsE)
        self.ResultFilter(Xhuy31,y,columnsE)
    def ResultFilter(self,X,y_out,columns_extract):
        self.text.insert(1.0,"Ma Trận Đầu Vào là:"+"\n")
        self.text.insert(END,X)
        self.text.insert(END,"\n"+"Vector Đầu ra là:"+"\n")
        self.text.insert(END,y_out)
        self.text.insert(END,"\n"+"Cột Đặc Trưng:"+"\n")
        self.text.insert(END,list(columns_extract))
    def ResultChoseAtri(self,atri,y_out):
        self.text.insert(1.0,"Trích Lọc thuộc tính đặc trưng"+"\n")
        self.text.insert(END,"\n")
        self.text.insert(END,atri)
        self.text.insert(END,"\n"+"Vector Đầu ra là:"+"\n")
        self.text.insert(END,y_out) 
    def PrintDescribe(self):
        self.text.insert(1.0,"Mô tả dữ liệu"+"\n")
        df31=self.describe()
        self.text.insert(END,df31)
    def load_data_to_treeview(self, df_31):
        columns = list(df_31.columns)
        # Set the headings for the columns
        self.tree["columns"] = columns
        for col in columns:
            self.tree.heading(col,text=col)
        # Set the width of each column
        for col in columns:
            self.tree.column(col, width=63)
        # Insert the data from the dataframe into the Treeview widget
        for index, row in df_31.iterrows():
            values = [row[col] for col in columns]
            self.tree.insert("", index, values=values)
        # Place the Treeview widget in the GUI
        self.tree.place(x=286, y=65, height=400)
    def PrintPopularValue_Clicked(self):
        self.text.insert(1.0,"Giá trị phổ biến của từng cột là:"+"\n")
        popular=self.FindPopularValue()
        self.text.insert(END,popular)
    def PrintChecknull_Clicked(self):
        df31=self.Checknull()
        self.text.insert(1.0,"Kết Quả khi kiểm tra null là:"+"\n")
        self.text.insert(END,df31)
    def PrintData_Clicked(self):
        self.load_data_to_treeview(self.temp)
    def ReLoad_Clicked(self):
        self.temp=self.ReadFile()
        self.zscore=None
        self.zscore_value=None
        self.numbercolumns=None
        self.listitemdrop=[]
        self.listcolumns=[]
        self.listfeatures=[]
        self.lbox.delete(0,END)
        self.UpdateSizeListBox()
    def UpdateSizeListBox(self):
        dem  =  self.lbox.size()
        self.lbl.configure(text = dem)
    def PrintZscore_Clicked(self):
        DNQuangHuy31_df=self.Zscore()
        self.load_data_to_treeview(DNQuangHuy31_df)
    def PrintRemoveCo_Clicked(self):
        DNQuangHuy31_df=self.ReadFile()
        self.text.insert(1.0,"Số lượng cột và dòng ban đầu là:"+"\n")
        self.text.insert(END,DNQuangHuy31_df.shape)
        try :
            DNQuangHuy31=self.RemoveColumns()
            self.text.insert(END,"\n")
            self.text.insert(END,"\n"+"Số lượng cột và dòng sau khi xoá là:"+"\n")
            self.text.insert(END,DNQuangHuy31.shape)
        except:
              messagebox.showerror("Thông Báo","Cột Đó Đã Xoá Rồi")
    def PrintChangeRow_Clicked(self):
        result=self.ChangeValues()
        self.load_data_to_treeview(result)
    def PrintRemoveRow_Clicked(self):
        DNQuangHuy31_df=self.ReadFile()
        self.text.insert(1.0,"Số lượng dòng và cột ban đầu là: "+"\n")
        self.text.insert(END,DNQuangHuy31_df.shape)
        DNQuangHuy31_df=self.RemoveRow()
        self.text.insert(END,"\n"+"Số lượng dòng và cột sau khi xoá là:"+"\n")
        self.text.insert(END,DNQuangHuy31_df.shape)
        return DNQuangHuy31_df
    def printIsolate_Clicked(self):
        try:
            DNQuangHuy31_df=self.RemoveIsolated()
            self.text.insert(1.0,"Đã Loại bỏ Thành Công: "+"\n")
            self.text.insert(END,"Còn Lại Số Lượng dòng và cột là: "+"\n")
            self.text.insert(END,DNQuangHuy31_df.shape)
        except:
             messagebox.showerror("Thông Báo","Vui lòng thực hiện từng bước")
             self.zscore_value = None
    def PrintMinMaxScaler_Clicked(self):
        DNQuangHuy31_df=self.MinMaxScaler()
        self.load_data_to_treeview(DNQuangHuy31_df)
        
    def InsertData_Clicked(self):
        for col  in  self.column_order:
            if self.lbox.get(0, END).count(self.column_order[col]) >0:
                # Tên cột bị trùng  
               continue
            else:
                # Thêm tên cột vào Listbox
                self.lbox.insert(col, self.column_order[col])
                # Cập nhật số lượng cột hiện có trong Listbox
                self.UpdateSizeListBox()
        self.AddItemOut(self.column_order.values())
    def ChoseColumns_Clicked(self):
       selected_items = [self.lbox.get(i) for i in self.lbox.curselection()]
       self.listcolumns.extend(selected_items)
       self.lbox.select_clear(0,END) # bỏ chế độ chọn các pt đã chọn
    def Delete_Clicked(self):
        i = 0
        while i<self.lbox.size():
             if(self.lbox.select_includes(i) == 1): 
                 self.listitemdrop.append(self.lbox.get(i))
                 self.lbox.delete(i)
                 i=-1
             i=i+1
        self.UpdateSizeListBox()
        self.lbox.select_clear(0,END) # bỏ chế độ chọn các pt đã chọn
    def ViewSelectedColumns_Clicked(self):
        self.text.insert(1.0,"Những Cột Đã Chọn:"+"\n")
        self.text.insert(END,self.listcolumns)
    def RemoveSelectedColumns_Clicked(self):
        self.text.insert(1.0,"Đã Xoá Thành Công"+"\n")
        self.text.insert(END,self.listcolumns)
        self.listcolumns=[]
    def ShowPopupMenu_Clicked(self,e): 
        if self.lbox.size() > 0 : 
            popMenu = Menu(self.lbox, tearoff = FALSE)
            popMenu.add_command(label = "Delete", command = self.Delete_Clicked)
            popMenu.add_command(label = "Chose Columns input",command=self.ChoseColumns_Clicked)
            popMenu.add_command(label="View Select Columns",command=self.ViewSelectedColumns_Clicked)
            popMenu.add_command(label="Remove Selected Columns",command=self.RemoveSelectedColumns_Clicked)
            popMenu.tk_popup(e.x_root, e.y_root)#phải thiết lập x_root, y_root để showpopup
    def RemoveTree_Clicked(self,tree):
        for col in tree['columns']:
            tree.heading(col, text="")
        for item in tree.get_children():
            tree.delete(item)
        tree.place_forget()
    def ShowColumnsFeature_Clicked(self):
        self.text.insert(1.0,"Mô hình trích lọc các thuộc tính đặc trưng"+"\n")
        self.text.insert(END,"\n")
        self.text.insert(END,list(self.listfeatures))
        try:
            self.text.insert(END,"\n")
            if  len(self.listcolumns)==0 or not self.cbbluachon.get():
                self.text.insert(END,"Bạn vui lòng quét khối chọn các thuộc tính đặc trưng "+"\n"+
                             " đã hiển thị trên màn hình.Sau đó hãy chọn thuộc tính output")
            else:
                self.ResultChoseAtri(self.temp[self.listcolumns],self.temp[[self.cbbluachon.get()]])
        except:
            messagebox.showerror("Có lỗi xảy ra")
    def ChoosefiltColumnsKbest_Clicked(self):
        try:
            if  self.numbercolumns is None or len(self.listcolumns)==0:
                self.numbercolumns = simpledialog.askinteger("Số Lượng", "Vui Lòng Nhập số lượng cột đặc trưng: ", minvalue=None)
                self.filterextractSKBEST(self.listcolumns,self.cbbluachon.get(),self.numbercolumns )
            else:
                self.filterextractSKBEST(self.listcolumns,self.cbbluachon.get(),self.numbercolumns)
        except:
            self.numbercolumns=None
            messagebox.showerror("Thông Báo","Bạn chưa quét khối chọn input hoặc output đầu ra hoặc số lượng cột để trích lọc:! Vui lòng thử lại") 
    
    def ChoosefiltColumnsPCA_Clicked(self):
        try:
            if  self.numbercolumns is None or len(self.listcolumns)==0:
                self.numbercolumns = simpledialog.askinteger("Số Lượng", "Vui Lòng Nhập số lượng cột đặc trưng: ", minvalue=None)
                self.filterextractPCA(self.listcolumns,self.cbbluachon.get(),self.numbercolumns )
            else:
                self.filterextractPCA(self.listcolumns,self.cbbluachon.get(),self.numbercolumns)
        except:
            self.numbercolumns=None
            messagebox.showerror("Thông Báo","Bạn chưa quét khối chọn input hoặc output đầu ra hoặc số lượng cột để trích lọc:! Vui lòng thử lại") 