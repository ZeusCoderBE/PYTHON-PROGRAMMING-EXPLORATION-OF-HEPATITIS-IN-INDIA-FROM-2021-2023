import G431DangNguyenQuangHuy_Hepatitis_Process as huyprocess
import matplotlib.pyplot as plt
from tkinter import messagebox
class Chart(huyprocess.Process):
    def __init__(self,text,lbl,lbox,tree,cbbluachon,ax1,canvas1):
        super().__init__(text,lbl,lbox,tree,cbbluachon)
        self.ax1 = ax1
        self.canvas1 = canvas1
    def drawchartsca_Clicked(self):
        try:
            cols = self.zscore
            dzscore=self.zscore
            # Vẽ biểu đồ cho từng cột
            for col in cols:
                data = dzscore[col].reset_index()
                self.ax1.scatter(data['index'], data[col], label=col)
            self.ax1.legend()
            self.ax1.set_title('Biểu đồ Z-Score Scatter',color='Red',fontsize=11)
            self.ax1.set_xlabel('Số Dòng',color='Blue',fontsize=9)
            self.ax1.set_ylabel('Giá Trị Zscore',color='black',fontsize=9)
            self.canvas1.draw()
            self.canvas1.get_tk_widget().place(x=290,y=0)
        except:
            messagebox.showerror("Thông Báo","Vui lòng thực hiện từng bước")
    def drawchartLine_Clicked(self):
        try:
            df2 = self.zscore
            df2.plot(kind='line', legend=True, ax=self.ax1, fontsize=9)
            # Thiết lập tiêu đề cho biểu đồ
            self.ax1.set_title('Biểu đồ Z-Score Line',color='Red',fontsize=11)
            self.ax1.set_xlabel('Số Dòng',color='Blue' ,fontsize=9)
            self.ax1.set_ylabel('Giá Trị Zscore',color='black',fontsize=9)
            self.canvas1.draw()
            self.canvas1.get_tk_widget().place(x=290,y=0)
        except:
            messagebox.showerror("Thông Báo","Vui lòng thực hiện từng bước")
    def drawcharattributeScatter_Clicked(self):
        try:
            x_values=self.temp.reset_index()  
            y_values = self.temp[self.listcolumns] # Convert x-axis values to a numeric data type # Get y-axis values by 
            self.ax1.scatter(x_values['index'],y_values, label=list(self.listcolumns))  # Create a bar chart with the x and y values, with a linewidth of 2
            self.ax1.legend()
            self.ax1.set_title('Biểu đồ Z-Score Scatter',color='Red',fontsize=11)
            self.ax1.set_xlabel('Số Dòng',color='Blue',fontsize=9)
            self.ax1.set_ylabel('Giá Trị ',color='black',fontsize=9)
            self.canvas1.draw()
            self.canvas1.get_tk_widget().place(x=290, y=0)
        except:
            messagebox.showerror("Thông Báo","Bạn chưa chọn cột để vẽ và bạn phải chọn từng cột để vẽ")
    def drawcharattributePlot_Clicked(self):
        try:
            # Sort the DataFrame by the selected column
            sorted_df = self.temp.sort_values(by=self.listcolumns)
            # Get the x and y values
            x_values = sorted_df[self.listcolumns].values.flatten()
            y_values = sorted_df[self.listcolumns].diff().values.flatten()
            # Create a line chart with the x and y values
            self.ax1.plot(x_values, y_values, linewidth=2)
            # Set the x and y labels and title of the chart
            self.ax1.set_xlabel('Thuộc Tính Đặc Trưng')
            self.ax1.set_ylabel('Độ biến thiên')
            self.ax1.set_title('Biểu đồ Plot biểu diễn cột đặc trưng')
            self.ax1.legend(list([self.listcolumns]), loc='upper left')
            # Draw the chart
            self.canvas1.draw()
            # Place the chart in the GUI
            self.canvas1.get_tk_widget().place(x=290,y=0)
        except:
            messagebox.showerror("Thông Báo","Bạn chưa chọn cột để vẽ và bạn phải chọn từng cột để vẽ")
    def drawcharattributeBar_Clicked(self):
        try:
            x_values=self.temp.reset_index()  
            y_values = self.temp[self.listcolumns].values.flatten() # Convert x-axis values to a numeric data type # Get y-axis values by 
            self.ax1.bar(x_values['index'],y_values)  # Create a bar chart with the x and y values, with a linewidth of 2
            self.ax1.set_title('Biểu đồ Cột biểu diễn cột đặc trưng',color='Red',fontsize=11)
            self.ax1.set_xlabel('Số Dòng',color='Blue',fontsize=9)
            self.ax1.set_ylabel('Giá Trị ',color='black',fontsize=9)
            self.ax1.legend(list([self.listcolumns]), loc='upper left')
            self.canvas1.draw()
            self.canvas1.get_tk_widget().place(x=290,y=0)
        except:
            messagebox.showerror("Thông Báo","Bạn chưa chọn cột để vẽ và bạn phải chọn từng cột để vẽ")
    def draw_heatmap_Clicked(self):
        try:
            # Chuẩn bị dữ liệu
            df = self.temp
            # Tính toán ma trận tương quan
            corr_matrix = df.corr()
            # Vẽ biểu đồ heatmap
            heatmap = self.ax1.imshow(corr_matrix, cmap='coolwarm', interpolation='nearest')
            # Thêm chú thích cho từng ô trên biểu đồ
            for i in range(corr_matrix.shape[0]):
                for j in range(corr_matrix.shape[1]):
                    text = self.ax1.text(j, i, '{:.2f}'.format(corr_matrix.iloc[i, j]),
                                        ha='center', va='center', color='white', fontsize=8)
            # Thêm các thông tin cho biểu đồ
            self.ax1.set_xticks(range(corr_matrix.shape[0]))
            self.ax1.set_yticks(range(corr_matrix.shape[1]))
            self.ax1.set_xticklabels(corr_matrix.columns)
            self.ax1.set_yticklabels(corr_matrix.columns)
            plt.setp(self.ax1.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')
            self.ax1.set_title('Biểu đồ Heatmap Z-Score', color='red', fontsize=11)
            self.ax1.set_xlabel('Các biến', color='blue', fontsize=9)
            self.ax1.set_ylabel('Các biến', color='black', fontsize=9)
            # Hiển thị biểu đồ
            self.canvas1.draw()
            self.canvas1.get_tk_widget().place(x=290, y=0)
        except:
            messagebox.showerror("Thông Báo","Vui lòng thực hiện từng bước")
    def delete_chart_Clicked(self):
    # Xóa đối tượng FigureCanvasTkAgg và xóa các đối tượng trên đồ thị
        self.canvas1.get_tk_widget().place_forget()
        self.ax1.clear()
        
    