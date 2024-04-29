import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
x = np.random.rand(100)  # Generate 100 random numbers between 0 and 1
y = 2 * x + 1 + np.random.randn(100)  # Apply a linear relationship with noise

# Create the scatter plot
plt.figure(figsize=(8, 6))  # Set the figure size
plt.scatter(x, y)  # Create the scatter plot

# Add labels and title
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simulated Data")

# Show the plot
plt.grid(True)  # Add a grid for better readability
plt.savefig("plot.png")


# read csv file annual-temp-anomalies.csv and plot the data


import pandas as pd
data = pd.read_csv("annual-temp-anomalies.csv")


plt.figure(figsize=(8, 6))


sources = data["Source"].unique()  # Get unique sources
for source in sources:
    source_data = data[data["Source"] == source]  # Filter data for each source
    plt.plot(source_data["Year"], source_data["Mean"], label=source)  # Plot line for each source

plt.xlabel("Year")
plt.ylabel("Temperature Anomaly (°C)")
plt.title("Global Temperature Anomalies")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("temp_plot.png")

