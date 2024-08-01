import tkinter as tk
import tkinter.messagebox as tk_messagebox
from Table1_Content import table1_column1_contents,table1_column2_contents
from User_Input_Info_Content import userInputInfo
class MyGUI:
    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Telephone Call Cost")
        self.main_window.configure(bg="black")

        self.top_frame = tk.Frame(self.main_window,bg="aqua")
        self.top_frame.pack(side="top")


        self.mid_frame = tk.Frame(self.main_window,bg="darkblue")
        self.mid_frame.pack(side="top")

        self.mid_frame_table1_column1 = tk.Frame(self.mid_frame,bg="green")
        self.mid_frame_table1_column1.pack(side="left",padx=(20,0))

        self.mid_frame_table1_column2 = tk.Frame(self.mid_frame,bg="green")
        self.mid_frame_table1_column2.pack(side="left",padx=(0,20))


        self.bottom_frame = tk.Frame(self.main_window,width=60,bg="darkblue")
        self.bottom_frame.pack(side="top")

        self.selectChargeRateVal = tk.IntVar()
        self.selectChargeRateVal.set(1)

        self.selectChargeRateVal_result = tk.StringVar()
        if self.selectChargeRateVal.get() == 1:
            self.selectChargeRateVal_result.set("0.07")

        
        self.default_number_of_minute = tk.StringVar()
        self.default_number_of_minute.set(1)

        self.totalCost = 0


        self.title_label = tk.Label(self.top_frame, 
        text="Telephone Call Cost (Long-distance Charge Rates)",
        font=("Helvetica",20,"bold"),bg="blue",fg="white",width=56)
        self.title_label.pack(side="top",ipadx=20,ipady=10,padx=6,pady=6)

        table1_column1_contents(self,tk)
        table1_column2_contents(self,tk)

        userInputInfo(self,tk)

        tk.mainloop()

    def rate1_select_func(self):
        self.displaySelectedRate("0.07")

    def rate2_select_func(self):
        self.displaySelectedRate("0.12")

    def rate3_select_func(self):
        self.displaySelectedRate("0.05")

    def displaySelectedRate(self,rate) :
        self.selectChargeRateVal_result.set(rate)   



    def calculate_cost(self):
        self.totalCost= float(float(self.selectChargeRateVal_result.get())*int(self.number_of_minutes_entry.get()))
        tk_messagebox.showinfo("Calculate Cost",f"Total Cost: ${self.totalCost:.2f}")

if __name__ == "__main__":
    my_gui = MyGUI()