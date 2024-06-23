class HighestLowestStockPrice_Button:
    def __init__(self):
        return

    def createButton(self,tk,para1):
        #remember that self in this method will get data
        # from this class,
        #tk is meant to get tkinter data from Main_GUI.py
        #para1 is meant to get 'self' data from Main_GUI.py

        #Create Button widget containing text "Dow Jones Stocks February 2020"
        para1.button1= tk.Button(para1.mid_frame, 
        text="Dow Jones Stocks February 2020",width=54,height=2,
        command=para1.displayHighLowPrice,borderwidth=3,
        relief="solid",bg="green",fg="white",
        font=("Helvetica", 15, "bold italic"),cursor=("hand2"))

         #Activate button from Button_Data_Content.py and add hover effect
        para1.button1.pack(side="right",ipadx=10,ipady=10)
        para1.button1.bind("<Enter>", self.on_button_hover)
        para1.button1.bind("<Leave>", self.on_button_leave)

        return para1.button1
    
    def on_button_hover(self,e):
            e.widget['background'] = 'aqua'
    def on_button_leave(self,e):
            e.widget['background'] = 'green'

HighestLowestStockPrice_Button_Obj = HighestLowestStockPrice_Button()
