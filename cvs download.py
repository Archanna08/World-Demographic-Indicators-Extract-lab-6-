
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
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, female')
# scatter plot showing relation between GNi per capita and life expectnacy for female
#if male:
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, male')
        
#Part 4 question 2
sns.relplot(data= data , x= 'GNI per capita', y='Life expectancy, female', hue= 'Region')

#Part 4 question 3 
sns.relplot( data= data,kind= "line", x= "GNI per capita", y= "Life expectancy, female", hue="Region", errorbar= "sd" )
#answer: why cant you see the area representing a std in the plot? Because many regions have the same x value

#Part 4 question 4
sns.lmplot( data= data, x= "GNI per capita", y= "Life expectancy, female" , hue="Region")

#Part 4 question 5
#exploring relationships between female life exepantcy and numerical features
sns.relplot(data= data, x= 'Internet use', y='Life expectancy, female')
#Comparison
sns.relplot(data= data, x= 'Internet use', y='Life expectancy, male')

sns.relplot( data= data, x='Physicians',y='Life expectancy, female' )
sns.relplot( data= data, x='Physicians',y='Life expectancy, male' )  
      
sns.relplot( data= data, x= 'International tourism', y='Life expectancy, female')
sns.relplot( data= data, x= 'International tourism', y='Life expectancy, male')

#all the plots between males and females' life expanctancy have similar trends

#Is there any relationship between the Population and Regions?

g= sns.FacetGrid(data= data, col= 'Region')
g.map(sns.relplot, x='GNI per capita',y='Population')


#Any relationship between Tertiary education, female and Regions?

#Internet use and REgions relationship: Does it vary depending on the Regions?

#Subregion and Regions relationship

#Women in national parliament and Regions relationship

#Part 4 question 6
#a)
data["emissions per capita"] = data["Greenhouse gas emissions "]/data["Population"]
sns.relplot( data=data, x='Internet use', y='emissions per capita')

#b)
filtered_data = data[data["Greenhouse gas emissions"]>0.03]
for country in filtered_data["Country Name"]:
    print(country) 

#c) 
#??

#d)

high_income = data[data["High Income Economy"]> 0]
count = (high_income["Greenhouse gas emissions"] >0.03).count()
if count == 66: # data obtained from question 8 part 3
        print('Yes all countries with high income economy have high emissions')
else:
        print('No, not all countries have such high emissions')
    


    

 

