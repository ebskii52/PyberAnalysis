#%%
# Add Matplotlib inline magic command
%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd


# %%
# Files to load
city_data_to_load = "Resources/city_data.csv"
ride_data_to_load = "Resources/ride_data.csv"

# %%
# Read the city data file and store it in a pandas DataFrame.
city_data_df = pd.read_csv(city_data_to_load)
city_data_df.head(10)

# %%
# Read the ride data file and store it in a pandas DataFrame.
ride_data_df = pd.read_csv(ride_data_to_load)
ride_data_df.head(10)

# %%
# Get the columns and the rows that are not null.
city_data_df.count()

# %%
# Get the columns and the rows that are not null.
city_data_df.isnull().sum()

# %%
# Get the data types of each column.
city_data_df.dtypes

# %%
# Get the unique values of the type of city.
city_data_df["type"].unique()

# %%
# Get the number of data points from the Urban cities.
sum(city_data_df["type"]=="Urban")

# %%
# Get the columns and the rows that are not null.
ride_data_df.count()

# %%
# Get the columns and the rows that are not null.
ride_data_df.isnull().sum()

# %%
# Get the data types of each column.
ride_data_df.dtypes

# %%
# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()

# %%
