from GUI_Data_and_Tools import createFrame
from Rate_category_select_content import rate_category_select_content
from Number_of_minutes_entry_content import number_of_minutes_entry_content

def Bottom_Frame1(self,tk,locate):
    createFrame(self,"self.bottom_frame1",tk,locate,60,"darkblue","top",0,0,0,0)

def Bottom_Frame1_Rate_Choosing_Block(self,tk,locate):
    createFrame(self,"self.bottom_frame1_rate_choosing_block",tk,locate,40,"black","left",0,0,(40,10),10)

def Bottom_Frame1_Number_Of_Minutes_Entry_Block(self,tk,locate):
    createFrame(self,"self.bottom_frame1_number_of_minutes_entry_block",tk,locate,50,"black","left",0,0,(10,40),0)

def userInputInfo(self,tk,dict_data):
    rate_category_select_content(self,tk,dict_data)
    number_of_minutes_entry_content(self,tk)




