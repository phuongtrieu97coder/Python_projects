import csv 

def get_stock_price_data():
    #In case you want turn the data from a CSV file into a list 
    userStockDataList = []
    
    try:
       with open("Dow_Jones_Stocks_February.csv",newline="") as csvFile:
        getData = csv.DictReader(csvFile,delimiter=",") 
        for rows in getData:
            userStockDataList.append(rows) 
       return userStockDataList
    
    #? Display error message if there's any error occurs 
    #? while getting the stock price data
    #? from "Dow_Jones_Stocks_February.csv" file.
    except FileNotFoundError:
        print("File not found error.\n"+\
            "Function: get_stock_price_data().\n"+\
            "File: Load_Dow_Jones_Stocks.py.\n")
        
    #? In case of any other error, display the error message
    #? with function name and file name
    except Exception as e:
        print(f"Error: {e}.\n"+\
            f"Function: get_stock_price_data().\n"+\
            f"File: Load_Dow_Jones_Stocks.py.\n")
    
