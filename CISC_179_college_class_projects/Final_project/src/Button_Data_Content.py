class HighestLowestStockPrice_Button:
    def __init__(self):
        return

    def createButton(self,tk,para1):
        #! Remember that self parameter in this method 
        #! will get data from this class,
        #! tk is meant to get tkinter data from Main_GUI.py
        #! para1 is meant to get 'self' data from Main_GUI.py

        try:
            #! Create Button widget containing text "Dow Jones Stocks February 2020".

            #? This button will activate displayHighLowPrice() method
            #? in Main_Running_Program.py file
            para1.button1= tk.Button(para1.mid_frame, 
            text="Dow Jones Stocks February 2020",width=54,height=2,
            command=para1.displayHighLowPrice,borderwidth=3,
            relief="solid",bg="green",fg="white",
            font=("Helvetica", 15, "bold italic"),cursor=("hand2"))

            #? Activate button from Button_Data_Content.py and add hover effect
            para1.button1.pack(side="right",ipadx=10,ipady=10)
            para1.button1.bind("<Enter>", self.on_button_hover)
            para1.button1.bind("<Leave>", self.on_button_leave)

            return para1.button1
        
        #? Display error message if there's any error occurs 
        #? while creating the button
        except Exception as e:
             print(f"Creating Button Error: {e}.\n"+\
                f"Method: createButton().\n"+\
                f"Class: HighestLowestStockPrice_Button.\n"+\
                f"File: Button_Data_Content.py.\n")
    
    #? Adding hover effect to the button to change the background color
    def on_button_hover(self,e):
        try:
            e.widget['background'] = 'aqua'

        #? Display error message if there's any error occurs 
        #? while using the mouse to hover over the button
        except Exception as e:
             print(f"Hovering Effect over a button Error: {e}.\n"+\
                f"Method: on_button_hover().\n"+\
                f"Class: HighestLowestStockPrice_Button.\n"+\
                f"File: Button_Data_Content.py.\n")
             

    def on_button_leave(self,e):
        try:
            e.widget['background'] = 'green'
            
        #? Display error message if there's any error occurs 
        #? while moving the mouse out of the button
        except Exception as e:
             print(f"Hovering Effect out of a button Error: {e}.\n"+\
                f"Method: on_button_leave().\n"+\
                f"Class: HighestLowestStockPrice_Button.\n"+\
                f"File: Button_Data_Content.py.\n")

HighestLowestStockPrice_Button_Obj = HighestLowestStockPrice_Button()
