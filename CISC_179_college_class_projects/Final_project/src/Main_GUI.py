import tkinter
from tkinter import ttk 
from Table_Find_Stock_Values import list_of_columns


class MyGUI:
    def __init__(self):

        self.tk = tkinter 
        #create main window widget
        self.main_window = tkinter.Tk()

        self.main_window.title("My First GUI")

        
        
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


        # Create a style object
        self.style = ttk.Style(self.main_window)


        # Configure our custom style for the Treeview widget
        self.style.configure("Custom.Treeview",
        font=('Calibri', 12), background="#d4f2db",
        foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        self.style.configure("Custom.Treeview.Heading", 
        font=('Calibri', 18, 'bold'), 
        foreground="green")
        #background="#00FF00", foreground="black"


        # Create the Treeview widget with the custom style
        self.tree_table = ttk.Treeview(self.main_window, style="Custom.Treeview")

        self.tree_table["columns"] = ("Column 1","Column 2","Column 3","Column 4","Column 5","Column 6","Column 7","Column 8","Column 9")
    


        self.list_of_columns = list_of_columns


        #call the Label widget's pack method
        self.label.pack(ipadx=15,ipady=10)
        self.label2.pack(side="left",ipadx=10,ipady=5,padx=5,pady=5)
        self.button1.pack(side="right",ipadx=10,ipady=10)


        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def stylingTable(self):
        return 
    
    def insertDataToTable(self):
        return 

    def displayHighLowPrice(self):
        return


