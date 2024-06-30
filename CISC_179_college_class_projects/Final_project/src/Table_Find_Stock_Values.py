from Load_Dow_Jones_Stocks import  get_stock_price_data

# Define the columns
column_heading_name_list = ["Stocks"]
#The purpose of this list is to use across the app
# in different files to handle 
# a list data of column heading name
# like Stocks, MMM, and so on.

# This list would be used to interact with data
# from Dow_Jones_Stocks_February.csv file later
# to find highest and lowest value of each stock.

#I must pay attention to the data that was created 
#after the Python syntax with open() read data from
#the csv file would be in structure like a list that 
#contains many dictionaries like [{“Date”:”…”, “MMM”:””},{“Date”:”…”,”MMM”:”””}]. 
#So, I would need to use some algorithm to loop through this data 
#and add the properties’ keys to column_heading_name_list in a way
#that doesn’t contain “Date” element. 

stock_list_contains_dict_data = get_stock_price_data()


list_include_date_key = []
#list_include_date_key must contain
# ['Date', 'MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO']

stock_first_dict_data = stock_list_contains_dict_data[0]
for g in stock_first_dict_data.keys():
    list_include_date_key.append(g)

column_heading_name_list =list_include_date_key[1:]
column_heading_name_list.insert(0,"Stocks")
#'Stocks','MMM', 'AXP', 'AAPL', 'BA', 'CAT', 'CVX', 'CSCO', 'KO']


#find highest and lowest stock values in February
def find_highest_lowest_stock_values(stock):
    stock_values = []
    date_of_max_stock_value = 0
    date_of_min_stock_value = 0

    for i in stock_list_contains_dict_data:
      stock_values.append(i[stock])
      if i[stock] == max(stock_values):
          date_of_max_stock_value = i["Date"]
      if i[stock] == min(stock_values):
          date_of_min_stock_value = i["Date"]
    max_stock_value=max(stock_values)
    min_stock_value=min(stock_values)
    return max_stock_value,date_of_max_stock_value,min_stock_value,date_of_min_stock_value

