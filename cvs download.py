
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
filtered_data = data[data["Life expectancy, female"]>80]
count = filtered_data["Country Name"].count()
print('There are',count, 'countries')
for country in filtered_data["Country Name"]:
    print(country)
    
#Part 4 question 1
life_expectancy= 'Life expectancy, female'
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, female')
# scatter plot showing relation between GNi per capita and life expectnacy for female
#if male:
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, male')
        
#Part 4 question 2
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, female', hue= 'Region')

#Part 4 question 3 
sns.relplot( data= data, kind= "line", x= "GNI per capita", y= "Life expectancy, female", errorbar= "sd" )

#Part 4 question 4
sns.lmplot( data= data, kind= "line", x= "GNI per capita", y= "Life expectancy, female", errorbar= "sd" )

#Part 4 question 5
#exploring relationships between female life exepantcy and numerical features
sns.relplot(data= data, x= 'Internet use', y='Life expectancy, female')
#Comparison
sns.relplot(data= data, x= 'Internet use', y='Life expectancy, male')

sns.relplot( data= data, x='Physicians',y='Life expectancy, female' )
sns.relplot( data= data, x='Physicians',y='Life expectancy, male' )  
      
sns.relplot( data= data, x= 'International tourism', y='Life expectancy, female')
sns.relplot( data= data, x= 'International tourism', y='Life expectancy, male')

#all the plots between males and females have similar trends

#Is there any relationship between the Population and life expantancy?

gender = data['Life expectancy, male','Life expectancy, female']
sns.relplot( data=data, x='Population', y='Life expectancy, female', label='Female')
sns.relplot( data=data, x='Population', y='Life expectancy, male', label='Male')
sns.FacetGrid(data= data, col= 'gender')

#Any relationship between Tertiary education, female and life expectancy?

#Regions and life expectancy relationship

#Subregion and life expectancy relationship

#Women in national parliament and life expectancy relationship

#Part 4 question 6
#a)
data["emissions per capita"] = data["Greenhouse gas emissions "]/data["Population"]
sns.relplot( data=data, x='Internet use', y='emissions per capita')

#b)
filtered_data = data[data["Greenhouse gas emissions"]>0.03]
for country in filtered_data["Country Name"]:
    print(country) 

#c) 


    

 

