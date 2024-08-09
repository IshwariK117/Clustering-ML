
import pandas as pd
import matplotlib.pylab as plt

#now import file from dataset and create a dataframe
Univ1=pd.read_excel("University_Clustering.xlsx")
a=Univ1.describe()
a

#state is not giving meaningful information..drop it
Univ=Univ1.drop(["State"],axis=1)
Univ

#There is scale difference among th column
#which we have to remove
#either by using normalization or standardization
#whenever there is mixed data apply normalization

def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_func(Univ.iloc[ : ,1: ])

#you can check the df_norm dataframe which is scaled between values 0 and 1
#you can apply describe fynction to apply new data frame


b=df_norm.describe()


#before we apply clustering we need to plot dendrogram first
#to ceate dendrogram we need to measure distance
#we have to import linkage

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or agglomerotive clustering

z=linkage(df_norm,method="complete",metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("hierarchical clustering dendrogram");
plt.xlabel("Index")
plt.ylabel("distance")

#ref help denrogram
#sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()


#--------------------

from sklearn.cluster import AgglomerativeClustering
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(df_norm)

#apply labels to clustres
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)

#assign this series to Univ dataframe as column and name the column
Univ['clust']=cluster_labels

#we want to rlocate column 7 to 0th position 
Univ1=Univ.iloc[ : ,[7,1,2,3,4,5,6]]

#check the Univ dataframe
Univ1.iloc[ : ,2: ].groupby(Univ.clust).mean()

#from output cluster2 has got highets top10
#lowest accept ratio ,best faculty ratio and highest expenses
#highest graduation ratio

