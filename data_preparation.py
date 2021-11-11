# Write code that prepares your data
#after drop some years, let's look at the missing data again
#read the file for doing business dataset
df = pd.read_csv('DBData.csv')

df_drop = df.drop(['2004','2005','2006','2007','2008','2009',
                                '2010','2011','2012','2013','2014','2015',
                                '2016','Unnamed: 21','Country Code','Indicator Code'],axis=1,inplace=False)


df_drop.isnull().sum()

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

#checking the missing value again, and there is only 20 missing value
df_indicator.isnull().sum()


#make the rows with missing value form a dataframe called null_data
null_data = df_indicator[df_indicator.isnull().any(axis=1)]


print(null_data)


#replace the missing data according their next column
df_ready = df_indicator.fillna(axis=1, method='bfill',inplace = False)


#the dataframe doesn't have any missing value now.
df_ready.isnull().sum()

df_ready['2017'] = df_ready['2017'].astype("float")
boxplot = df_ready.boxplot(column=['2017'])
boxplot.plot()
plt.show()


df_ready['2018'] = df_ready['2018'].astype("float")
boxplot = df_ready.boxplot(column=['2018'])
boxplot.plot()
plt.show()



df_ready['2019'] = df_ready['2019'].astype("float")
boxplot = df_ready.boxplot(column=['2019'])
boxplot.plot()
plt.show()


df_ready['2020'] = df_ready['2020'].astype("float")
boxplot = df_ready.boxplot(column=['2020'])
boxplot.plot()
plt.show()


his2017 = plt.hist(df_ready['2017']) 
plt.title("score distribution in 2017")
plt.show()


his2018 = plt.hist(df_ready['2018'],color='green') 
plt.title("score distribution in 2018")
plt.show()


his2019 = plt.hist(df_ready['2019'],color = 'red') 
plt.title("score distribution in 2019")
plt.show()


his2020 = plt.hist(df_ready['2020']) 
plt.title("score distribution in 2020")
plt.show()


#this code will help the data been converted to an csv file, the people who are examine this dataset can put path where they want to store in the code
df_ready.to_csv(r'Path where you want to store the exported CSV file\File Name.csv', index = False)
