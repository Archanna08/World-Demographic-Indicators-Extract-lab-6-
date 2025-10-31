
#World Demographic Indicator Extract
#Author: Archanna Nagesan
#Due date: 31/10/2025
#Progamming in science- 420-SN1-RE

#This Python script uses seaborn and its functions to explore and plot graphs on the dataset World Demographic Indicator Extract.

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
#count, mean, std,min,max, quartile (Q3 -Q1)

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
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, female').set(title="Association between GNI per capita and life expectancy in female")

# scatter plot showing relation between GNi per capita and life expectnacy for female
#if male:
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, male').set(title="Association between GNI per capita and life expectancy in male")
        
#Part 4 question 2
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, female', hue= 'Region').set(title="Association between GNI per capita and life expectancy in female in each Regions")

#Part 4 question 3 
sns.relplot( data= data,kind= "line", x= "GNI per capita", y= "Life expectancy, female", hue="Region", errorbar= "sd" ).set(title="Association between GNI per capita and life expectancy in female in each Regions")
#answer: why cant you see the area representing a std in the plot? Because many regions have the same x value

#Part 4 question 4
sns.lmplot( data= data, x= "GNI per capita", y= "Life expectancy, female" , hue="Region").set(title="Association between GNI per capita and life expectancy in female in each Regions")

#Part 4 question 5
#exploring relationships between female life exepantcy and numerical features
sns.relplot(data= data, x= 'Internet use', y='Life expectancy, female').set(title="Relationship between life expectancy in female and the Internet Use")
#Comparison
sns.relplot(data= data, x= 'Internet use', y='Life expectancy, male').set(title="Relationship between life expectancy in male and the Internet Use")

sns.relplot( data= data, x='Physicians', y='Life expectancy, female' ).set(title="Relationship between life expectancy in female and the average number of Physicians")
sns.relplot( data= data, x='Physicians', y='Life expectancy, male' )  .set(title="Relationship between life expectancy in male and the average number of Physicians")
      
sns.relplot( data= data, x= 'International tourism', y='Life expectancy, female').set(title="Relationship between life expectancy in female and International tourism")
sns.relplot( data= data, x= 'International tourism', y='Life expectancy, male').set(title="Relationship between life expectancy in male and International tourism")

#all the plots between males and females' life expanctancy have similar trends

#1) Is there any relationship between the GNI per capita and life expectancy, female in each Regions?
g= sns.relplot(data= data, x="GNI per capita", y='Life expectancy, female' , col= 'Region')
g.fig.suptitle("Relationship between GNI per capita and life expectancy in female in each Regions", y=1.1)

#Any relationship between Tertiary education, female and GNI per capita in each Regions?
g= sns.relplot(data= data, x="Tertiary education, female", y='GNI per capita' , col= 'Region')
g.fig.suptitle("Relationship between tertiary education of female and GNI per capita in each Regions", y=1.1)

#Internet use and GNI per capita in each REgions relationship?
g = sns.relplot(data= data, x="Internet use", y='GNI per capita' , col= 'Region')
g.fig.suptitle("Relationship between Internet use and the GNI per capita in each Regions", y=1.1)

#Poluation and International toursism in each Regions relationship:
g= sns.relplot(data= data, x="Population", y='International tourism' , col= 'Region')
g.fig.suptitle("Relationship between Population and International tourism in each Regions", y=1.1)

#Woman in national parliament and tertiary education, female in each Regions relationship:
g = sns.relplot(data= data, x="Women in national parliament", y='Tertiary education, female' , col= 'Region')
g.fig.suptitle("Relationship between Woman in national parliament and Tertiary education of female in each Regions", y=1.1)

#Part 4 question 6
#a)
data["emissions per capita"] = data["Greenhouse gas emissions"]/data["Population"]
sns.relplot( data=data, x='Internet use', y='emissions per capita').set(title="Association between Internet use and emissions per capita")

#b)
filtered_data = data[data["emissions per capita"]>0.03]
for country in filtered_data["Country Name"]:
    print(country) 

#c) 
g =sns.relplot(data= data, x="Internet use", y='emissions per capita' , hue= 'High emissions countries', col='Region')
g.fig.suptitle('Variation between Internet use and Regions with high emissions', y=1.1)

#d)
high_income = data[data["High Income Economy"]> 0]
count = (high_income["Greenhouse gas emissions"] >0.03).sum() #sum of all high emissions countries
if count == 66: # data obtained from question 8 part 3
        print('Yes all countries with high income economy have high emissions')
else:
        print('No, not all countries have such high emissions')
    


    

 

