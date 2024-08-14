import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from sklearn.cluster import KMeans


X=np.random.uniform(0,1,50)
Y=np.random.uniform(0,1,50)

#create a empty dataframe with 0 rows and 2 columns
df_xy=pd.DataFrame(columns=["X","Y"])
#assign the value of x and y to this column
df_xy.X=X
df_xy.Y=Y
df_xy.plot(x="X",y="Y",kind="scatter")
model1=KMeans(n_clusters=3).fit(df_xy)


model1.labels_
df_xy.plot(x="X",y="Y",c=model1.labels_,kind="scatter",s=10,cmap=plt.cm.coolwarm)
Univ1 = pd.read_excel("University_Clustering.xlsx")
Univ1.describe()

Univ=Univ1.drop(["State"],axis=1)

def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_func(Univ.iloc[ : ,1: ])


####################################################################



TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
    #total within sum of square
    '''
    KMeans 
    '''
TWSS
#as k value increase the TWSS value decrease
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters")
plt.ylabel("Total_within_SS")

'''
How to select value of k from elbow curve
when k changes from 2-3 ,then decrease
in twss is higher than
when k chnages from 3 to 4
when k value changes from 5 to 6 decrease

'''

model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ.iloc[:,2:8].groupby(Univ.clust).mean()

Univ.to_csv("kmeans_university.csv",encoding="utf-8")
import os
os.getcwd()

