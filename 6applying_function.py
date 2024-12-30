import pandas as pd
data=[1,2,2,4]
a=pd.Series(data)
squared=a.apply(lambda x: x**2)
triple=a.apply(lambda x: x*3)
print(squared,triple)
