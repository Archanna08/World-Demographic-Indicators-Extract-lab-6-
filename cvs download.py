
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("wdi_wide.csv")

#Part 3 size of column (testing)

data.info("Column")

#Part 3 question 3
data.info("Column")
# answer for Physicians = 10 did not report how many physicians they have
# answer for Populations = 0

#Part 3 question 4 print unique values
print(data.nunique())

#Part 3 question 5
print(data.describe())
#it gives the number of rows and columns
#count, mean, std,min,max

#Part 3 question 6
data["GNI per capita"] = data["GNI"]/data["Population"]
data["GNI per capita"]= data["GNI per capita"].round(2)

#Part 3 question 7
#a)
print(data["Region"].value_counts())
#Region
#Africa      54 countries
#Asia        50
#Europe      47
#Americas    46
#Oceania     19

#b)
print(data["High Income Economy"].value_counts())
#67 countries

#Part 3 question 8
print(pd.crosstab(data["High Income Economy"],data["Region"]))

#Part 3 question 9
filtered_data = data[data["Life expectancy,female"]>80]

count = filtered_data["Country"]
print(count)





 

