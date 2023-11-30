import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('crime_data.csv')

plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Total'])
plt.xlabel('Year')
plt.ylabel('Total Crime Count')
plt.title('Total Crime Count over the Years')
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.plot(data['Year'], data['Violent'], label='Violent', linestyle='--')
plt.plot(data['Year'], data['Property'], label='Property')
plt.xlabel('Year')
plt.ylabel('Crime Count')
plt.title('Violent and Property Crime Count over the Years')
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.hist(data['Vehicle Theft'], bins=20, alpha=0.7, label='Vehicle Theft')
plt.hist(data['Robbery'], bins=20, alpha=0.7, label='Robbery')
plt.hist(data['Violent'], bins=20, alpha=0.7, label='Violent')
plt.xlabel('Crime Count')
plt.ylabel('Frequency')
plt.title('Distribution of Vehicle Theft, Robbery and Violent Count')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
