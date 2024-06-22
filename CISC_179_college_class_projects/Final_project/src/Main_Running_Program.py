import Main_GUI as MPM
from Table_Find_Stock_Values import find_highest_lowest_stock_values


class Table_Insert_Data_Class(MPM.MyGUI):

    def stylingTabel(self):

        # Format the columns
        self.tree_table.column("#0", width=0, stretch=self.tk.NO)
        for col in range(len(self.list_of_columns)):
            self.tree_table.column(self.tree_table["columns"][col], anchor=self.tk.W, width=150)

        # Create headings
        self.tree_table.heading("#0", text="", anchor=self.tk.W)
        for col_head in range(len(self.list_of_columns)):
            self.tree_table.heading(f"Column {col_head+1}",text=self.list_of_columns[col_head], anchor=self.tk.W)


        # Insert data
    def insertDataToTable(self):
        list1 = ["Highest Value","Date","Lowest Value","Date"]
        highest_val = [list1[0]]
        date_highest_val = [list1[1]]
        lowest_val = [list1[2]]
        date_lowest_val = [list1[3]]

        for l in range(1,len(self.list_of_columns)):
            highest_val.append(f'${float(find_highest_lowest_stock_values(self.list_of_columns[l])[0]):.2f}')
            date_highest_val.append(find_highest_lowest_stock_values(self.list_of_columns[l])[1])
            lowest_val.append(f'${float(find_highest_lowest_stock_values(self.list_of_columns[l])[2]):.2f}')
            date_lowest_val.append(find_highest_lowest_stock_values(self.list_of_columns[l])[3])
        self.tree_table.insert("", self.tk.END, values=tuple(highest_val))
        self.tree_table.insert("", self.tk.END, values=tuple(date_highest_val))
        self.tree_table.insert("", self.tk.END, values=tuple(lowest_val))
        self.tree_table.insert("", self.tk.END, values=tuple(date_lowest_val))
        

    def displayHighLowPrice(self):
       self.value.set(self.insertDataToTable())
       self.stylingTabel()
       self.tree_table.pack() #Display the table in my app
       #return



if __name__ == "__main__":
    my_gui = Table_Insert_Data_Class()

