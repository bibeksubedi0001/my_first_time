import pandas as pd
Dataframe={
    "Name":["Bibek","Vikash","Princy","Shream"],
    "Age":[20,21,63,42],
    "City":["Alaska","Switizerland","Banarsi","Pokhara"]
}
index=[1,2,4,8]
kkkk=pd.DataFrame(Dataframe,index=index)
print(kkkk[kkkk["Age"]<45][["Age","Name"]])
kk=kkkk[(kkkk["Age"]>22) & (kkkk["City"]=="Banarsi")]#And
print(kk)
k=kkkk[(kkkk["Age"]>28)|(kkkk["City"]=="Alaska")]#Or
print(k)
kkk=kkkk[~(kkkk["Age"]<25)]#Not
print(kkk)