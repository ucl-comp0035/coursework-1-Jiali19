#Importing the needed packages
import numpy as np 
import pandas as pd 

import matplotlib.pyplot as plt

#read the file for doing business dataset
df = pd.read_csv('DBData.csv')
df.head(10) 

df.shape

df.info

#here we print all the unique value in all the columns from the data daset
for col in df:
    print(df[col].unique())
    
uniqueIndicators = df['Indicator Name'].unique()


#Finding the missing data in the dataset
missing = df.isnull().sum()
missing



#we drop the most of years and only remain the rows from year 2017 to 2020
#we also drop the columns such as Country code, and indicator code, which would be useless in analyzing the data.
df_drop = df.drop(['2004','2005','2006','2007','2008','2009',
                                '2010','2011','2012','2013','2014','2015',
                                '2016','Unnamed: 21','Country Code','Indicator Code'],axis=1,inplace=False)


#we view the dataset again
df_drop.head()


df_indicator = df_drop.loc[df_drop['Indicator Name'].isin(['Trading across borders (DB16-20 methodology) - Score',
                                                       'Dealing with construction permits (DB16-20 methodology) - Score',
                                                       'Starting a business - Score',
                                                      'Enforcing contracts (DB17-20 methodology) - Score',
                                                      'Getting credit (DB15-20 methodology) - Score',
                                                      'Getting electricity (DB16-20 methodology) - Score',
                                                      'Paying taxes (DB17-20 methodology) - Score',
                                                      'Protecting minority investors (DB15-20 methodology) - Score',
                                                      'Registering property (DB17-20 methodology) - Score',
                                                      'Resolving insolvency - Score',
                                                     'Global: Ease of doing business score (DB17-20 methodology)'])]



df_indicator.shape

#make the rows with missing value form a dataframe called null_data
null_data = df_indicator[df_indicator.isnull().any(axis=1)]

#replace the missing data according their next column
df_ready = df_indicator.fillna(axis=1, method='bfill',inplace = False)

#the dataframe doesn't have any missing value now.
df_ready.isnull().sum()
