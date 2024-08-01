def table1_column1_contents(self,tk):
        self.table1_column1_row1 = tk.Label(self.mid_frame_table1_column1, 
        text="Rate Category",anchor="w",
        font=("Helvetica",12,"bold"),bg="white",fg="black",width=45)
        self.table1_column1_row1.pack(side="top",ipadx=10,ipady=10,padx=2,pady=2)

        self.table1_column1_row2 = tk.Label(self.mid_frame_table1_column1, 
        text="Daytime (6:00 a.m. through 5:59 p.m.)",anchor="w",
        font=("Helvetica",12),bg="white",fg="black",width=50)
        self.table1_column1_row2.pack(side="top",ipadx=10,ipady=10,padx=0,pady=2)
       
        self.table1_column1_row3 = tk.Label(self.mid_frame_table1_column1, 
        text="Evening (6:00 p.m. through 11:59 p.m.)",anchor="w",
        font=("Helvetica",12),bg="white",fg="black",width=50)
        self.table1_column1_row3.pack(side="top",ipadx=10,ipady=10,padx=2,pady=2)
       
        self.table1_column1_row4 = tk.Label(self.mid_frame_table1_column1, 
        text="Off-Peak (midnight through 5:59 a.m.)",anchor="w",
        font=("Helvetica",12),bg="white",fg="black",width=50)
        self.table1_column1_row4.pack(side="top",ipadx=10,ipady=10,padx=2,pady=2)



def table1_column2_contents(self,tk):
        self.table1_column2_row1 = tk.Label(self.mid_frame_table1_column2, 
        text="Rate per Minute",anchor="w",
        font=("Helvetica",12,"bold"),bg="white",fg="black",width=45)
        self.table1_column2_row1.pack(side="top",ipadx=10,ipady=10,padx=2,pady=2)

        self.table1_column2_row2 = tk.Label(self.mid_frame_table1_column2, 
        text="$0.07",anchor="w",
        font=("Helvetica",12),bg="white",fg="black",width=50)
        self.table1_column2_row2.pack(side="top",ipadx=10,ipady=10,padx=0,pady=2)
       
        self.table1_column2_row3 = tk.Label(self.mid_frame_table1_column2, 
        text="$0.12",anchor="w",
        font=("Helvetica",12),bg="white",fg="black",width=50)
        self.table1_column2_row3.pack(side="top",ipadx=10,ipady=10,padx=2,pady=2)
       
        self.table1_column2_row4 = tk.Label(self.mid_frame_table1_column2, 
        text="$0.05",anchor="w",
        font=("Helvetica",12),bg="white",fg="black",width=50)
        self.table1_column2_row4.pack(side="top",ipadx=10,ipady=10,padx=2,pady=2)


