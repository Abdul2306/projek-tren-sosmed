import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 1. Load Data
df = pd.read_csv("PRSA_data_2010.1.1-2014.12.31.csv")

# 2. Pilih Fitur dan Label
features = ['DEWP', 'TEMP', 'PRES', 'Iws', 'Is', 'Ir']  # Parameter lingkungan
target = 'PM2.5'

# Hapus baris dengan nilai kosong
df = df.dropna(subset=[target])

X = df[features]
y = df[target]

# 3. Preprocessing (Normalisasi dan Split)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 4. Model Neural Network
model = Sequential()
model.add(Dense(32, input_dim=X_train.shape[1], activation='relu'))  # Layer input
model.add(Dense(16, activation='relu'))                               # Hidden layer
model.add(Dense(1))                                                   # Output (regresi)

# 5. Kompilasi dan Pelatihan
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

# 6. Evaluasi
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\n✅ Evaluasi Model:")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Error (MAE): {mae}")
