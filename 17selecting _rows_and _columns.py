import pandas as pd
Dataframe={
    "Name":["Bibek","Vikash","Princy","Shream"],
    "Age":[20,21,63,42],
    "City":["Alaska","Switizerland","Banarsi","Pokhara"]
}
index=[1,2,4,8]
kkkk=pd.DataFrame(Dataframe,index=index)
print(kkkk[["Age","City"]]) #usecols cannot be used
print(kkkk.loc[1]) #indexname
print(kkkk.iloc[1]) #indexnumber
print(kkkk.Age[1]) #columns
print(kkkk.iloc[0:2])
print(kkkk.loc[kkkk["Age"] >= 23])
print(kkkk[kkkk["Age"]>60])
print(kkkk.loc[0:2,[kkkk["Age"],"Name"]]) #both
