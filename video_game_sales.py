# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:08:55 2020

@author: ThinkPad X1
"""

"""
Author: Angela Vaynshteyn
Date: 9/5/2019

Assignment 1
Group partner: Nawal

"""
#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data
my_data = pd.read_csv("vgsales.csv")
my_data.head()

# 1) How many instances are in the data?
print("")
print("Data size: ",my_data.size)
print(" ")

# 2) How many attributes? (features)
print("Number of attributes: ",my_data.shape)
print("")

# 4) Any obvious outliers?
data_no_character = my_data.drop(["Name","Platform","Year","Genre","Publisher"], axis=1)
new_header = data_no_character.iloc[0]
data_no_character = data_no_character[1:]
data_no_character.columns = new_header
columns = list(data_no_character)
# Making a For loop that checks for outliers in the sales. It checks 3 columns
for z in columns:
    # finding mean & standard variation for the combined sales
    NA_mean = my_data.loc[:,"NA_Sales"].mean()
    EU_mean = my_data.loc[:,"EU_Sales"].mean()
    JP_mean = my_data.loc[:,"JP_Sales"].mean()
    melt_all_sales = pd.melt(my_data[['NA_Sales','EU_Sales','JP_Sales']])
    all_sales_mean = np.mean(melt_all_sales)
    all_sales_std = np.std(melt_all_sales)
    z_score = (z - all_sales_mean) / all_sales_std
    if any(z_score) > 3:
        print(z)
    else:
        all(z_score) < 3
        print("No outliers")
        continue

# 5) Include at least 5 different plots
# 5.1) PRINT SALES BY YEAR
yearly_grouped = my_data.groupby(by="Year")
#NA_sales_mean = (yearly_grouped['NA_Sales']).mean().plot(figsize=(10,10))
#EU_sales_mean = (yearly_grouped['EU_Sales']).mean().plot(figsize=(10,10))
#JP_sales_mean = (yearly_grouped['JP_Sales']).mean().plot(figsize=(10,10))
all_sales_mean = (yearly_grouped['NA_Sales','EU_Sales','JP_Sales']).mean().plot(figsize=(10,10))
plt.title('Average Sales by Year')
plt.xlabel('Year')
plt.ylabel('Average Sales (millions)')
plt.show()

# 5.2) PRINT SALES BY GENRE
genre_grouped = my_data.groupby(by="Genre")
all_sales_mean = (genre_grouped['NA_Sales','EU_Sales','JP_Sales']).mean().plot(kind='bar',figsize=(10,10))
plt.title('Average Sales by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Sales (millions)')
plt.show()

# print(my_data.groupby('Genre').head())
# fig = plt.figure(figsize=(10,10))
# plt.scatter(my_data['NA_Sales'],my_data['EU_Sales'])
# plt.show()

# 5.3) PRINT SALE BY PUBLISHER
import random
random.seed(a=52, version = 2) #trying to stabilize the random sample
index_publisher = my_data.sample(n=20,replace=False)
publisher_grouped = index_publisher.groupby(["Publisher"])
all_sales_mean = (publisher_grouped['NA_Sales','EU_Sales','JP_Sales']).mean().plot(kind='barh',figsize=(10,10))
plt.title('Average Sales by Publisher')
plt.ylabel('Publisher', fontsize=7)
plt.xlabel('Average Sales (millions)', fontsize=10)
plt.show()

# 5.4) PRINT SALES BY PLATFORM
random.seed(a=52, version = 2) #trying to stabilize the random sample
index_platform = my_data.sample(n=20,replace=False)
platform_grouped = index_platform.groupby(by="Platform")
all_sales_mean = (platform_grouped['NA_Sales','EU_Sales','JP_Sales']).mean().plot(kind = 'bar',figsize=(10,10))
plt.title('Average Sales by Platform')
plt.xlabel('Platform', fontsize=10)
plt.ylabel('Average Sales (millions)', fontsize=10)
plt.show()

# 5.5) PRINT SALES BY NAME
index_name = my_data.iloc[0:10] #top 10 games
name_grouped = index_name.groupby(by="Name")
all_sales_mean = (name_grouped['NA_Sales','EU_Sales','JP_Sales']).mean().plot(kind = 'barh', figsize=(10,10))
plt.title('Average Sales by Name')
plt.xlabel('Name',fontsize=7)
plt.ylabel('Average Sales (millions)')
plt.show()

# 6) PRINT YEAR BY GENRE
# print(my_data.groupby(['Year','Genre']).size())
my_data.groupby(['Year','Genre']).size().unstack(fill_value=0).plot(kind='bar',figsize=(10,10))
plt.show()


# IGNORE BELOW THIS
#my_data = my_data.to_numpy()
#print(my_data)
# CAN I KEEP JUST THE TOP 15 PUBLISHERS INSTEAD OF ALL OF THEM?
# OR HOW CAN I WRITE CODE THAT AUTOMATES THE RE-NUMBERING PROCESS
# HOW TO WRITE CODE ON MULTIPLE LINES?
# ask for 25 random publishers
#import random
#r#andom.seed(a=52, version = 2) #trying to stabilize the random sample
#random_subset = my_data.sample(n=25)
#print(random_subset)

#print("Dropping & renaming data")
# drop the 25 random publishers
#my_data.drop(index=my_data.index.difference(["Nintendo","Take-Two Interactive",\
#"Acclaim Entertainment","Microsoft Game Studios","Idea Factory","Alchemist","Capcom",\
#"Minato Station","Electronic Arts","THQ","Activision","Avanquest","NEC",\
#"Konami Digital Entertainment","Namco Bandai Games","Sega","505 Games","Vivenda Games",\
#"Take-Two Interactive","Atlus","Square Enix","Devolver Digital","20th Century Fox Video Games",\
#,"Falcom Corporation"]))
# make a dictionary for the publishers to numbers
#Scleanup_pub = {"Publisher": {"Nintendo":0,""}}
#changing publishers to numbers
