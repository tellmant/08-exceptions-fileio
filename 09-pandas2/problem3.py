import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("crime_data.csv")

data.plot(kind="box", y=['Burglary', 'Violent', 'Vehicle Theft'])
plt.ylabel('Crime Frequency')
plt.title('Distributions of Crimes')

data.plot(kind="hexbin", x='Vehicle Theft', y='Robbery', gridsize=15, sharex=False)
plt.title('Distributions of Vehicle Thefts by Robberies')

plt.tight_layout()
plt.show()
