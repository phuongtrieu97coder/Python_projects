from GUI_Data_and_Tools import createFrame,createLabel

def Top_Frame(self,var_name,tk,locate):
    createFrame(self,var_name,tk,locate,100,"aqua","top",0,0,0,0)

def Title_Label(self,var_name,tk,locate):
    createLabel(self,var_name,tk,locate,56,"Telephone Call Cost (Long-distance Charge Rates)",("Helvetica",20,"bold"),
    "center","blue","white",0,"solid","top",20,10,6,6)