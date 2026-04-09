[15:11, 09/04/2026] Mayank Gadpal: import pandas as pd

# Sample DataFrame (you can replace with your actual data)
df = pd.read_csv("diamonds.csv")

# Mean price for each cut
mean_price = df.groupby('cut')['price'].mean()

print(mean_price)
[15:12, 09/04/2026] Mayank Gadpal: import pandas as pd

df = pd.read_csv("diamonds.csv")

# Count, min and max
result = df.groupby('cut')['price'].agg(['count', 'min', 'max'])

print(result)
[15:12, 09/04/2026] Mayank Gadpal: import pandas as pd

df = pd.read_csv("diamonds.csv")

# Mean of x, y, z
avg_values = df[['x', 'y', 'z']].mean()

print(avg_values)
[15:12, 09/04/2026] Mayank Gadpal: import pandas as pd

df = pd.read_excel("employee.xlsx")

print(df.head())