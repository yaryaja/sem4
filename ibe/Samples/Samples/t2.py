import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("Sucrose_0.01M.csv")
wavelength = data["Wavelength(nm)"]
absorbance = data["Absorbance"]
plt.plot(wavelength, absorbance)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.title("UV Spectrum of Sucrose_0.01")
plt.show()
