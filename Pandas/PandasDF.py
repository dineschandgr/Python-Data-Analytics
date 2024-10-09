import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)
result = df.loc[1]
print(result)

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc['day2'])
#print(df.loc[0])

pd.options.display.max_rows = 9999
#it prints only 1st 5 and last 5 rows
df = pd.read_csv('data.csv')
print("csv data \n", df)

#to print all rows
print("csv data \n", df.to_string())

df = pd.read_csv('data.csv')

#analyze data
print(df.head(10))
print(df.tail(11))
print("after tail --------------------------")
print("before ",df.info())

print("duplicated ",df.duplicated())
df.drop_duplicates(inplace = True)
print("after removing duplicate \n",df.to_string())
print("after ",df.info())