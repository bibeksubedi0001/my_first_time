import pandas as pd
rainfall = pd.read_csv(r"D:\at_my_labs\Rainfall_csv.csv")  # The 'r' before the string makes it a raw string.
print(rainfall.tail())
rainfallnepal=pd.read_excel(r"D:\at_my_labs\Rainfall_excel.xlsx")
print(rainfallnepal.head())
rn=pd.read_json(r"D:\at_my_labs\Rainfall_json.json")
print(rn.head())
r=pd.read_parquet(r"D:\at_my_labs\Rainfall_parquet.parquet")
print(r.tail())