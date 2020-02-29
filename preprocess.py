#!/usr/local/bin/python3

import pandas as pd

print("Lowercasing")

data = pd.read_csv("@Barclaycard_tweets.csv")

data["text"] = data["text"].str.lower()

print(data)
data.to_csv('file1.csv') 
