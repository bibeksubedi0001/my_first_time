import pandas as pd
data=[1,2,3,4,5,6]
serial=["a","b","c","d","e","f"]
s=pd.Series(data,index=serial)
print(s["a"])
print(s[0]) 
#both will give same output.
print(s["a":"d"])
print(s[0:4])
#both will give same output.