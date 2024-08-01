from Property_Actual_Value_entry_content import property_actual_value_entry_content

def userInputInfo(self,tk):

    self.mid_frame2_property_actual_value_entry_block = tk.Frame(self.mid_frame2,width=50,bg="black")
    self.mid_frame2_property_actual_value_entry_block.pack(side="left",padx=(130,130))
    property_actual_value_entry_content(self,tk)




