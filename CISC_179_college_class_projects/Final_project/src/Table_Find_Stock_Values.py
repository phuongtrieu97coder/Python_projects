from Load_Dow_Jones_Stocks import  get_stock_price_data

# Define the columns
column_heading_name_list = ["Stocks"]
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

