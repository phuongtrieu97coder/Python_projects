from Main_GUI import MyGUI 
from Table_Find_Stock_Values import column_heading_name_list, find_highest_lowest_stock_values

class Table_Insert_Data_Class(MyGUI):

        # Insert data
    def insertDataToTable(self):
        list1 = ["Highest Value","Date","Lowest Value","Date"]
        highest_val = [list1[0]]
        date_highest_val = [list1[1]]
        lowest_val = [list1[2]]
        date_lowest_val = [list1[3]]

        for l in range(1,len(column_heading_name_list)):
            highest_val.append(f'${float(find_highest_lowest_stock_values(column_heading_name_list[l])[0]):.2f}')
            date_highest_val.append(find_highest_lowest_stock_values(column_heading_name_list[l])[1])
            lowest_val.append(f'${float(find_highest_lowest_stock_values(column_heading_name_list[l])[2]):.2f}')
            date_lowest_val.append(find_highest_lowest_stock_values(column_heading_name_list[l])[3])
        self.tree_table.insert("", self.tk.END, values=tuple(highest_val))
        self.tree_table.insert("", self.tk.END, values=tuple(date_highest_val))
        self.tree_table.insert("", self.tk.END, values=tuple(lowest_val))
        self.tree_table.insert("", self.tk.END, values=tuple(date_lowest_val))
        

    def displayHighLowPrice(self):
       self.value.set(self.insertDataToTable())
       self.tree_table.pack() #Display the table in my app



if __name__ == "__main__":
    my_gui = Table_Insert_Data_Class()

