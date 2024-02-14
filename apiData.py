import json
from turtle import stamp
import pandas as pd
import random
from datetime import datetime

def generateAllocation():
    numOfFunds = random.randint(1,5)
    allocation = []
    for i in range(0,numOfFunds):
        theFund = funds[i]
        allocationPercent = 100/numOfFunds
        allocation.append({"fund": theFund, "percent": allocationPercent})

    allocationJson = json.dumps(allocation)
    return allocationJson

# Specify the path to your JSON file
file_path = "./api_account.json"

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

  
    funds = ["AAA","BBB","CCC","DDD","EEE", "FFFF"]

    for x in range(0,1000):
        allocation = []
        allocation.append(generateAllocation())
        allocationJson = { "account" : "XXXX", "allocation" : allocation }
        random_int = random.randint(1, 100000)
        apiRow = {'id': random_int, 'timeStamp ': stamp,'type': "ALLOCATION", 'package': allocationJson }
        outData.append(apiRow)  
        print(apiRow)
        
        
  # Convert the data to a DataFrame
    df = pd.DataFrame(outData)

    # Save the DataFrame to a CSV file
    df.to_csv('api_data.csv', index=False)
    