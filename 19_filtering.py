import pandas as pd
Dataframe={
    "Name":["Bibek","Vikash","Princy","Shream"],
    "Age":[20,21,63,42],
    "City":["Alaska","Switizerland","Banarsi","Pokhara"]
}
index=[1,2,4,8]
kkkk=pd.DataFrame(Dataframe,index=index)
kk=kkkk[kkkk["City"].isin(["Alaska","Pokhara"])]
print(kk)
k=kkkk.query('Age<25 and City=="Alaska"')
print(k)
kkk=kkkk[(kkkk["Age"]<25) & (kkkk["City"].isin(['Alaska','Switizerland']))]
print(kkk)