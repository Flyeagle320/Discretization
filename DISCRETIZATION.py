# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 06:26:11 2022

@author: Rakesh
"""

#loading package for data manipulation##

import pandas as pd

##importing dataset irish.csv ##

iris = pd.read_csv('D:/DATA SCIENCE ASSIGNMENT/DataSets-Data Pre Processing/DataSets/iris.csv')

iris.info() ##to see null or na value#

iris.describe() ##to find mean,median, IQR
##we dont need column 'unnamed'

iris.drop(iris.columns[0],axis=1 , inplace = True)

###to Check NA's value ##
iris.isna().sum()

##box plot for every column

iris.columns

iris.boxplot(column= ['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width'])

#we can see Sepal width has outlier ##

##graphical representation##

import matplotlib.pyplot as plt


##Descritization for each column

##Sepal Length##

plt.hist(iris['Sepal.Length']) ##histogram#
iris['Sepal.Length'].unique()
iris['Sepal.Length'] = pd.cut(iris['Sepal.Length'],bins=[0,5.5,6.7,7.9],labels=['small', 'medium', 'large'])
# size under 5.5 = small , 5.5 between 6.7 = medium ,greater 6.7 = large 
iris['Sepal.Length'].value_counts()

##Sepal Width##
plt.hist(iris['Sepal.Width']) #histogram#
iris['Sepal.Width'].unique()
iris['Sepal.Width']= pd.cut(iris['Sepal.Width'],bins=[0,2.7,3.5,4.5],labels=['small','medium', 'large'])
# size under 2.7 = small , 2.7 between 3.5 = medium ,greater than 3.5 = large 
iris['Sepal.Width'].value_counts()

##Petal length
plt.hist(iris['Petal.Length'])
iris['Petal.Length'].unique()
iris['Petal.Length']=pd.cut(iris['Petal.Length'],bins=[0,2.5,5,7],labels=['small','medium','large'])
# size under 2.5 = small , 2.5 between 5 = medium ,greater than 5 = large
iris['Petal.Length'].value_counts()

##Petal Width
plt.hist(iris['Petal.Width'])
iris['Petal.Width'].unique()
iris['Petal.Width'] =pd.cut(iris['Petal.Width'],bins=[0,0.9,1.8,2.5])
# size under 0.9 = small , 0.9 between 1.8 = medium ,greater than 1.8 = large 
iris['Petal.Width'].value_counts()










