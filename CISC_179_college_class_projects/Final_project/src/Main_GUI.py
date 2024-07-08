import tkinter
from Poster_Img_Data_Content import PosterImgagesData
from Label_Widgets_Data_Content import LabelWidgets_obj
from Button_Data_Content import HighestLowestStockPrice_Button_Obj
from Table_Data_Content import TableData_obj

class MyGUI:
    def __init__(self):

        try:
            self.tk = tkinter 
            #! create main window widget
            self.main_window = tkinter.Tk()

            self.main_window.title("GJK Stock Monitor Program")

            #! create background color for the app
            self.main_window.configure(bg="black")
            
            #! Define frames and activate them
            self.top_frame = tkinter.Frame(self.main_window)
            self.mid_frame = tkinter.Frame(self.main_window)
            self.mid_frame2 = tkinter.Frame(self.main_window)
            self.bottom_frame = tkinter.Frame(self.main_window)

            self.top_frame.pack()
            self.mid_frame.pack()
            self.mid_frame2.pack()
            self.bottom_frame.pack()
        

            #! Create and display poster images inside Label widget 
            #! using data from Poster_Img_Data_Content.py
            PosterImgagesData.poster1Func(tkinter,self).pack(side="left")
            PosterImgagesData.poster2Func(tkinter,self).pack(side="left")

            
            #! Create a StringVar object to use for the value attribute
            #! value attribute is used to store the value of the widget
            #! after the user has clicked the button Dow Jones Stocks February 2020
            self.value = tkinter.StringVar()


           

        
            #! Create and activate the Label widgets
            #! using data from Label_Widgets_Data_Content.py
            LabelWidgets_obj.labelWidget1(tkinter,self)
            LabelWidgets_obj.labelWidget2(tkinter,self)


            #! Create and activate button widget with data 
            #! from Button_Data_Content.py and add hover effect

            #! I wrote the following code near label widgets above
            #! to make place them next to each other on my app
            HighestLowestStockPrice_Button_Obj.createButton(tkinter,self)




            #! Create and style Table widget using data 
            #!  from Table_Data_Content.py
            TableData_obj.createTable(self)
            TableData_obj.stylingTable(tkinter,self)


            tkinter.mainloop()


        #? Display error message if there's any error occurs while running the GUI
        except Exception as e:
            print(f"Running the GUI Error: {e}.\n"+\
                f"Method: __init__().\n"+\
                f"Class: MyGUI.\n"+\
                f"File: Main_GUI.py.\n")   




