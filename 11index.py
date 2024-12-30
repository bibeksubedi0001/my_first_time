import pandas as p
data={
    "Name":["ram","sam","yam"],
    "City":["Paris","Kathmandu","Paris"],
    "DOB":["2003","2005","2006"]
}
ndex=["Hi","Bibek","samita"]
info=p.DataFrame(data)
io=p.DataFrame(data,index=[2,4,8])
i=p.DataFrame(data,index=ndex)
print(info.index)
print(io.index)
print(i)
print("Bibek" in i.index) #check if label exist.
info.index=["Ram","Sam","Yam"] #renaming the index.
print(info.index)
io=io.set_index("Name") #setting a column as index
print(io)