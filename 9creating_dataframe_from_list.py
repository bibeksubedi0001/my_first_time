import pandas as pd
data=[
    ["Bibek","Rameh","Kartan","Manjok"],
    ["Switzerland","Turkey","Egypt","Burkina Faso"],
    ["$93749334","$937332","$83633","$628"]
]
df=pd.DataFrame(data,index=["Name","Country","Per_capita_income"],columns=["Person1","Person2","Person3","Person4"])
print(df)