import pandas as pd

# ==========================================
# SELF-ASSESSMENT REFLECTIONS (Lab 13)
# 1. A boolean filter evaluates conditions row by row, returning True or False 
#    to select only the rows that match the specified criteria.
# 2. df["revenue"] returns a 1D Pandas Series, whereas df[["revenue"]] 
#    returns a 2D Pandas DataFrame. The distinction matters when doing operations 
#    that expect a DataFrame layout vs a single column series.
# 3. Pandas allows for fast, programmatic handling of massive datasets that 
#    would crash or bog down Excel, enabling reproducible scripts.
# ==========================================

# EXERCISE 1: Load it
df = pd.read_csv('data/retail_sales.csv')
print("--- EXERCISE 1 ---")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)

# EXERCISE 2: Filter by region
print("\n--- EXERCISE 2 ---")
south = df[df['region'] == 'South']
print(len(south))
print(south.head())

# EXERCISE 3: Top 5 by revenue
print("\n--- EXERCISE 3 ---")
print(df.sort_values('revenue', ascending=False).head(5))

# EXERCISE 4: Two-condition filter
print("\n--- EXERCISE 4 ---")
big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]
print(len(big_south))
print(big_south.head(5))

# EXERCISE 5: A new column
print("\n--- EXERCISE 5 ---")
df['per_unit'] = df['revenue'] / df['quantity']
print(df.head())
print("Mean per-unit price:", df['per_unit'].mean())

# EXERCISE 6: Unique values
print("\n--- EXERCISE 6 ---")
print(df['region'].unique())
print(df['region'].value_counts())

# EXERCISE 7: Select columns
print("\n--- EXERCISE 7 ---")
subset_df = df[['region', 'product', 'revenue']]
print(subset_df.shape)

# EXERCISE 8: Save
df.to_csv('data/explored.csv', index=False)
print("\n--- EXERCISE 8 ---")
print("Saved successfully to data/explored.csv")