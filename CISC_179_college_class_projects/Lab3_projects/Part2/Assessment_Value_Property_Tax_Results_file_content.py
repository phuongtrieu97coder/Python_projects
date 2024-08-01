def Assessment_Value_Property_Tax_Results_content(self,tk):
    self.assessment_value_results_content_frame1 = tk.Frame(self.bottom_frame_Assessment_Value_Property_Tax_Results_block,bg="darkblue")
    self.assessment_value_results_content_frame1.pack(side="left",padx=(20,20),pady=10)
    assessment_value_results_content_title_label_and_result_label(self,tk)

    self.property_tax_results_content_frame1 = tk.Frame(self.bottom_frame_Assessment_Value_Property_Tax_Results_block,bg="darkblue")
    self.property_tax_results_content_frame1.pack(side="left",padx=(20,20),pady=10)
    property_tax_results_content_title_label_and_result_label(self,tk)

   

def assessment_value_results_content_title_label_and_result_label(self,tk):
    self.assessment_value_title_label = tk.Label(self.assessment_value_results_content_frame1,
    text="💸Assessment Value ($): ",
    font=("Helvetica",14,"bold"),
    bg="#57C521",fg="white",borderwidth=4,relief="groove")
    self.assessment_value_title_label.pack(side="left",ipadx=10,ipady=10)

    self.assessment_value_result_label = tk.Label(self.assessment_value_results_content_frame1,
    textvariable=self.assessment_value,font=("Helvetica",14,"bold"),
    anchor="e",borderwidth=4,relief="groove",
    bg="white",fg="blue",width=15)
    self.assessment_value_result_label.pack(side="left",ipadx=5,ipady=8)


def property_tax_results_content_title_label_and_result_label(self,tk):
    self.property_tax_title_label = tk.Label(self.property_tax_results_content_frame1,
    text="💸Property Tax ($): ",
    font=("Helvetica",14,"bold"),
    bg="#1353A7",fg="white",borderwidth=4,relief="groove")
    self.property_tax_title_label.pack(side="left",ipadx=10,ipady=10)

    self.property_tax_value_result_label = tk.Label(self.property_tax_results_content_frame1,
    textvariable=self.property_tax_value,font=("Helvetica",14,"bold"),
    anchor="e",borderwidth=4,relief="groove",
    bg="white",fg="blue",width=15)
    self.property_tax_value_result_label.pack(side="left",ipadx=5,ipady=8)

