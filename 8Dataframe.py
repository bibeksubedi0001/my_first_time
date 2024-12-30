import pandas as pd
Dataframe={
    "Name":["Bibek","Vikash","Princy","Shream"],
    "Age":["20","21","63","42"]
}
index=[1,2,3,4]
print(pd.DataFrame(Dataframe,index=index,))