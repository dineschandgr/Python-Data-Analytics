import pandas as pd


df = pd.read_csv('data.csv')
pd.options.display.max_rows = 9999
new_df = df.dropna()
print("new df ",new_df.to_string())
print("new df info",new_df.info())
df.dropna(inplace = True)
print("original frame \n",df)
print("original frame info",df.info())

df = pd.read_csv('data.csv')
df.fillna(99999, inplace = True)
print("original frame \n",df)

df1 = pd.read_csv('data.csv')
df1["Maxpulse"].fillna(9999, inplace = True)
print("Maxpulse frame \n",df1)

df = pd.read_csv('data.csv')
x = df["Maxpulse"].mean()
df["Maxpulse"].fillna(x, inplace = True)
print("Maxpulse frame \n",df)

# df = pd.read_csv('cleaning.csv')
# df['Date'] = pd.to_datetime(df['Date'])
#
# df.dropna(subset=['Date'], inplace = True)
# print("date \n",df.to_string())

df = pd.read_csv('data.csv')
df.loc[7, 'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print("date \n",df.to_string())

