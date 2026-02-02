#Collected dataset from Kaggel "Student marks"
#install pandas, matplotlib, seaborn packages
# pip install pandas matplotlib seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset.csv")

# Basic analysis
print("First 5 rows:\n", df.head())
print("\nDataset Info:")
print(df.info())
print("\nStatistical Summary:\n", df.describe())

# Calculate average of a numeric column
numeric_column = df.select_dtypes(include='number').columns[0]
average_value = df[numeric_column].mean()
print(f"\nAverage of {numeric_column}: {average_value}")

# Bar Chart
df[numeric_column].value_counts().head(10).plot(kind='bar')
plt.title("Bar Chart")
plt.show()

# Scatter Plot
if len(df.select_dtypes(include='number').columns) >= 2:
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1])
    plt.title("Scatter Plot")
    plt.xlabel(df.columns[0])
    plt.ylabel(df.columns[1])
    plt.show()

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
