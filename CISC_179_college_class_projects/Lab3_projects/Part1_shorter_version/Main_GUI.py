import tkinter as tk
import tkinter.messagebox as tk_messagebox
from GUI_Data_and_Tools import Cost_Rate_Data
from Title_Label_Content import Top_Frame,Title_Label
from Table1_Content import Mid_Frame1, Mid_Frame1_Table1, Table1_Rows, Table1_Cells_Content
from User_Input_Info_Content import Bottom_Frame1, Bottom_Frame1_Rate_Choosing_Block, Bottom_Frame1_Number_Of_Minutes_Entry_Block, userInputInfo
class MyGUI:
    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Telephone Call Cost")
        self.main_window.configure(bg="black")

        self.tools_data = {}

        Top_Frame(self,"self.top_frame",tk,self.main_window)
        Title_Label(self,"self.title_label",tk,self.tools_data["self.top_frame"])

        Mid_Frame1(self,"self.mid_frame1",tk,self.main_window)

        Mid_Frame1_Table1(self,"self.mid_frame1_table1",tk,self.tools_data["self.mid_frame1"])
        Table1_Rows(self,tk,self.tools_data["self.mid_frame1_table1"])
        Table1_Cells_Content(self,tk,self.tools_data)

        self.selectChargeRateVal = tk.IntVar()
        self.selectChargeRateVal.set(1)

        self.selectChargeRateVal_result = tk.StringVar()
        if self.selectChargeRateVal.get() == 1:
            self.selectChargeRateVal_result.set(f"{Cost_Rate_Data['row2'][1][1:]}")
        
        self.default_number_of_minute = tk.StringVar()
        self.default_number_of_minute.set(1)

        self.totalCost = 0

        Bottom_Frame1(self,tk,self.main_window)
        Bottom_Frame1_Rate_Choosing_Block(self,tk,self.tools_data["self.bottom_frame1"])
        Bottom_Frame1_Number_Of_Minutes_Entry_Block(self,tk,self.tools_data["self.bottom_frame1"])

        userInputInfo(self,tk,Cost_Rate_Data)
       
        tk.mainloop()

    def displaySelectedRate(self):
         if self.selectChargeRateVal.get() == 1:
            self.selectChargeRateVal_result.set(f"{Cost_Rate_Data['row2'][1][1:]}")
         
         if self.selectChargeRateVal.get() == 2:
            self.selectChargeRateVal_result.set(f"{Cost_Rate_Data['row3'][1][1:]}")
        
         if self.selectChargeRateVal.get() == 3:
            self.selectChargeRateVal_result.set(f"{Cost_Rate_Data['row4'][1][1:]}")

    def calculate_cost(self):
        self.totalCost= float(float(self.selectChargeRateVal_result.get())*int(self.tools_data["self.number_of_minutes_entry"].get()))
        tk_messagebox.showinfo("Calculate Cost",f"Total Cost: ${self.totalCost:.2f}")

if __name__ == "__main__":
    my_gui = MyGUI()
