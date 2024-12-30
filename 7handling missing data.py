import pandas as pd
dataa=[1,2,3,3,4,5,None,0]
index=["a","b","c","d","e","f","g","h"]
s=pd.Series(dataa,index=index)
q=s.apply(lambda x: x+2)
m=s.fillna(8)
r=s.dropna()
print(r)
print(m)