from Load_Dow_Jones_Stocks import  get_stock_price_data
#? get_stock_price_data() function from Load_Dow_Jones_Stocks.py
#? returns data that was read from
#? Dow_Jones_Stocks_February.csv file

#* This function returns a list that includes dictionaries data
#* Ex: [{“Date”:”…”, “MMM”:””},{“Date”:”…”,”MMM”:”””}]. 

#TODO: I'll use the get_stock_price_data() function
#TODO: to add data to column_heading_name_list and
#TODO: to find highest and lowest value of each stock.


#! Notice: column_heading_name_list is a list that 
#! is used across the app in different files.

#? column_heading_name_list includes data of column heading name
#? like Stocks, MMM, and so on.
column_heading_name_list = []
#TODO: I need to loop through get_stock_price_data() 
#TODO: to access dictionaries data.

#TODO: Then, adding the keys name to column_heading_name_list.

#TODO: I must make sure that column_heading_name_list
#TODO: doesn’t contain “Date” element, and begins with 'Stocks'. 


def addDataTo_column_heading_name_list():
    #! Accessing global variable column_heading_name_list
    global column_heading_name_list
    
    #? Using error handling to make sure that
    #? get_stock_price_data() function
    #? returns a list contains dictionaries data.

    #? If so, add the data to column_heading_name_list.
    try:
        if get_stock_price_data() != "" and \
        get_stock_price_data() != None:
            #! First, I want to loop through the first dictionary data
            #! in get_stock_price_data() list
            #! to get the keys name.
            for i in get_stock_price_data()[0].keys():
                #! I want to add the keys name to column_heading_name_list
                column_heading_name_list.append(i)
            #* Now column_heading_name_list contains data like this:
            #* ['Date', 'MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO']
            
            #! Remove 'Date' from column_heading_name_list
            column_heading_name_list = column_heading_name_list[1:]
           
            #! Add the 'Stocks' element to the beginning of column_heading_name_list
            column_heading_name_list.insert(0,"Stocks")
            #* Now column_heading_name_list contains data like this:
            #* ['Stocks', 'MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO']

    #? Display an error message if get_stock_price_data() function
    #? doesn't return a list contains dictionaries data
    except ValueError:
        print(f"Error: Value Error occurred. \n"+\
        f"get_stock_price_data() function doesn't return a list contains dictionaries data")
    #? In case of any other error, display the error message
    #? with function name, and file name.
    except Exception as e:
        print(f"Error: {e}. \n"+\
        f"Function: addDataTo_column_heading_name_list().\n"+\
        f"File: Table_Find_Stock_Values.py.\n")


addDataTo_column_heading_name_list()



#? find_highest_lowest_stock_values() function will 
#? find the highest and lowest stock values in February

#! Notice: This function will be used in Table_Insert_Data_Class class's 
#! insertDataToTable() method in Main_Running_Program.py file

#? This function returns 4 values through variables:
#? max_stock_value,date_of_max_stock_value,
#? min_stock_value,date_of_min_stock_value
#? representing 
#? the highest stock value, the date of the highest stock value,
#? the lowest stock value, and the date of the lowest stock value
#? return data can be 
#? Ex: (12.69,25.36,74.58,69.23)

def find_highest_lowest_stock_values(stock):
    #! stock parameter is a string value with specific 
    #! stock name like 'MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO'

    #TODO: I'll use built-in max() and min() functions
    #TODO: to find the highest and lowest stock values.

    #! max() and min() functions only work with lists.
    #TODO: I'll use a list called stock_values.
    stock_values = []
    #TODO: I'll add data to stock_values after I looped through
    #TODO: get_stock_price_data() list

    date_of_max_stock_value = 0
    date_of_min_stock_value = 0
    #TODO: I'll add a string value to date_of_max_stock_value
    #TODO: and date_of_min_stock_value
    #TODO: after I looped through get_stock_price_data() list
    

    #? Using error handling to make sure that
    #? get_stock_price_data() function
    #? returns a list contains dictionaries data.

    #? If so, find highest and lowest stock values.
    try:
        if get_stock_price_data() != "" and \
        get_stock_price_data() != None:
             #! Loop through get_stock_price_data() list
             for i in get_stock_price_data():
               #! Adding the stock values to stock_values list.
               
               #! Because i contains dictionaries data,
               #! I can get the stock values by accessing the keys name               
               stock_values.append(i[stock])

               #! Find the highest stock value 
               #! and assign the date of the highest stock value
               #! to date_of_max_stock_value
               if i[stock] == max(stock_values):
                   date_of_max_stock_value = i["Date"]
               
               #! Find the lowest stock value
               #! and assign the date of the lowest stock value
               #! to date_of_min_stock_value
               if i[stock] == min(stock_values):
                   date_of_min_stock_value = i["Date"]

             #! create max_stock_value and min_stock_value variables
             #! to store the highest and lowest stock values
             max_stock_value=max(stock_values)
             min_stock_value=min(stock_values)

             #! Return 4 values
             return max_stock_value,date_of_max_stock_value,\
             min_stock_value,date_of_min_stock_value

    #? Display an error message if get_stock_price_data() function
    #? doesn't return a list contains dictionaries data
    except ValueError:
        print(f"Error: Value Error occurred. \n"+\
        f"get_stock_price_data() function doesn't return a list contains dictionaries data")
    #? In case of any other error, display the error message
    #? with function name, and file name.
    except Exception as e:
        print(f"Error: {e}. \n"+\
        f"Function: find_highest_lowest_stock_values().\n"+\
        f"File: Table_Find_Stock_Values.py.\n")

   
