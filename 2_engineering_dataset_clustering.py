

import pandas as pd
import matplotlib.pylab as plt

#now import file from dataset and create a dataframe
Univ1=pd.read_excel("Engineering_Dataset.xlsx")
a=Univ1.describe()
a




#state is not giving meaningful information..drop it
Univ=Univ1.drop(["State"],axis=1)
Univ
Univ.columns


def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x

df_norm=norm_func(Univ.iloc[ : ,1: ])

#you can check the df_norm dataframe which is scaled between values 0 and 1
#you can apply describe fynction to apply new data frame


b=df_norm.describe()
