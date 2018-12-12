# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## PyBank

#The dataset is composed of two columns: `Date` and `Profit/Losses`. 

import os
import csv

#link to the csv file we are using for this homework
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#create the title for the answer print out
print ("Financial Analysis")
print ("----------------------------")

totalmonths = 0
totalrev = []
monthlychange = []
totalchange = 0
changemonths = 0
averagechange = 0
maxchange = 0
minchange = 0
maxdate = 0
mindate = 0
date =[]


with open(csvpath, "r") as csvfile:

# Initialize csv.writer and skip first row
    csvreader = csv.reader(csvfile,delimiter = ",")
    next(csvreader, None)
     
    #count the months: since there is one row per month, we can count the rows
    #calc net profit or loss: sum all rows in the "Profit/Losses" column  
    #file = csvreader
    #data = list(file)
    #totalmonths = len(data)
    #totalmonths = sum(1 for row in csvreader)
    
    for row in csvreader:
        totalmonths = totalmonths + 1
        totalrev.append(float(row[1]))
        date.append(row[0])
        
    for i in range(1,totalmonths):
        monthlychange.append(totalrev[i] - totalrev[i-1])
    
    total = int(sum(totalrev))
    totalchange = sum(monthlychange)
    changemonths = int(totalmonths) - 1   
    averagechange = round(((totalchange) / (changemonths)), 2)
        
    print (f"Total Months: {totalmonths}")
    print (f"Total: ${total}")
    print (f"Average Change: ${averagechange}")
    
    maxchange = int(max(monthlychange))
    minchange = int(min(monthlychange))
    maxdate = date[monthlychange.index(max(monthlychange))+1]
    mindate = date[monthlychange.index(min(monthlychange))+1]
    
    print (f"Greatest Increase in Profits: {maxdate} (${maxchange})")
    print (f"Greatest Decrease in Profits: {mindate} (${minchange})")
