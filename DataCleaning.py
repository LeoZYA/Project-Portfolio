# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)


#1. Read CSV file.

file_path = "WalmartEC.csv"
df1 = pd.read_csv(file_path)

print(df1.head())        # Display first few rows
print(df1.info())        # Display data types and missing values

# Conclusion: Missing Values in Description(13), Brand(564), Item Number(21125), Package Size(30000), Category(17) in 30000rows

#2. Missing Values.

del df1["Item Number"]
del df1["Postal Code"]
del df1["Description"]
del df1["Package Size"]    # Removed Problematic and Redundant Columns

missing_categories = df1[df1['Category'].isnull()]
missing_categories.to_csv('missing_categories.csv', index=False)

df1['Category'].fillna('Uncategorized', inplace=True) # Fill in all missing values in Category with "Uncategorized"

missing_brands = df1[df1['Brand'].isnull()]
missing_brands.to_csv('missing_brands.csv', index=False)

df1['Brand'].fillna('Unknown', inplace=True) # Fill in all missing values in Brand with "Unknown"

print(df1.head())        # Display first few rows
print(df1.info())        # Display data types and missing values

#3. Check Duplicates.


duplicates = df1[df1.duplicated()]

# Display duplicate rows
print("Duplicates:")
print(duplicates)

# No Dups found

#4. Check Outliers.

# Detect range of values for each column of the dataset
df1.describe([x*0.1 for x in range(10)])

# Display boxplot to display the distribution of a column
import seaborn as sns
sns.boxplot(x=df1['List Price'])

# Display histogram to display the distribution of a column
sns.displot(data=df1['List Price'])
# Display a graph for observation purpose plt.show()

# Items with List Price <= 0
zero_list_price_items = df1[df1['List Price'] <= 0]
zero_list_price_items.to_csv('zero_list_price_items.csv', index=False)

# Items with List Price >= 6000
high_list_price_items = df1[df1['List Price'] > 6000]
high_list_price_items.to_csv('high_list_price_items.csv', index=False)

# 397 rows of items with 0 list price, all unavailable.

# Filter out rows where 'Available' is False
filtered_df = df1[df1['Available'] == False]

# Display the resulting DataFrame
print(filtered_df)

# Remove items with list price=0
df1 = df1[df1['List Price'] != 0]

# Outliers can't really be defined, removed items with 0 list price for analytical purpose. Items with 0 list price are
# not necessarily outliers or entry mistakes, but purpose for assigning 0 to list price is unkown.

#5. Assure Data Type.

# Convert 'Crawl Timestamp' to datetime
df1['Crawl Timestamp'] = pd.to_datetime(df1['Crawl Timestamp'])

# Convert 'Global trade item No.' to string
df1['Gtin'] = df1['Gtin'].astype(str)

# Convert 'Available' to boolean
df1['Available'] = df1['Available'].astype(bool)

#6. Output Cleaned Data.

print(df1.head())        # Display first few rows
print(df1.info())        # Display data types and missing values

df1.to_csv('Walmart_cleaned_data.csv', index=False)