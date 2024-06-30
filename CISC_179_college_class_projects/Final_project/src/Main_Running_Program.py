from Main_GUI import MyGUI 
from Table_Find_Stock_Values import column_heading_name_list, find_highest_lowest_stock_values

class Table_Insert_Data_Class(MyGUI):

#? insertDataToTable() method inserts data to the table
#? row by row and is used in displayHighLowPrice() method.

#! Notice: I want my table have a structure like this:
#! Row1 -> |Stocks        | MMM       | AXP       | AAPL      | 
#! Row2 -> |Highest Value | $price    | $price    | $price    | 
#! Row3 -> |Date          | 2/dd/2020 | 2/dd/2020 | 2/dd/2020 | 
#! Row4 -> |Lowest Value  | $price    | $price    | $price    | 
#! Row5 -> |Date          | 2/dd/2020 | 2/dd/2020 | 2/dd/2020 | 

#! 'Highest Value' and 'Lowest Value' data must be a string
#! begins with '$' sign, followed by a floating point number
#! with 2 decimal places

    def insertDataToTable(self):
        #TODO: To insert data to the table using the tree_table widget
        #TODO: I need syntax like 
        #TODO: self.tree_table.insert("", self.tk.END, values=("something","something"))

        #! Notice that argument values inside .insert()
        #! must be assigned to a tuple and it helps 
        #! to insert data to the table row by row.

        #? Let's say I want to add content to the second row 
        #? of the table above. I may need a tuple like
        #? ("Highest Value", "$20", "$36", "$10").

        #! Because a tuple is immutable, I can't add data to it.

        #TODO: I can use a list to add data with the order structure 
        #TODO: like above with data from 
        #TODO: find_highest_lowest_stock_values() function.

        #TODO: Then, I'll convert this list to a tuple.


        #? Because I need to insert 4 rows of data, 
        #? I need 4 lists like below to store the data:
        highest_val = ["Highest Value"]
        date_highest_val = ["Date"]
        lowest_val = ["Lowest Value"]
        date_lowest_val = ["Date"]


        #? Here's the logic to add data to 4 lists above:
        #? Let's assume that I call the syntax 
        #? find_highest_lowest_stock_values("MMM").

        #? This syntax may return
        #? (52.99,"02/25/2020",12.99,"02/15/2020").

        #? After that, I'll access the value 52.99 by  
        #? using find_highest_lowest_stock_values("MMM")[0].

        #? To append to highest_val list variable, 
        #? I'll use the line: 
        #? highest_val.append(find_highest_lowest_stock_values("MMM")[0]).


        #! Warning: If our program interacts with too many stocks,
        #! It must be a tedious task to add each stock name as argument
        #! to find_highest_lowest_stock_values() function.
     

        #TODO: Because our program works with 
        #TODO: Dow_Jones_Industrial_Average_Stocks_2020.csv file,
        #TODO: I can solve the issue above by looping through
        #TODO: data from column_heading_name_list variable
        #TODO: to add specific stock name value to 
        #TODO: find_highest_lowest_stock_values() function as argument.


       #? Using error handling to make sure that column_heading_name_list
       #? returns a list contains column heading name data.

       #? If so, use some logic to add data high_val, 
       #? date_highest_val, low_val, and date_lowest_val.
        try:
           if column_heading_name_list != "" and \
           column_heading_name_list != None and len(column_heading_name_list) > 0:
            
             #! Loop through column_heading_name_list with a range begins at 1
             #! to avoid the first element 'Stocks'.
             for l in range(1,len(column_heading_name_list)):
                 
                 #! Adding data to 
                 #! highest_val, date_highest_val, lowest_val, date_lowest_val
                 #! by calling find_highest_lowest_stock_values() function with
                 #! argument column_heading_name_list[l].

               
                 #? Let's assume find_highest_lowest_stock_values("MMM") returns
                 #? (52.99,"02/25/2020",12.99,"02/15/2020").

                 #? If I want to add 52.99 to highest_val list, 
                 #? I must access find_highest_lowest_stock_values("MMM")[0].

                 #? The right logic syntax can be find_highest_lowest_stock_values(column_heading_name_list[l])[0].
                 
                 highest_val.append(f'${float(find_highest_lowest_stock_values(column_heading_name_list[l])[0]):.2f}')
                
                 date_highest_val.append(find_highest_lowest_stock_values(column_heading_name_list[l])[1])
                
                 lowest_val.append(f'${float(find_highest_lowest_stock_values(column_heading_name_list[l])[2]):.2f}')
                
                 date_lowest_val.append(find_highest_lowest_stock_values(column_heading_name_list[l])[3])
             
             #! Insert data to the table row by row
             self.tree_table.insert("", self.tk.END, values=tuple(highest_val))
             self.tree_table.insert("", self.tk.END, values=tuple(date_highest_val))
             self.tree_table.insert("", self.tk.END, values=tuple(lowest_val))
             self.tree_table.insert("", self.tk.END, values=tuple(date_lowest_val))

        #? Display an error message if column_heading_name_list
        #? doesn't return a list contains column heading name data
        except ValueError:
           print(f"Error: Value Error occurred. \n"+\
           f"column_heading_name_list variable doesn't return a list contains column heading name data")
        #? In case of any other error, display the error message
        #? with method name, class name, and file name.
        except Exception as e:
            print(f"Error: {e}. \n"+\
            f"Method: insertDataToTable().\n"+\
            f"Class: Table_Insert_Data_Class.\n"+\
            f"File: Main_Running_Program.py.\n")
        
    #? displayHighLowPrice() method displays the table in the app
    #? after the user clicks the "Dow Jones Stocks February 2020" button.

    #? This method can be used inside createButton() method
    #?  in Button_Data_Content.py file.
    def displayHighLowPrice(self):
       try:
          #! Add value to self.value 
          self.value.set(self.insertDataToTable())
          #! Display the table in my app
          self.tree_table.pack() 
       #? Display an error message if there's any error occurs while displaying the table
       except Exception as e:
          print(f"Display High Low Price Error: {e}.\n"+\
                f"Method: displayHighLowPrice().\n"+\
                f"Class: Table_Insert_Data_Class.\n"+\
                f"File: Main_Running_Program.py.\n")



if __name__ == "__main__":
    my_gui = Table_Insert_Data_Class()

