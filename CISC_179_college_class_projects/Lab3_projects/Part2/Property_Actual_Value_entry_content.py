def property_actual_value_entry_content(self,tk):
    self.property_actual_value_entry_content_frame1 = tk.Frame(self.mid_frame2_property_actual_value_entry_block,bg="darkblue")
    self.property_actual_value_entry_content_frame1.pack(side="top",padx=(20,20),pady=10)
    property_actual_value_entry_content_inquiry_label_and_entry(self,tk)

    self.property_actual_value_entry_content_frame2 = tk.Frame(self.mid_frame2_property_actual_value_entry_block)
    self.property_actual_value_entry_content_frame2.pack(side="top",padx=(0,20),pady=10)
    property_actual_value_entry_content_calculate_assessment_value_and_property_tax_button(self,tk)


def property_actual_value_entry_content_inquiry_label_and_entry(self,tk):
    self.property_actual_value_inquiry_label = tk.Label(self.property_actual_value_entry_content_frame1,
    text="⌨Enter the actual value of a property ($) 👉 ",
    font=("Helvetica",14,"bold"),
    bg="green",fg="white",borderwidth=4,relief="groove")
    self.property_actual_value_inquiry_label.pack(side="left",ipadx=10,ipady=10)

    self.property_actual_value_entry = tk.Entry(self.property_actual_value_entry_content_frame1,
    textvariable=self.user_property_actual_value,font=("Helvetica",14,"bold"),
    justify="right",borderwidth=4,relief="groove",
    bg="white",fg="blue",width=20)
    self.property_actual_value_entry.pack(side="left",ipadx=5,ipady=8)


def property_actual_value_entry_content_calculate_assessment_value_and_property_tax_button(self,tk):
    self.calculate_assessment_value_and_property_tax_button = tk.Button(self.property_actual_value_entry_content_frame2,
    text="👉Calculate Assessment Value and Property Tax",font=("Helvetica",14,"bold"),borderwidth=4,relief="groove",
    bg="#34d0b3",fg="white",command=self.calculate_assessment_value_and_property_tax)
    self.calculate_assessment_value_and_property_tax_button.pack(side="left",ipadx=10,ipady=5)

