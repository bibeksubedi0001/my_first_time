import pandas as pd
raif=pd.read_csv(r"D:\at_my_labs\Rainfall_csv.csv")
raif["Rainfall (mm)"]=raif["Rainfall (mm)"]-1 #faster
raif["Rainfall (mm)"]=raif["Rainfall (mm)"].apply(lambda x: x-1) #slower
print(raif.tail())
raif.to_csv(r"D:\at_my_labs\Rainfall_csv.csv")