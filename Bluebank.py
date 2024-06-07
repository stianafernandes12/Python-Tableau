# -*- coding: utf-8 -*-
"""
Created on Fri May 10 10:30:10 2024

@author: Stiana Fernandes
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#method 1 to read json data
json_file = open('C:/Users/NIRMALA PAUL/OneDrive/Documents/Udemy - Python/Project 2 Blue Bank/loan_data_json.json')
data = json.load(json_file) 


#transform to dataframe
loandata = pd.DataFrame(data)

#finding unique values for the purpose column
loandata['purpose'].unique()

#describe the data 
loandata.describe()


#describe the data for a specific col
loandata['int.rate'].describe()

loandata['fico'].describe()

loandata['dti'].describe()


loandata.info()

#Install numpy in anaconda prompt - pip install numpy

#Using EXP() to get the annual income 

income = np.exp(loandata['log.annual.inc'])

loandata['annualincome']=income

#FICO score

fico = 250

# 300 - 400: Very Poor
# 401 - 600: Poor
# 601 - 660: Fair
# 661 - 780: Good
# 781 - 850: Excellent


if fico >= 300 and fico < 400:
    ficocat ='Very Poor'
elif fico >= 401 and fico <600:
    ficocat = 'Poor'
elif fico >= 601 and fico <660:
    ficocat = 'Fair'
elif fico >= 661 and fico <780:
    ficocat = 'Good'
elif fico >= 781 and fico <850:
    ficocat = 'Excellent'  
else:
    ficocat = 'Unknown'
print(ficocat)
    

#for loop to apply this on every cell in a row 

#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    if category >= 300 and category<400:
        cat='Very Poor'
    elif category >= 400 and category<600:
        cat='Poor'
    elif category >= 601 and category<660:
        cat='Fair'
    elif category >= 660 and category<700:
        cat='Good'
    elif category >= 700:
        cat='Excellent'
    else:
        cat='Unknown'
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

#Try and except
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category<400:
            cat='Very Poor'
        elif category >= 400 and category<600:
            cat='Poor'
        elif category >= 601 and category<660:
            cat='Fair'
        elif category >= 660 and category<700:
            cat='Good'
        elif category >= 700:
            cat='Excellent'
        else:
            cat='Unknown'
            
    except:
         cat='Unknown'
    ficocat.append(cat)
    

#Try and error (This is used so that in case there is any string in the data, atleast the code runs for the rest of the values and doesn't give error)
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat



    
ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat



#Loops or Loc
#df.loc as conditional statements
# df.loc[df[columnname]condition,newcolumnname] = 'value if the condition is met'


loandata.loc[loandata['int.rate']>0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <=0.12,'int.rate.type'] = 'Low'

#To get how many borrowers are in a particular fico category 
#Number of loans/rows by fico.category
#Here size represenst number of rows

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color='purple', width=0.5)
plt.show()

purposeplot = loandata.groupby(['purpose']).size()
purposeplot.plot.bar(color='green', width=0.2)
plt.show()


#Scatter Plot
#Using Income and DTI score, with high inc so less debt

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color = '#4caf50')
plt.show()




#Writing to csv

loandata.to_csv('loan_cleaned.csv', index= True)











#for loops
fruits = ['apple','pear','banana','cherry']

for x in fruits:
    print(x)
    y=x+'fruit'
    print(y)
    
    
for x in range(0,1):
    y = fruits[x]+' for sale'
    print(y)
    
    
#While loops
i = 1
while i<10:
    print(i)
    i=i+1

#Working with arrays

arr= np.array([1,2,3,4])

#0D Array
arr = np.array(43)

#2D array
arr = np.array([[1,2,3],[4,5,6]])

#Logical conditions
#Equals a==b
#Not equla a!=b

#Working with if statements
a = 40
b = 500

if b > a:
    print ('b is greater than a')

#Let's add more conditions

a=40
b=500
c=1000

if b>a and b<c:
    print ('b is greater than a but less than c')


#What if a condition is not met

a=40
b=500
c=20

if b>a and b<c:
    print ('b is greater than a but less than c')
else:
    print('no conditions met')

#another condition diff metrics
a=40
b=500
c=30

if b>a and b<c:
    print ('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('No conditions met')

#Using or
a=40
b=0
c=30

if b>a or b<c:
    print ('b is greater than a or less than c')

else:
    print('No conditions met')







lists = ['apple', 'pear','banana', 'pear']

#append to a list
lists.append('cherry')

#insert item into a specific position
lists.insert(1, 'kiwi')

#remove items in a list
lists.remove('pear')

#remove the last item in a list
lists.pop()

#Working with dictionaries
#Dictionary has a key and its value

mydict = {
    'name' : 'Sti',
    'favcolour': 'Purple',
    'fav place' : 'India',
    'luckynumber': 7
      }

#access other keys
color = mydict['favcolour']
print(color)

#to get a list of keys


mydict.keys()
#to get a list of values
mydict.values()

#to get a list of items
mydict.items()


#to add a new key/variable
mydict['gender'] = 'female'
