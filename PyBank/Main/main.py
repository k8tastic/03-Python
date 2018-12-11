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

Profit_Losses = []
monthlychange = []

with open(csvpath, "r") as csvfile:

# Initialize csv.writer
    csvreader = csv.reader(csvfile,delimiter = ",")
    next(csvreader, None)
     
    #count the months: since there is one row per month, we can count the rows
    #calc net profit or loss: sum all rows in the "Profit/Losses" column  
    row_count = len(row[1])
    total = sum(int(row[1]) for row in csvreader)
    
    print (f"Total Months: {row_count}")
    print (f"Total: {total}")
    
    #calc average month to month change: first calc change for each month, then take average  

#    for i in range(2,len(row[1]):
#        monthlychange.append(Profit_Losses[i] - Profit_Losses[i-1])   
#        print (sum(monthlychange))
#        
#        avg_monthlychange = (sum(monthlychange)/row_count)

#        max_monthlychange = max(monthlychange)

#        min_monthlychange = min(monthlychange)

#        max_monthlychange_date = str(date[monthlychange.index(max(monthlychange))])
#        min_monthlychange_date = str(date[monthlychange.index(min(monthlychange))])
      
    #print (f"Average Change: {avg_monthlychange}")
    #print (f"Greatest Increase in Profits: str{max_monthlychange_date}, str{max_monthlychange}")
    #print (f"Greatest Decrease in Profits: str{min_monthlychange_date}, str{min_monthlychange}")
    
  # The average change in "Profit/Losses" between months over the entire period
  # The greatest increase in profits (date and amount) over the entire period
  # The greatest decrease in losses (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:

  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
  

# In addition, your final script should both print the analysis to the terminal 
# and export a text file with the results.