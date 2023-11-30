import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("crime_data.csv")

plt.figure(figsize=(10, 6))
plt.scatter(data["Violent"], data["Forcible Rape"])
plt.xlabel("Violent Crime")
plt.ylabel("Forcible Rape")
plt.title("Correlation between Violent Crime and Forcible Rape")
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.scatter(data["Burglary"], data["Forcible Rape"])
plt.xlabel("Burglary")
plt.ylabel("Forcible Rape")
plt.title("Correlation between Burglary and Forcible Rape")
plt.grid(True)

plt.figure(figsize=(10, 6))
plt.scatter(data["Aggravated Assault"], data["Forcible Rape"])
plt.xlabel("Aggravated Assault")
plt.ylabel("Forcible Rape")
plt.title("Correlation between Aggravated Assault and Forcible Rape")
plt.grid(True)

plt.tight_layout()
plt.show()

correlation_violent = data["Violent"].corr(data["Forcible Rape"])
correlation_burglary = data["Burglary"].corr(data["Forcible Rape"])
correlation_aggravated_assault = data["Aggravated Assault"].corr(data["Forcible Rape"])

exists_violent_correlation = abs(correlation_violent) > 0.5
exists_burglary_correlation = abs(correlation_burglary) > 0.5
exists_aggravated_assault_correlation = abs(correlation_aggravated_assault) > 0.5

print("Exists Violent Correlation: ", exists_violent_correlation)
print("Exists Burglary Correlation: ", exists_burglary_correlation)
print("Exists Aggravated Assault Correlation: ", exists_aggravated_assault_correlation)
print(f"Correlation between Forcible Rape and Violent: {correlation_violent:.3f}")
print(f"Correlation between Forcible Rape and Burglary: {correlation_burglary:.3f}")
print(f"Correlation between Forcible Rape and Aggravated Assault: {correlation_aggravated_assault:.3f}")
