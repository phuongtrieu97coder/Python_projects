Cost_Rate_Data = {
    "row1":["Rate Category","Rate per Minute"],
    "row2":["Daytime (6:00 a.m. through 5:59 p.m.)","$0.07"],
    "row3":["Evening (6:00 p.m. through 11:59 p.m.)","$0.12"],
    "row4":["Off-Peak (midnight through 5:59 a.m.)","$0.05"]
}

def createFrame(self,var_name,tk,locate,
widthVal,
bgVal,
sideVal,
ipadxVal,ipadyVal,padxVal,padyVal):
    
    globals()[var_name] = tk.Frame(locate,width=widthVal,bg=bgVal)
    
    globals()[var_name].pack(side=sideVal,
    ipadx=ipadxVal,ipady=ipadyVal,
    padx=padxVal,pady=padyVal)
    
    self.tools_data[var_name] = globals()[var_name]

def createLabel(self,var_name,tk,locate,
widthVal,
textVal,fontVal,anchorVal,
bgVal,fgVal,
borderwidth_Val,reliefVal,
sideVal,
ipadxVal,ipadyVal,padxVal,padyVal):
    
    globals()[var_name] = tk.Label(locate,width=widthVal,
    text=textVal,font=fontVal,anchor=anchorVal,
    borderwidth=borderwidth_Val,relief=reliefVal,
    bg=bgVal,fg=fgVal)
    
    globals()[var_name].pack(side=sideVal,
    ipadx=ipadxVal,ipady=ipadyVal,
    padx=padxVal,pady=padyVal)
    
    self.tools_data[var_name] = globals()[var_name]



def createEntry(self,var_name,tk,locate,
widthVal,
textvariable_Val,fontVal,justifyVal,
bgVal,fgVal,
borderwidth_Val,reliefVal,
sideVal,
ipadxVal,ipadyVal,padxVal,padyVal):
    
    globals()[var_name] = tk.Entry(locate,width=widthVal,
    textvariable=textvariable_Val,font=fontVal,justify=justifyVal,
    borderwidth=borderwidth_Val,relief=reliefVal,
    bg=bgVal,fg=fgVal)
    
    globals()[var_name].pack(side=sideVal,
    ipadx=ipadxVal,ipady=ipadyVal,
    padx=padxVal,pady=padyVal)
    
    self.tools_data[var_name] = globals()[var_name]



def createButton(self,var_name,tk,locate,
widthVal,
textVal,fontVal,anchorVal,
bgVal,fgVal,
borderwidth_Val,reliefVal,
commandVal,
sideVal,
ipadxVal,ipadyVal,padxVal,padyVal):
    
    globals()[var_name] = tk.Button(locate,width=widthVal,
    text=textVal,font=fontVal,anchor=anchorVal,
    borderwidth=borderwidth_Val,relief=reliefVal,
    bg=bgVal,fg=fgVal,command=commandVal)
    
    globals()[var_name].pack(side=sideVal,
    ipadx=ipadxVal,ipady=ipadyVal,
    padx=padxVal,pady=padyVal)
    
    self.tools_data[var_name] = globals()[var_name]



def createRadioButton(self,var_name,tk,locate,
textVal,fontVal,
fgVal,activebackground_val,
activeforeground_val,
variableVal,value_val,
commandVal,sideVal):
    
    globals()[var_name] = tk.Radiobutton(locate,
    text=textVal,font=fontVal,
    fg=fgVal,activebackground=activebackground_val,
    activeforeground=activeforeground_val,
    variable=variableVal,value=value_val,
    command=commandVal)
    
    globals()[var_name].pack(side=sideVal)
    
    self.tools_data[var_name] = globals()[var_name]

