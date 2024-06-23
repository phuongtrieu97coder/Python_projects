class LabelWidgets_Data:
    def labelWidget1(self,tk,para1):
        #create Label widget containing text "Welcome to GJK Stock Monitor Program"
        para1.label = tk.Label(para1.mid_frame, 
        text="Welcome to GJK Stock Monitor Program",width=77,height=2,
        borderwidth=5,relief="solid",bg="blue",fg="white",
        font=("Helvetica", 20, "bold"))

         #call the Label widget's pack method
        para1.label.pack(ipadx=15,ipady=10)

    def labelWidget2(self,tk,para1):
         #create Label widget containing text "Trending now is Dow Jones Stocks" 
        para1.label2 = tk.Label(para1.mid_frame, 
        text="Trending now is Dow Jones Stocks",width=54,height=2,
        borderwidth=1,relief="solid",bg="red",fg="white",
        font=("Helvetica", 15, "bold"))

        para1.label2.pack(side="left",ipadx=10,ipady=18)

        
LabelWidgets_obj = LabelWidgets_Data()