#%%
%matplotlib inline
# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Load in csv
pyber_ride_df = pd.read_csv("Resources/PyBer_ride_data.csv")
pyber_ride_df

# %%
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.show()

#%%
x_axis = np.arange(len(pyber_ride_df))
tick_locations = [value for value in x_axis]
tick_locations

# %%
# Set x-axis and tick locations.
x_axis = np.arange(len(pyber_ride_df))
tick_locations = [value for value in x_axis]

# Plot the data.
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)")
plt.xticks(tick_locations, pyber_ride_df["Month"])
plt.show()

# %%
pyber_ride_df.plot.bar(x="Month", y="Avg. Fare ($USD)")
plt.show()

# %%
pyber_ride_df.plot(x="Month", y="Avg. Fare ($USD)", kind='bar')
plt.show()

# %%
import statistics
# Get the standard deviation of the values in the y-axis.
stdev = statistics.stdev(y_axis)

fig, ax = plt.subplots()
ax.bar(x_axis, y_axis, yerr=stdev, capsize=3)
plt.show()


# %%
