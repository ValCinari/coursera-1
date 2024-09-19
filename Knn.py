#In this Lab I will load a customer dataset, fit the data, and use K-Nearest Neighbors to predict a data point. But what is K-Nearest Neighbors?
#K-Nearest Neighbors is a supervised learning algorithm. Where the data is 'trained' with data points corresponding to their classification. 
#To predict the class of a given data point, it takes into account the classes of the 'K' nearest data points and chooses the class in which the majority of the 'K' nearest data points belong to as the predicted class.
#Lets load required libraried
# This code sets up the enivironment for data analysis and visualizatiom in Python, preparing to use both numerical and ML techniques. 

#!pip install scikit-learn==0.23.1 # this installs a specific version of the scikit learn library, which is a popular ML in Python )
import numpy as np                # library for numercial computation, particually usefull to work with arreys)
import matplotlib.pyplot as plt   #used to create static, interactiv and animated visualizations in Python 
import pandas as pd               # A data manipulation and analysis library, particulary good for handling tabular data ( like DF) 
from sklearn import preprocessing # A module from scikit-learn that provides funxtions for data preprocessing such as scaling or normalizing data 
#%matplotlib inline                # This comand is specific to jupyter Notebooks. It allows for the inline display of plots. 

#Imagine a telecommunication provider has segmented its customers base by service usage patterns, categorizing the customers into 4 gr. 
#The target field, called custcat, has four possible values that correspond to the four customer groups, as follows: 
#1- Basic Service 2- E-Service 3- Plus Service 4- Total Service
# Our object is to build a classifier, to predict the class of unknowd cases. We will use a specific type of classification called K nearest neighbour.

df = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%203/data/teleCust1000t.csv')
df.head()

