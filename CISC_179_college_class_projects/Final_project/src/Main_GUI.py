import tkinter
from tkinter import ttk 
from PIL import Image, ImageTk
from Table_Find_Stock_Values import list_of_columns


class MyGUI:
    def __init__(self):

        self.tk = tkinter 
        #create main window widget
        self.main_window = tkinter.Tk()

        self.main_window.title("GJK Stock Monitor Program")

        #create background color for the app
        self.main_window.configure(bg="black")
        
        
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        #poster1
        self.openImg = Image.open("stock_poster1_img.jpg")
        self.openImg = self.openImg.resize((670, 350), Image.LANCZOS)
        self.poster1 = ImageTk.PhotoImage(self.openImg)

        self.poster_label = tkinter.Label(self.top_frame, image=self.poster1)

        #poster2
        self.openImg2 = Image.open("stock_poster2_img.jpg")
        self.openImg2 = self.openImg2.resize((670, 350), Image.LANCZOS)
        self.poster2 = ImageTk.PhotoImage(self.openImg2)

        self.poster_label2 = tkinter.Label(self.top_frame, image=self.poster2)


        #create Label widget containing text "Welcome to GJK Stock Monitor Program"
        self.label = tkinter.Label(self.mid_frame, 
        text="Welcome to GJK Stock Monitor Program",width=77,height=2,
        borderwidth=5,relief="solid",bg="blue",fg="white",
        font=("Helvetica", 20, "bold"))

        self.label2 = tkinter.Label(self.mid_frame, 
        text="Trending now is Dow Jones Stocks",width=54,height=2,
        borderwidth=1,relief="solid",bg="red",fg="white",
        font=("Helvetica", 15, "bold"))
        
        self.button1 = tkinter.Button(self.mid_frame, 
        text="Dow Jones Stocks February 2020",width=54,height=2,
        command=self.displayHighLowPrice,borderwidth=3,
        relief="solid",bg="green",fg="white",
        font=("Helvetica", 15, "bold italic"),cursor=("hand2"))
        
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
        self.poster_label.pack(side="left")
        self.poster_label2.pack(side="right")


        self.label.pack(ipadx=15,ipady=10)
        self.label2.pack(side="left",ipadx=10,ipady=18)
        self.button1.pack(side="right",ipadx=10,ipady=10)

        def on_button_hover(e):
            e.widget['background'] = 'aqua'
        def on_button_leave(e):
            e.widget['background'] = 'green'

        self.button1.bind("<Enter>", on_button_hover)
        self.button1.bind("<Leave>", on_button_leave)


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


