from GUI_Data_and_Tools import Cost_Rate_Data,createFrame,createLabel

def Mid_Frame1(self,var_name,tk,locate):
    createFrame(self,var_name,tk,locate,100,"darkblue","top",0,0,0,0)

def Mid_Frame1_Table1(self,var_name,tk,locate):
    createFrame(self,var_name,tk,locate,80,"green","top",0,0,20,0)

def Table1_Rows(self,tk,locate):
    for v_count in range(len(Cost_Rate_Data)): 
        createFrame(self,f"self.table1_row{v_count+1}",tk,locate,80,"green","top",0,0,0,0)

def Table1_Cells_Content(self,tk,locate):
    for v_count in range(len(Cost_Rate_Data["row1"])): 
       createLabel(self,f"self.table1_row1_cell{v_count+1}",tk,locate["self.table1_row1"],45,
       Cost_Rate_Data["row1"][v_count],("Helvetica",12,"bold"),"w","white","black",0,"solid","left",10,10,2,2)

#I want the style of each cell following after the first row 
#to be the same
    for c in range(1,len(Cost_Rate_Data)):
        for v_count in range(len(Cost_Rate_Data[f"row{c+1}"])): 
           createLabel(self,f"self.table1_row{c+1}_cell{v_count+1}",tk,locate[f"self.table1_row{c+1}"],50,
           Cost_Rate_Data[f"row{c+1}"][v_count],("Helvetica",12),"w","white","black",0,"solid","left",10,10,2,2)


#In case I want to adjust the style of each cell following after the first row       
#    for v_count in range(len(Cost_Rate_Data["row2"])): 
#       createLabel(self,f"self.table1_row2_cell{v_count+1}",tk,locate["table1_row2"],
#       50,
#       Cost_Rate_Data["row2"][v_count],
#       ("Helvetica",12),"w",
#       "white","black",
#       0,"solid",
#       "left",
#       10,10,2,2)
#    for v_count in range(len(Cost_Rate_Data["row3"])): 
#       createLabel(self,f"self.table1_row3_cell{v_count+1}",tk,locate["table1_row3"],
#       50,
#       Cost_Rate_Data["row3"][v_count],
#       ("Helvetica",12),"w",
#       "white","black",
#       0,"solid",
#       "left",
#       10,10,2,2)
#    for v_count in range(len(Cost_Rate_Data["row4"])): 
#       createLabel(self,f"self.table1_row4_cell{v_count+1}",tk,locate["table1_row4"],
#       50,
#       Cost_Rate_Data["row4"][v_count],
#       ("Helvetica",12),"w",
#       "white","black",
#       0,"solid",
#       "left",
#       10,10,2,2)



