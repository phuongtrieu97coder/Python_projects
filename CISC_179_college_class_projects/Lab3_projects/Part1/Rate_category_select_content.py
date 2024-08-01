def rate_category_select_content(self,tk):
    self.rate_inquiry_label = tk.Label(self.bottom_frame_rate_choosing_block,
    text="👇Select a Rate Category:",font=("Helvetica",14,"bold"),
    bg="green",fg="white",borderwidth=4,relief="groove")
    self.rate_inquiry_label.pack(side="top",ipadx=10,ipady=10,padx=20,pady=10)

    self.rate_category_select_radio_button_frame = tk.Frame(self.bottom_frame_rate_choosing_block,bg="green")
    self.rate_category_select_radio_button_frame.pack(side="top",pady=(0,10))

    rate_category_select_radio_button_content1(self,tk)
    rate_category_select_radio_button_content2(self,tk)
    rate_category_select_radio_button_content3(self,tk)

def rate_category_select_radio_button_content1(self,tk):
    self.rate_category_select_rate1_frame = tk.Frame(self.rate_category_select_radio_button_frame,bg="white")
    self.rate_category_select_rate1_frame.pack(side="top",padx=3,pady=1)

    self.rate_category_select_rate1_radio_button = tk.Radiobutton(self.rate_category_select_rate1_frame,
    fg="green",activebackground="blue",activeforeground="white",font=("Helvetica",14),
    text="Rate 1: $0.07/min",variable=self.selectChargeRateVal,value=1,command=self.rate1_select_func)
    self.rate_category_select_rate1_radio_button.pack(side="top")


def rate_category_select_radio_button_content2(self,tk):
    self.rate_category_select_rate2_frame = tk.Frame(self.rate_category_select_radio_button_frame,bg="white")
    self.rate_category_select_rate2_frame.pack(side="top",padx=3,pady=1)

    self.rate_category_select_rate2_radio_button = tk.Radiobutton(self.rate_category_select_rate2_frame,
    fg="green",activebackground="blue",activeforeground="white",font=("Helvetica",14),
    text="Rate 2: $0.12/min",variable=self.selectChargeRateVal,value=2,command=self.rate2_select_func)
    self.rate_category_select_rate2_radio_button.pack(side="top")



def rate_category_select_radio_button_content3(self,tk):
    self.rate_category_select_rate3_frame = tk.Frame(self.rate_category_select_radio_button_frame,bg="white")
    self.rate_category_select_rate3_frame.pack(side="top",padx=3,pady=1)

    self.rate_category_select_rate3_radio_button = tk.Radiobutton(self.rate_category_select_rate3_frame,
    fg="green",activebackground="blue",activeforeground="white",font=("Helvetica",14),
    text="Rate 3: $0.05/min",variable=self.selectChargeRateVal,value=3,command=self.rate3_select_func)
    self.rate_category_select_rate3_radio_button.pack(side="top")


