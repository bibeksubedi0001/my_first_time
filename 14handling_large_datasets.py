import pandas as pd
dtypes={"Rainfall (mm)":"float32","Humidity (%)":"int16"}
rainfall=pd.read_csv(r"D:\at_my_labs\Rainfall_csv.csv",dtype=dtypes) #datatypes usage
print(rainfall.head())
rainfalls=pd.read_csv(r"D:\at_my_labs\Rainfall_csv.csv", usecols=["Rainfall (mm)",'Humidity (%)']) #use of usecols
print(rainfalls.head())
print(rainfall["Precipitation Type"].head()) #specify column, column name won't be visible
