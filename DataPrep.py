import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Assuming df is already loaded with the data
# If not, it would need to be reloaded with 
df = pd.read_csv('Drive_data_Jan-Feb.csv')

# Correct the negative energy consumption values and introduce anomalies
# For simplicity, we'll assume any negative value is an error and set it to the absolute value
df['Energy Consumption (kWh)'] = df['Energy Consumption (kWh)'].abs()

# Introduce anomalies for 1% of the dataset
anomaly_indices = np.random.choice(df.index, size=int(0.01 * len(df)), replace=False)

# Increase the torque and energy consumption at these indices to simulate anomalies
df.loc[anomaly_indices, 'Torque (Nm)'] = df.loc[anomaly_indices, 'Torque (Nm)'] * np.random.uniform(1.5, 3.0)
df.loc[anomaly_indices, 'Energy Consumption (kWh)'] = df.loc[anomaly_indices, 'Energy Consumption (kWh)'] * np.random.uniform(1.5, 3.0)

# Feature engineering: Calculate the rolling means
df['Torque Rolling Mean'] = df['Torque (Nm)'].rolling(window=5, min_periods=1).mean()
df['Energy Consumption Rolling Mean'] = df['Energy Consumption (kWh)'].rolling(window=5, min_periods=1).mean()

# Normalize the data using MinMaxScaler to scale the feature to a range [0,1]
scaler = MinMaxScaler()

# Select features to scale
features_to_scale = ['Torque (Nm)', 'Energy Consumption (kWh)', 'Torque Rolling Mean', 'Energy Consumption Rolling Mean']

# Fit the scaler on the features and transform
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Split the dataset into features (X) and target (y)
X = df.drop(['Timestamp', 'Maintenance Flag'], axis=1)  # drop non-feature columns
y = df['Maintenance Flag']  # target column

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Return the first few rows of the dataframe to verify changes
print(df.head())
