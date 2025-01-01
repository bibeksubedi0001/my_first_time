import pandas as pd
rainfalls=pd.read_csv(r"D:\at_my_labs\Rainfall_csv.csv")
rainfalls['Wind Speed (km/h)'] = pd.to_numeric(rainfalls['Wind Speed (km/h)'], downcast="integer")
rainfalls['Humidity (%)'] = pd.to_numeric(rainfalls['Humidity (%)'], downcast="integer")
print(rainfalls.tail())
rainfalllse=rainfalls.drop(columns=["Humidity (%)",'Date','Station','Precipitation Type']) #removing columns if necessary
print(rainfalllse.tail())