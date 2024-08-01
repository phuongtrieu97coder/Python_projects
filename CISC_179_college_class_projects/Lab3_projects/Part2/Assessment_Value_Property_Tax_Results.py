from Assessment_Value_Property_Tax_Results_file_content import Assessment_Value_Property_Tax_Results_content

def Assessment_Value_Property_Tax_Results_func(self,tk):

    self.bottom_frame_Assessment_Value_Property_Tax_Results_block = tk.Frame(self.bottom_frame,width=50,bg="black")
    self.bottom_frame_Assessment_Value_Property_Tax_Results_block.pack(side="left",padx=(12,12),pady=(0,15))
    Assessment_Value_Property_Tax_Results_content(self,tk)




