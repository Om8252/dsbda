import pandas as pd
import numpy as np
path="E:\study\dsbda\Toyota.csv"
missing_value=["??","????"]
df=pd.read_csv(path,sep=",",na_values=missing_value)
#=====================================subset=========================
#Create subset of cars_data having Price greater than 15000 and Age less yhan 8
subset1=df[(df["Price"]>15000 )&(df["Age"]<8)]
#Create subset of cars data consuming Petrol
subset2=df[df["FuelType"]=="Petrol"]
#b.	Create  selecting rows and columns, 
subset3=df.loc[:10,["Price","Age","FuelType"]]
subset6=df[["Price","Age","FuelType","Automatic"]].loc[52:67]
subset5=df[['Price','Age','FuelType']].loc[df['FuelType']!='Petrol']
#Subset by Selecting columns,
subset4=df[["Price","Age","FuelType","Automatic"]]
#=============================================================================

#===============================	Merge ==========
merge=pd.concat([subset1,subset6])

#=========================sort====================
#rverce order or decending order
sort1=df.sort_values("Price",ascending=False)
#assending order
sort2=df.sort_values("Price")

#==========================transose=========
transpose=df.transpose();

#=============shape and reshape using pivot_ table

print(df.shape);
reshped=pd.pivot_table(subset3, index=["Age","FuelType"],values="Price")



#=============================================================================================





print(df.info)
print(df.describe)
#===========================
print(df["Price"].describe)
print(df.dtypes)
#===========================
#convert dataa type
#4.	Convert the datatype of Metcolor and Automatic column in as object type
df["MetColor"]=df["MetColor"].astype('object')
print(df["MetColor"].dtype)
#===========================
#Add a new column ‘Revised’ to the dataset specifying 5% increase in old Price.(New Price=Old Price×(1+Percentage Increase))
df['Revised_Price']=df["Price"]*1.05 







#=========================================

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






#-----------------------------transformation

#4.	Apply mean-max normalization on HP column

from sklearn.preprocessing import MinMaxScaler
df['HP_normalized']  = MinMaxScaler().fit_transform(df[['HP']])
print(df['HP_normalized'])
#--------------------------------------------or----------
min_hp = df['HP'].min()
max_hp = df['HP'].max()
df['HP_normalized'] = (df['HP'] - min_hp) / (max_hp - min_hp)
print(df['HP_normalized'])

#================================Z-score------------------
from scipy.stats import zscore
df["Z-SCORE"]=zscore(df["HP"])
print(df['Z-SCORE'])
#==========================================or=================
# (x - x.mean()) / x.std()
hp_mean=df["Price"].mean()
hp_std=df["Price"].std()
df["Z-SCORE"]=(df["Price"]-hp_mean)/(hp_std)
print(df['Z-SCORE'])


#===================================decimal===================== 

max_abs_price = np.max(np.abs(df['Price']))
print(max_abs_price)
num_digits = len(str(int(max_abs_price)))
print(num_digits)
df['Price_normalized'] = df['Price'] / (10 ** num_digits)
print(df['Price_normalized'])












#================================e.	Get dummies
#e.	Get dummies for categorical data Fuel type
cars_sub1=df[['Price','Age','FuelType','Automatic']]
dummy_df1=pd.get_dummies(cars_sub1,columns=['FuelType'])
dummy_df2=pd.get_dummies(cars_sub1,columns=['FuelType','Automatic'])