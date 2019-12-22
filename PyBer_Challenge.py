#%%
# Add Matplotlib inline magic command
%matplotlib inline
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import os

# %%
# Files to load
dirname = os.path.dirname(__file__)
city_data_to_load = os.path.join(dirname, "Resources/city_data.csv")
ride_data_to_load = os.path.join(dirname, "Resources/ride_data.csv")


# %%## Module 5 Challenge
## Create a PyBer Summary DataFrame
# Combine the data into a single dataset

pyber_data_df = pd.merge(ride_data_df, city_data_df, on=["city", "city"])

# Display the DataFrame
pyber_data_df.head()


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
SummaryDF = pd.DataFrame({"Total Rides": Total_Rides, "Total Drivers":TotalDriverDF,  "Total Fares": Total_Fares,
                       "Average Fare per ride":Avg_PerRide, "Average Per Driver": Avg_FarePerDriver})

SummaryDF.index.name = None

SummaryDF



# %%
## Rename columns

pyber_data_df.rename(columns={'city': 'City', 'date':'Date','fare':'Fare', 'ride_id': 'Ride Id','driver_count': 'No. Drivers', 'type':'City Type'}, inplace=True)


# %%
## Set the index to the Date column
# Reorder the columns in the order you want them to appear.
new_column_order = ['Date', 'City', 'Fare', 'Ride Id','No. Drivers', 'City Type']

pyber_data_df = pyber_data_df[new_column_order]


# %%
# Create a new DataFrame for fares and include only the 
##Date, City Type, and Fare columns using the copy() method on the merged DataFrame
new_pyber_data_df  = pyber_data_df[["Date", "City", "Fare", "City Type"]].copy()

# %%'d
new_pyber_data_df.set_index("Date")

# %%
new_pyber_data_df.info()

# %%
FaresDF = new_pyber_data_df.groupby(["City"]).sum()["Fare"]

# %%
new_pyber_data_df.reset_index()

#DateBasedDF = new_pyber_data_df[new_pyber_data_df["Date"] == '2019-01-01'] 

# %%
DateTypes = new_pyber_data_df["Date"].tolist()

# %%
## Create a new DataFrame from the pivot table DataFrame on the given dates '2019-01-01':'2019-04-28' using loc .
Date_fixed = []

for name in DateTypes:
    if len(name.split()) >= 1:
        Date_fixed.append(name.split()[0])

new_pyber_data_df["Date"] =  Date_fixed

new_pyber_data_df.loc[(new_pyber_data_df["Date"] == '2019-01-01') | (new_pyber_data_df["Date"] == '2019-04-28')]

# %%
# Create a new DataFrame by setting the DataFrame you created in Step 11 with 
# resample() in weekly bins, and calculate the sum() of the fares for each week.

from datetime import datetime 

DateTrialType = new_pyber_data_df.copy()

DateTrialType["Date"] = pd.to_datetime(DateTrialType["Date"])

DateTrialType = DateTrialType.set_index(["Date"])

UrbanType = DateTrialType[DateTrialType["City Type"] == "Urban"]
RuralType = DateTrialType[DateTrialType["City Type"] == "Rural"]
SuburbanType = DateTrialType[DateTrialType["City Type"] == "Suburban"]

UrbanDateTrialType = UrbanType.resample("W").sum()
RuralDateTrialType = RuralType.resample("W").sum()
SuburbanDateTrialType = SuburbanType.resample("W").sum()

# %%
# Create a box-and-whisker plot for the urban cities ride count.
#DateTrialType.plot(x="Date", y="Fare")

#plt.style.use('fivethirtyeight')

x_axis = np.arange(len(RuralDateTrialType))

tick_locations = [value for value in x_axis]

# Add a grid.
plt.grid()

plt.figure(figsize=(15,8))
plt.xlabel("Date")
plt.ylabel("Fare($)")

#plt.xticks(RuralDateTrialType.index,Rotation="vertical")

# Create a title. 
plt.title("PyBer Fare by Month")

plt.plot(UrbanDateTrialType.index.to_pydatetime(), UrbanDateTrialType["Fare"], marker="*", color="green", linewidth=2, label='Urban')
plt.plot(RuralDateTrialType.index.to_pydatetime(), RuralDateTrialType["Fare"], marker="*", color="black", linewidth=2, label='Rural')
plt.plot(SuburbanDateTrialType.index.to_pydatetime(), SuburbanDateTrialType["Fare"], marker="*", color="red", linewidth=2, label='Subarban')

# Add the legend.
# Create a legend
lgnd = plt.legend(fontsize="12", mode="Expanded",
         scatterpoints=1, loc="best", title="City Types")
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]
lgnd.get_title().set_fontsize(12)


plt.savefig(os.path.join(dirname,"analysis/module_challenge.png"))

# %%
