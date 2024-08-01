from Rate_category_select_content import rate_category_select_content
from Number_of_minutes_entry_content import number_of_minutes_entry_content

def userInputInfo(self,tk):
    self.bottom_frame_rate_choosing_block = tk.Frame(self.bottom_frame,width=50,bg="black")
    self.bottom_frame_rate_choosing_block.pack(side="left",padx=(40,10),pady=10)
    rate_category_select_content(self,tk)

    self.bottom_frame_number_of_minutes_entry_block = tk.Frame(self.bottom_frame,width=50,bg="black")
    self.bottom_frame_number_of_minutes_entry_block.pack(side="left",padx=(10,40))
    number_of_minutes_entry_content(self,tk)




