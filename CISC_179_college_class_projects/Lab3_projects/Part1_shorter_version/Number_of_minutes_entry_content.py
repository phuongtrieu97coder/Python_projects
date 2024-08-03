from GUI_Data_and_Tools import createFrame, createLabel, createEntry, createButton 
def number_of_minutes_entry_content(self,tk): 
    createFrame(self,"self.number_of_minutes_entry_content_frame1",tk,self.tools_data["self.bottom_frame1_number_of_minutes_entry_block"],
    20,"darkblue","top",0,0,(20,20),10)
    number_of_minutes_entry_content_inquiry_label_and_entry(self,tk)

    createFrame(self,"self.number_of_minutes_entry_content_frame2",tk,self.tools_data["self.bottom_frame1_number_of_minutes_entry_block"],
    20,"darkblue","top",0,0,(0,20),10)
    number_of_minutes_entry_content_calculate_cost_button(self,tk)

def number_of_minutes_entry_content_inquiry_label_and_entry(self,tk):
    createLabel(self,"self.number_of_minutes_inquiry_label",tk,self.tools_data["self.number_of_minutes_entry_content_frame1"],40,
    "⌨Enter the number of minutes of your call 👉\n(Please enter a number in the range from 0 to 60)",
    ("Helvetica",14,"bold"),"center","blue","white",4,"groove","left",10,10,0,0)

    createEntry(self,"self.number_of_minutes_entry",tk,self.tools_data["self.number_of_minutes_entry_content_frame1"],2,
    self.default_number_of_minute,("Helvetica",14,"bold"),"right","white","blue",4,"groove","left",5,8,0,0)

def number_of_minutes_entry_content_calculate_cost_button(self,tk):
    createButton(self,"self.calculate_cost_button",tk,self.tools_data["self.number_of_minutes_entry_content_frame2"],
    15,"👉Calculate Cost",("Helvetica",14,"bold"),"center","#34d0b3","white",4,"groove",self.calculate_cost,"left",10,5,0,0)
