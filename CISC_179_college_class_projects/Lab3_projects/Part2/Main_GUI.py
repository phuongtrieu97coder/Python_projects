import tkinter as tk
from Table1_Content import table1_column1_contents,table1_column2_contents
from User_Input_Info_Content import userInputInfo
from Assessment_Value_Property_Tax_Results import Assessment_Value_Property_Tax_Results_func
class MyGUI:
    def __init__(self):

        self.main_window = tk.Tk()
        self.main_window.title("Assessment Value and Property Tax Calculator")
        self.main_window.configure(bg="black")

        self.top_frame = tk.Frame(self.main_window,bg="aqua")
        self.top_frame.pack(side="top")


        self.mid_frame = tk.Frame(self.main_window,bg="darkblue")
        self.mid_frame.pack(side="top")

        self.mid_frame_table1_column1 = tk.Frame(self.mid_frame,bg="green")
        self.mid_frame_table1_column1.pack(side="left",padx=(20,0))

        self.mid_frame_table1_column2 = tk.Frame(self.mid_frame,bg="green")
        self.mid_frame_table1_column2.pack(side="left",padx=(0,20))

        self.mid_frame2 = tk.Frame(self.main_window,bg="darkblue")
        self.mid_frame2.pack(side="top")


        self.bottom_frame = tk.Frame(self.main_window,width=60,bg="darkblue")
        self.bottom_frame.pack(side="top",pady=(0,15))

        
        self.user_property_actual_value = tk.StringVar()
        self.user_property_actual_value.set(0.0)

        self.assessment_value = tk.StringVar()
        self.assessment_value.set("$0.0")

        self.property_tax_value = tk.StringVar()
        self.property_tax_value.set("$0.0")




        self.title_label = tk.Label(self.top_frame, 
        text="🧮 Assessment Value and Property Tax Calculator",
        font=("Helvetica",20,"bold"),bg="blue",fg="white",width=56)
        self.title_label.pack(side="top",ipadx=20,ipady=10,padx=6,pady=6)

        table1_column1_contents(self,tk)
        table1_column2_contents(self,tk)

        userInputInfo(self,tk)

        Assessment_Value_Property_Tax_Results_func(self,tk)

        tk.mainloop()

  



    def calculate_assessment_value_and_property_tax(self):
        get_assessment_value = float(float(self.user_property_actual_value.get())*60/100)
        self.assessment_value.set(f"${get_assessment_value:.3f}")

        get_property_tax = float(get_assessment_value*0.75/100)
        self.property_tax_value.set(f"${get_property_tax:.3f}")

if __name__ == "__main__":
    my_gui = MyGUI()