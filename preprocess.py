#!/usr/local/bin/python3

import pandas as pd
import nltk
nltk.download('stopwords')

#1 ########Lowercasing##########
print("1")
print("Lowercasing")

data = pd.read_csv("@Barclaycard_tweets.csv")

data["text"] = data["text"].str.lower()

print(data) #Printing
data.to_csv('file1.csv') 

#2 ########Dropping unnecessary columns##############
print ("2")
print("Dropping the created at column")
del data['created_at']

print("Dropping the id column")
del data['id']

print(data) #Printing

data.to_csv('file2.csv')

#3 ###########Stop Word Removal######################

print("3")
print("Removing Stop Words")

from nltk.corpus import stopwords

stop = stopwords.words('english')

df = pd.read_table('file2.csv', error_bad_lines = False, header = None , names = ['text'], na_filter= True)
print(df)

df['cleaned'] = list(map(lambda x: x.lower().split(), df.text))
print(df)
df.to_csv('file3.csv')

df['filtered'] = list(map(lambda line: list(filter(lambda word: word not in stop, line)), df.cleaned))
df.to_csv('textsanssw.csv')

