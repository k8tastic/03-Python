# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 12:27:56 2018

@author: katef_000
"""

import os
import csv

#link to the csv file we are using for this homework
csvpath = os.path.join("election_data.csv")

#create the title for the answer print out
print ("Election Results")
print ("----------------------------")

totalvotes = int

with open(csvpath, "r") as csvfile:

# Initialize csv.writer and skip first row
    csvreader = csv.reader(csvfile,delimiter = ",")
    next(csvreader, None)
     
    #count the votes: since there is one row per vote, we can count the rows
    #calc net profit or loss: sum all rows in the "Profit/Losses" column  
    
    data = list(csvreader)
    totalvotes = len(data)
   
    
    # Populate a new dictionary with the candiate name and their vote total    
    candidatelist = {}
    
    for row in data:
        if row[2] not in candidatelist:
            candidatelist[row[2]] = 1
        else:
            vote = candidatelist.get(row[2]) + 1
            candidatelist[row[2]] = vote
    
    #Print all results       
    print (f"Total Votes: {totalvotes}")
    print ("----------------------------")

    #Add calculation for percent of votes per candidate
    for key in candidatelist:
        percent = candidatelist[key]/totalvotes*100
        percent = round(percent, 3)
        print (f"{key}: {percent}% ({candidatelist[key]})")   
        
    print ("----------------------------") 
    
    #Find the winner of the election
    highvote = 0
    winner = str
    for key in candidatelist:
        if candidatelist[key] > highvote:
            highvote = candidatelist[key]
            winner = key
            
    print (f"Winner: {winner}")
    print ("----------------------------") 
    
#Export results into a new text file
f= open("election_results.txt","w+")
f= open("election_results.txt","a+")
f.write("Election Results"  + "\n") 
f.write("----------------------------"  + "\n")     
f.write(f"Total Votes: {totalvotes}"  + "\n")
f.write("----------------------------"  + "\n")
for key in candidatelist:
    percent = candidatelist[key]/totalvotes*100
    percent = round(percent, 3)
    f.write(f"{key}: {percent}% ({candidatelist[key]})"  + "\n")
f.write("----------------------------"  + "\n")
f.write(f"Winner: {winner}" + "\n")
f.write("----------------------------") 
f.close()   
 