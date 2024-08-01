def number_of_minutes_entry_content(self,tk):
    self.number_of_minutes_entry_content_frame1 = tk.Frame(self.bottom_frame_number_of_minutes_entry_block,bg="darkblue")
    self.number_of_minutes_entry_content_frame1.pack(side="top",padx=(20,20),pady=10)
    number_of_minutes_entry_content_inquiry_label_and_entry(self,tk)

    self.number_of_minutes_entry_content_frame2 = tk.Frame(self.bottom_frame_number_of_minutes_entry_block)
    self.number_of_minutes_entry_content_frame2.pack(side="top",padx=(0,20),pady=10)
    number_of_minutes_entry_content_calculate_cost_button(self,tk)


def number_of_minutes_entry_content_inquiry_label_and_entry(self,tk):
    self.number_of_minutes_inquiry_label = tk.Label(self.number_of_minutes_entry_content_frame1,
    text="⌨Enter the number of minutes of your call 👉\n(Please enter a number in the range from 0 to 60)",
    font=("Helvetica",14,"bold"),
    bg="blue",fg="white",borderwidth=4,relief="groove")
    self.number_of_minutes_inquiry_label.pack(side="left",ipadx=10,ipady=10)

    self.number_of_minutes_entry = tk.Entry(self.number_of_minutes_entry_content_frame1,
    textvariable=self.default_number_of_minute,font=("Helvetica",14,"bold"),borderwidth=4,relief="groove",
    bg="white",fg="blue",width=2)
    self.number_of_minutes_entry.pack(side="left",ipadx=5,ipady=8)


def number_of_minutes_entry_content_calculate_cost_button(self,tk):
    self.calculate_cost_button = tk.Button(self.number_of_minutes_entry_content_frame2,
    text="👉Calculate Cost",font=("Helvetica",14,"bold"),borderwidth=4,relief="groove",
    bg="#34d0b3",fg="white",command=self.calculate_cost)
    self.calculate_cost_button.pack(side="left",ipadx=10,ipady=5)

