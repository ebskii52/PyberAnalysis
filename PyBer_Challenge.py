#%%
# Add Matplotlib inline magic command
%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import os

# %%
# Files to load

city_data_to_load = os.path.abspath("Resources/city_data.csv")
ride_data_to_load = os.path.abspath("Resources/ride_data.csv")


# %%## Module 5 Challenge
## Create a PyBer Summary DataFrame
# Combine the data into a single dataset

ride_data_df = pd.read_csv(ride_data_to_load)
city_data_df = pd.read_csv(city_data_to_load)

pyber_data_df = pd.merge(ride_data_df, city_data_df, on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()

# %%
# Create the Urban city DataFrame.
urban_cities_df = pyber_data_df[pyber_data_df["type"] == "Urban"]
urban_cities_df.head()

# %%
# Create the Suburban and Rural city DataFrames.
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]
rural_cities_df = pyber_data_df[pyber_data_df["type"] == "Rural"]

# %%
# Get the number of rides for urban cities.
urban_ride_count = urban_cities_df.groupby(["city"]).count()["ride_id"]

# %%
# Create the suburban and rural ride count.
suburban_ride_count = suburban_cities_df.groupby(["city"]).count()["ride_id"]

rural_ride_count = rural_cities_df.groupby(["city"]).count()["ride_id"]

# %%
# Get average fare for each city in the urban cities.
urban_avg_fare = urban_cities_df.groupby(["city"]).mean()["fare"]
urban_avg_fare.head()

# %%
# Get average fare for each city in the suburban and rural cities.
suburban_avg_fare = suburban_cities_df.groupby(["city"]).mean()["fare"]
rural_avg_fare = rural_cities_df.groupby(["city"]).mean()["fare"]

# %%
# Total Number of Urban Drivers
urban_driver_count = urban_cities_df.groupby(["city"]).mean()["driver_count"]
suburban_driver_count = suburban_cities_df.groupby(["city"]).mean()["driver_count"]
rural_driver_count = rural_cities_df.groupby(["city"]).mean()["driver_count"]

#%%
# Get the average number of drivers for each urban city.
Total_Rides = pyber_data_df.groupby(["type"]).count()["city"]

urban_driver_sum = urban_driver_count.sum()
rural_driver_sum= rural_driver_count.sum()
suburban_driver_sum = suburban_driver_count.sum()

TotalDriverDF = pd.DataFrame({"type": ["Rural", "Suburban", "Urban"], "Total Drivers":[rural_driver_sum,suburban_driver_sum,urban_driver_sum]})
TotalDriverDF = TotalDriverDF.set_index(["type"])["Total Drivers"]

Total_Fares = pyber_data_df.groupby(["type"]).sum()["fare"] 
Avg_PerRide = pyber_data_df.groupby(["type"]).mean()["fare"]
Avg_FarePerDriver = Total_Fares/TotalDriverDF


# %%
#To create the summary DataFrame, follow these steps:

#Get the total rides, total drivers, and total fares for each city type using the groupby() function on the city type using the merged DataFrame or separate DataFrames.
#Calculate the average fare per ride and the average fare per driver by city type.
#Delete the index name.
#Create the summary DataFrame with the appropriate columns and apply formatting where appropriate.


SummaryDF = pd.DataFrame({"Total Rides": Total_Rides, "Total Drivers":TotalDriverDF,  "Total Fares": Total_Fares,
                       "Average Fare per ride":Avg_PerRide, "Average Per Driver": Avg_FarePerDriver})

SummaryDF.index.name = None

SummaryDF["Total Fares"] = SummaryDF["Total Fares"].map("${:.2f}".format)
SummaryDF["Average Fare per ride"] = SummaryDF["Average Fare per ride"].map("${:.2f}".format)
SummaryDF["Total Drivers"] = SummaryDF["Total Drivers"].map("{:.0f}".format)
SummaryDF["Average Per Driver"] = SummaryDF["Average Per Driver"].map("${:.2f}".format)
SummaryDF["Total Rides"] = SummaryDF["Total Rides"].map("{:,}".format)


# %%
## Rename columns

pyber_data_df.rename(columns={'city': 'City', 'date':'Date','fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 'type':'City Type'}, inplace=True)

pyber_data_df

# %%
## Set the index to the Date column
# Reorder the columns in the order you want them to appear.
new_column_order = ['Date', 'City', 'Fare', 'Ride Id','No. Drivers', 'City Type']

pyber_data_df = pyber_data_df[new_column_order]

pyber_data_df
# %%
# Create a new DataFrame for fares and include only the 
##Date, City Type, and Fare columns using the copy() method on the merged DataFrame
new_pyber_data_df  = pyber_data_df[["Date", "City", "Fare", "City Type"]].copy()

# %%
new_pyber_data_df.set_index("Date")

DateTypes = new_pyber_data_df["Date"].tolist()

Date_fixed = []

for name in DateTypes:
    if len(name.split()) >= 1:
        Date_fixed.append(name.split()[0])

new_pyber_data_df["Date"] =  Date_fixed

# %%
new_pyber_data_df.head()

# %%
# 7. Calculate the sum() of fares by the type of city and date using groupby() to create a new DataFrame.
FaresDF = new_pyber_data_df.groupby(["City Type", "Date"]).sum()["Fare"]
FaresDF = FaresDF.to_frame()

FaresDF

# %%
## 8. Reset the index, which is needed for Step 10.
FaresDF.reset_index(inplace = True) 
FaresDF

#%%
#from datetime import datetime 

#FaresDF['Date'] = pd.to_datetime(FaresDF['Date']).dt.date

FaresDF

#FaresDF.index.name = "Date"
#FaresDF
#%%
## 
## 9. Create a pivot table DataFrame with the Date as the index and columns = 'City Type' with the Fare for each Date in each row

import numpy as np
import scipy.stats as sts

FarePVTable = pd.pivot_table(FaresDF, values='Fare', index=['Date'], columns=['City Type'], aggfunc=np.sum)
FarePVTable

#%% 
## 10. Create a new DataFrame from the pivot table DataFrame on the given dates '2019-01-01':'2019-04-28' using loc .

FarePVTableDF =  FarePVTable.reset_index()
FarePVTableDFTrial = FarePVTableDF.set_index("Date")
FarePVTableDF =  FarePVTableDFTrial.loc['2019-01-01':'2019-04-28']
FarePVTableDF

#%%
from datetime import datetime 
FaresDFDate = FarePVTableDF.copy()
FaresDFDate = FaresDFDate.reset_index()
FaresDFDate["Date"] = pd.to_datetime(FaresDFDate["Date"])
FaresDFDate = FaresDFDate.reset_index(drop=True)
FaresDFDate = FaresDFDate.set_index(["Date"])
FaresDFDate

#%%
## 11. Create a new DataFrame by setting the DataFrame you created in Step 11 
##     with resample() in weekly bins, and calculate the sum() of the fares for each week.

TotalFaresWeekly = FaresDFDate.resample("W").sum()
TotalFaresWeekly


# %%
# Using the object-oriented interface method, plot the DataFrame you created in 
# Step 12 using the df.plot() function. Things to consider with your plotting:

import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt


plt.style.use('fivethirtyeight')

plt.figure(figsize=(15,8))
plt.xlabel("Date")
plt.ylabel("Fare($)")

# Create a title. 
plt.title("PyBer Fare by Month")

plt.plot((TotalFaresWeekly.index.to_pydatetime()).astype('datetime64[W]'), TotalFaresWeekly["Urban"], marker="*", color="green", linewidth=2, label='Urban')
plt.plot((TotalFaresWeekly.index.to_pydatetime()).astype('datetime64[W]'), TotalFaresWeekly["Rural"], marker="*", color="black", linewidth=2, label='Rural')
plt.plot((TotalFaresWeekly.index.to_pydatetime()).astype('datetime64[W]'), TotalFaresWeekly["Suburban"], marker="*", color="red", linewidth=2, label='Suburban')

# Add a grid.
plt.grid()

#plt.xticks(RuralDateTrialType.index,Rotation="vertical")
# Add the legend.
# Create a legend

lgnd = plt.legend(fontsize="12", mode="Expanded",
         scatterpoints=1, loc="best", title="City Types")
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]
lgnd.get_title().set_fontsize(12)


plt.savefig(os.path.abspath("analysis/module_challenge.png"))

# %%
