import pandas as pd
Dataframe={
    "Name":["Bibek","Vikash","Princy","Shream"],
    "Age":[20,21,63,42],
    "City":["Alaska","Switizerland","Banarsi","Pokhara"]
}
index=[1,2,4,8]
kkkk=pd.DataFrame(Dataframe,index=index)
print(kkkk.loc[0:2])
print(kkkk.iloc[0:2])
print(kkkk.loc[:,"Name":"City"])