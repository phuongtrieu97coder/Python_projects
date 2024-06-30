class LabelWidgets_Data:
    def labelWidget1(self,tk,para1):
        try:
           #! create Label widget containing text "Welcome to GJK Stock Monitor Program"
           para1.label = tk.Label(para1.mid_frame, 
           text="Welcome to GJK Stock Monitor Program",width=77,height=2,
           borderwidth=5,relief="solid",bg="blue",fg="white",
           font=("Helvetica", 20, "bold"))

           #! call the Label widget's pack method
           para1.label.pack(ipadx=15,ipady=10)

        #? Display error message if there's any error occurs while creating the label widget 1
        except Exception as e:
            print(f"Label Widget 1 Error: {e}.\n"+\
                f"Method: labelWidget1().\n"+\
                f"Class: LabelWidgets_Data.\n"+\
                f"File: Label_Widgets_Data_Content.py.\n")

    def labelWidget2(self,tk,para1):
        try:
           #! create Label widget containing text "Trending now is Dow Jones Stocks" 
           para1.label2 = tk.Label(para1.mid_frame, 
           text="Trending now is Dow Jones Stocks",width=54,height=2,
           borderwidth=1,relief="solid",bg="red",fg="white",
           font=("Helvetica", 15, "bold"))

           para1.label2.pack(side="left",ipadx=10,ipady=18)

        #? Display error message if there's any error occurs while creating the label widget 2
        except Exception as e:
            print(f"Label Widget 2 Error: {e}.\n"+\
                f"Method: labelWidget2().\n"+\
                f"Class: LabelWidgets_Data.\n"+\
                f"File: Label_Widgets_Data_Content.py.\n")

        
LabelWidgets_obj = LabelWidgets_Data()