import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file into a pandas dataframe
data = pd.read_csv("Sucrose_0.01M.csv")

# Define the desired wavelengths
wavelengths = [2693, 2694, 2695, 2696, 2697]

# Create a plot for each wavelength
for wavelength in wavelengths:
    # Filter the dataframe to include only the desired wavelength
    df = data[data["Wavelength(nm)"] == wavelength]
    
    # Sort the dataframe by the "Absorbance" column
    df = df.sort_values(by="Absorbance")
    print(df)
    
    # Extract the absorbance values for the wavelength
    absorbance = df["Absorbance"]
    
    # Plot the data for the wavelength
    plt.plot(absorbance, label=f"{wavelength} nm")

# Add a legend to the plot
plt.legend()

# Label the x and y axes
plt.xlabel("Sample Number")
plt.ylabel("Absorbance")

# Add a title to the plot
plt.title("Absorbance vs. Sample Number for Five Wavelengths")

# Adjust the y-axis limits
plt.ylim([-5, 15])

# Show the plot
plt.show()
