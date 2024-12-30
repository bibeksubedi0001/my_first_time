import pandas as pd  # Corrected the alias for pandas
data = {
    "Name": ["ram", "sam", "yam"],
    "City": ["Paris", "Kathmandu", "Paris"],
    "DOB": ["2003", "2005", "2006"]
}
# Create the MultiIndex
index = pd.MultiIndex.from_tuples(
    [("Pulchowk", "$1000000"), ("Thapathali", "$323"), ("Pulchowk", "$83638")],
    names=["College", "Salary"]
)
df = pd.DataFrame(data, index=index)
print(df)
print(df[df["City"] == "Paris"]["City"])
#Resetting the Index
df_reset=df.reset_index()
print(df_reset)