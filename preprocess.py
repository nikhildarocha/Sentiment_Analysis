#!/usr/local/bin/python3

import pandas as pd


########Lowercasing##########
print("Lowercasing")

data = pd.read_csv("@Barclaycard_tweets.csv")

data["text"] = data["text"].str.lower()

print(data) #Printing
data.to_csv('file1.csv') 

########Dropping unnecessary columns##############

print("Dropping the created at column")
del data['created_at']

print("Dropping the id column")
del data['id']

print(data) #Printing

data.to_csv('file2.csv')

