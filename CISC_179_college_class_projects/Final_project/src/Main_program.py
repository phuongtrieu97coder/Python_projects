import tkinter
from tkinter import ttk 
from Table_Find_Stock_Values import list_of_columns,find_highest_lowest_stock_values

class MyGUI:
    def __init__(self):

        #create main window widget
        self.main_window = tkinter.Tk()

        self.main_window.title("My First GUI")

        
        # Create a style object
        self.style = ttk.Style(self.main_window)


        self.style.configure("Custom.Treeview.Heading", 
        font=('Calibri', 20, 'bold'), 
        background="#00FF00", foreground="black")

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()


        #create Label widget containing text "Welcome to GJK Stock Monitor Program"
        self.label = tkinter.Label(self.top_frame, 
        text="Welcome to GJK Stock Monitor Program",
        borderwidth=2,relief="solid",bg="blue",fg="white",
        font=("Helvetica", 20, "bold"))

        self.label2 = tkinter.Label(self.mid_frame, 
        text="Trending now is Dow Jones Stocks",
        borderwidth=1,relief="solid",fg="red",
        font=("Helvetica", 15, "bold"))
        
        self.button1 = tkinter.Button(self.mid_frame, 
        text="Dow Jones Stocks February 2020",
        command=self.displayHighLowPrice,borderwidth=2,
        relief="solid",bg="green",fg="white",
        font=("Helvetica", 12, "bold italic"),cursor=("hand2"))
        
        self.value = tkinter.StringVar()

        # Create the Treeview widget with the custom style
        self.tree_table = ttk.Treeview(tkinter.Tk(), style="Custom.Treeview")

        self.tableOutput = tkinter.Label(self.bottom_frame, textvariable=self.value)




        self.tree_table["columns"] = ("Column 1","Column 2","Column 3","Column 4","Column 5","Column 6","Column 7","Column 8","Column 9")
    

        # Format the columns
        self.tree_table.column("#0", width=0, stretch=tkinter.NO)
        for col in range(len(list_of_columns)):
            self.tree_table.column(self.tree_table["columns"][col], anchor=tkinter.W, width=200)

        # Create headings
        self.tree_table.heading("#0", text="", anchor=tkinter.W)
        for col_head in range(len(list_of_columns)):
            self.tree_table.heading(f"Column {col_head+1}", text=list_of_columns[col_head], anchor=tkinter.W)

        
      

        #call the Label widget's pack method
        self.label.pack(ipadx=15,ipady=10)
        self.label2.pack(side="left",ipadx=10,ipady=5,padx=5,pady=5)
        self.button1.pack(side="right",ipadx=10,ipady=10)


        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.tree_table.pack()
        self.tableOutput.pack(side="bottom")

        tkinter.mainloop()

    def insertDataToTable(self):
        list1 = ["Highest Value","Date","Lowest Value","Date Value"]
        highest_val = [list1[0]]
        date_highest_val = [list1[1]]
        lowest_val = [list1[2]]
        date_lowest_val = [list1[3]]

        for l in range(1,len(list_of_columns)):
            highest_val.append(find_highest_lowest_stock_values(list_of_columns[l])[0])
            date_highest_val.append(find_highest_lowest_stock_values(list_of_columns[l])[1])
            lowest_val.append(find_highest_lowest_stock_values(list_of_columns[l])[2])
            date_lowest_val.append(find_highest_lowest_stock_values(list_of_columns[l])[3])
        self.tree_table.insert("", tkinter.END, values=tuple(highest_val))
        self.tree_table.insert("", tkinter.END, values=tuple(date_highest_val))
        self.tree_table.insert("", tkinter.END, values=tuple(lowest_val))
        self.tree_table.insert("", tkinter.END, values=tuple(date_lowest_val))

    def displayHighLowPrice(self):
       self.value.set(self.insertDataToTable())
       #return

if __name__ == "__main__":
    my_gui = MyGUI()