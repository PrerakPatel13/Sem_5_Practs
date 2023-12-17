

import pandas as pd
list1=[2,3,4]
var1=pd.Series(list1)
print(var1)

var1=pd.Series(list1,index=['x','y','z'])
print(var1)

dist1={'1':'abc','2':'dfg'}
var1=pd.Series(dist1)
print(var1)

data={
    'sapid':[12,13,14,None],
    'name':['abc','dfg','xyz',None]
}
df=pd.DataFrame(data)
df.loc[0]

row=df.loc[df['name']=='abc'].index
row

df

df.head(1)

df.tail(1)

df.info()

df.isna().sum()

df.dropna()

data={
    'sapid':[12,13,14,None],
    'name':['abc','dfg','xyz','erf']
}
df=pd.DataFrame(data)

df.fillna(df.mean())

data={
    'sapid':[12,14,15,None],
    'name':['abc','dfg','xyz','erf']
}
df=pd.DataFrame(data)

df.fillna(df.median())

df.describe()

import matplotlib.pyplot as plt
import numpy as np
x=np.array(['A','B','C'])
y=np.array([9,8,7])
plt.scatter(x,y)
plt.show()

plt.pie(y)

plt.bar(x,y)

x=np.random.normal(100,10,200)
plt.hist(x)
plt.show()

