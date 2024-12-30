import pandas as p
import numpy as n
data=n.array([[2,3,5],[4,6,8],[9,8,9]])
k=p.DataFrame(data,index=["ram","sam","tam"],columns=["Films","Poems","Jornals"])
print(k)
print(k["Films"]) #selecting column
print(k.Films)    #selecting columns
print(k.iloc[0]) #integer-location based selection of rows indexing
print(k.loc["ram"]) #label_based indexing
print(k[["Jornals","Poems"]])
k["Films"]=[4,5,6] #modifying a column
k.iloc[0]=[4,9,23] #modifying a row
k["Stories"]=[21,None,None] #add new column
print(k)
k.fillna(method="ffill",inplace=True)
print(k)