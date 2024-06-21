import csv 

def get_stock_price_data():
    #In case you want turn the data from a CSV file into a list 
    userStockDataList = []
    with open("Dow_Jones_Stocks_February.csv",newline="") as csvFile:
     getData = csv.DictReader(csvFile,delimiter=",") 
     for rows in getData:
         userStockDataList.append(rows) 
    return userStockDataList
