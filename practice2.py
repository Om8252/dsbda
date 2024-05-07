import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path="E:\study\dsbda\Toyota.csv"
missing_value=["??","????"]
df=pd.read_csv(path,sep=",",na_values=missing_value)


#data cleaning

#=====================duplicate 

newdf=df.drop_duplicates()

print(df.isna().sum())
#-------numric value
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['KM'].fillna(df['KM'].median(), inplace=True)
df['HP'].fillna(df['HP'].mean(), inplace=True)

#===================String catagroal vriables
df['FuelType'].fillna(df['FuelType'].value_counts().index[0] ,inplace=True )
df['MetColor'].fillna(df['MetColor'].value_counts().index[0] ,inplace=True ) 

print(df.isna().sum())

#==========================visulization==========================.
#1.	Scatter plot- Car-Price by Age
sns.scatterplot(data=df,x="Price",y="Age",hue="Age");
plt.title("Scatter Plot Car Price vs Age")
plt.xlabel('Agee in months')
plt.ylabel('Price in Dollars')
plt.show();
#2.	Histogram on Cars data KM
sns.histplot(data=df,x="KM")
plt.show();
#1.	Bar plot on counts of FuelType category (Petrol, Disel and CNG) 
# Bar label
counts = df['FuelType'].value_counts()
fuel_types = counts.index.tolist()
# Create bar plot using Seaborn
sns.barplot(x=fuel_types, y=counts)
plt.title("Bar Plot of Fuel Type")
plt.xlabel('Fuel Used')
plt.ylabel('Frequency')
plt.show()
#b.	Distribution of KM data - Histogram with/without default kernel density estimate
sns.distplot(df["KM"], kde=False)
sns.distplot(df["KM"])
#c.	Bar plot
sns.barplot(data=df.loc[:30],x="Age",y="Price")
