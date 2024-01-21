import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load the dataset
df = pd.read_csv('Drive_data_Jan-Feb.csv')

# Correct negative energy consumption values
df['Energy Consumption (kWh)'] = df['Energy Consumption (kWh)'].abs()

# Introduce anomalies for 1% of the dataset
anomaly_indices = np.random.choice(df.index, size=int(0.01 * len(df)), replace=False)
df.loc[anomaly_indices, 'Torque (Nm)'] *= np.random.uniform(1.5, 3.0)
df.loc[anomaly_indices, 'Energy Consumption (kWh)'] *= np.random.uniform(1.5, 3.0)

# Feature Engineering: Calculate rolling means
df['Torque Rolling Mean'] = df['Torque (Nm)'].rolling(window=5, min_periods=1).mean()
df['Energy Consumption Rolling Mean'] = df['Energy Consumption (kWh)'].rolling(window=5, min_periods=1).mean()

# Normalize the data
scaler = MinMaxScaler()
features_to_scale = ['Torque (Nm)', 'Energy Consumption (kWh)', 'Torque Rolling Mean', 'Energy Consumption Rolling Mean']
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# Split the dataset into features (X) and target (y)
X = df.drop(['Timestamp', 'Maintenance Flag'], axis=1)
y = df['Maintenance Flag']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest Classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Feature Importances
feature_importances = pd.Series(clf.feature_importances_, index=X_train.columns)
print("\nFeature Importances:")
print(feature_importances.sort_values(ascending=False))

# Save the model (optional)
# import joblib
# joblib.dump(clf, 'predictive_maintenance_model.pkl')
