
from GUI_Data_and_Tools import Cost_Rate_Data,createFrame,createLabel,createRadioButton

def rate_category_select_content(self,tk,dict_data):

    createLabel(self,"self.rate_inquiry_label",tk,self.tools_data["self.bottom_frame1_rate_choosing_block"],20,
    "👇Select a Rate Category:",("Helvetica",14,"bold"),"center","green","white",4,"groove","top",10,10,20,10)

    createFrame(self,"self.rate_category_select_radio_button_frame",tk,self.tools_data["self.bottom_frame1_rate_choosing_block"],
    20,"green","top",0,0,0,(0,10))
    
    for i in range(1,len(Cost_Rate_Data)):
        rate_category_select_radio_button_content(self,i,tk,dict_data,self.displaySelectedRate)

  

def rate_category_select_radio_button_content(self,num,tk,dict_data,activeFunc):

    createFrame(self,f"self.rate_category_select_rate{num}_frame",tk,self.tools_data["self.rate_category_select_radio_button_frame"],
    40,"white","top",10,2,3,1)

    createRadioButton(self,f"self.rate_category_select_rate{num}_radio_button",tk,self.tools_data[f"self.rate_category_select_rate{num}_frame"],
    f"Rate {num}: ${dict_data[f"row{num+1}"][1][1:]}/min",("Helvetica",14),"green","blue","white",self.selectChargeRateVal,num,activeFunc,"top")

 

 