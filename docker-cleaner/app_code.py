# %% [markdown]
# #PM Task
# Load the two datasets
# Clean the them (thoroughly)
# Measure at least 1 data engineering metric in the data cleaning process (ie dropped rows)
# MVP: Output the cleaned files as a local csv.
# Stretch:
# 
# Output the cleaned files into the local SSMS (use SQLAlchemy); create a new DB for this.
# Refactor your code into modular functions.

# %%
import pandas as pd

# Data engineering metrics (instantiation)
dropCount= 0

# Reading both sets of data

Book_Data = pd.read_csv ('03_Library Systembook.csv')
Customer_Data = pd.read_csv ('03_Library SystemCustomers.csv')

print(Book_Data.head())
print(Customer_Data.head())

# Summary
print(f"There are {len(Book_Data)} rows in this dataset")
Book_Data.head()

# %%
Customer_Data.drop_duplicates
Book_Data.drop_duplicates


# %%
Book_Data.dropna(thresh=2)

# %%
try:
    Book_Data['Book checkout'] = Book_Data['Book checkout'].str.replace('"',"",regex=True)
    Book_Data['Book checkout'] = pd.to_datetime(Book_Data['Book checkout'], format='mixed')
    Book_Data.head()
except Exception as e:
    print(f"Error Occured: {e}")

# %%
Book_Data.iloc[16]

# %%
Book_Data.drop(16, inplace=True)
dropCount += 1

# %%
Customer_Data.dropna(thresh=1)

# %%
# RETRY Converting the date of purchase to date format
Book_Data['Book checkout'] = Book_Data['Book checkout'].str.replace('"', "", regex=True)
Book_Data['Book checkout'] = pd.to_datetime(Book_Data['Book checkout'], format='mixed' ) 
Book_Data['Book Returned'] = pd.to_datetime(Book_Data['Book Returned'], format='mixed' ) 
Book_Data.head()

# %%
na_dropped_data = Book_Data.dropna()
dropCount +=  len(Book_Data) - len(na_dropped_data)
na_dropped_data.head()

# %%
na_dropped_data

# %%
# Creating and using a function to enrich the data by adding in the time a book was on loan.
data_enriched = na_dropped_data.copy()

def enrich_dateDuration(colA, colB, df=data_enriched):
    """
    Takes the two input columns and the dataframe to create a new column date_delta which is the difference, in days, between colA and colB.
    
    Note: ColA should be the highest of the expected date columns.
    """
    df['date_delta'] = (df[colA]-df[colB]).dt.days
    return df.head()

enrich_dateDuration(df=data_enriched, colA='Book Returned', colB='Book checkout')


