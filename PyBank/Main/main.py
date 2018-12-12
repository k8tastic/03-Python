# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## PyBank

#Dependencies

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
date =[]

with open(csvpath, "r") as csvfile:

# Initialize csv.writer and skip first row
    csvreader = csv.reader(csvfile,delimiter = ",")
    next(csvreader, None)
     
    #count the months and calc net profit or loss 
    
    for row in csvreader:
        totalmonths = totalmonths + 1
        totalrev.append(float(row[1]))
        date.append(row[0])
    
    #calculate the ave monthly change and max, min    
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

#Export results into a new text file
f= open("budget_data.txt","w+")
f= open("budget_data.txt","a+")
f.write("Financial Analysis"  + "\n") 
f.write("----------------------------"  + "\n")     
f.write(f"Total Months: {totalmonths}"  + "\n")
f.write(f"Total: ${total}"  + "\n")
f.write(f"Average Change: ${averagechange}" + "\n")
f.write(f"Greatest Increase in Profits: {maxdate} (${maxchange})" + "\n")
f.write(f"Greatest Decrease in Profits: {mindate} (${minchange})") 
f.close()   