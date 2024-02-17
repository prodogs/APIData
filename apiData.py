import json
from turtle import stamp
import pandas as pd
import random
from datetime import datetime

def generateAllocation():
    numOfFunds = random.randint(1,5)
    allocation = []
    allocationString = "{ allocation: ["
    for i in range(0,numOfFunds):
        theFund = funds[i]
        allocationPercent = 100/numOfFunds
        allocationString += "{{'fundCode': '{}', 'percent': {}}},".format(theFund, allocationPercent)

        allocation.append({"fund": theFund, "percent": allocationPercent})

    allocationString += "]}"
    return allocationString







# Specify the path to your JSON file
file_path = "./api_account.json"


 
funds = ["AAA","BBB","CCC","DDD","EEE", "FFFF"]
outData = []
for x in range(0,1000):
    allocationString = generateAllocation()
    random_int = random.randint(1, 100000)
    current_time = datetime.now()
    
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
    apiRow = {'id': random_int, 'timeStamp ': timestamp,'type': "ALLOCATION", 'package': allocationString }
    outData.append(apiRow)  
    print(apiRow)
        
  # Convert the data to a DataFrame
df = pd.DataFrame(outData)

    # Save the DataFrame to a CSV file
df.to_csv('api_allocation.csv', index=False)
    
exit()


# create account API Activity Data
with open(file_path, "r") as file:
    # Load the JSON data
    data = json.load(file)

    # Define an empty array
    outData = []
    # Append each first name to the array
    for i in data:
        current_time = datetime.now()
        stamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        
        random_int = random.randint(1, 100000)
        apiRow = {'id': random_int, 'timeStamp ': stamp,'type': "ACCOUNT_OPEN", 'package': i }
        outData.append(apiRow)

 