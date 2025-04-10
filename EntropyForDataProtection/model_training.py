from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import numpy as np

with open('encrypted_dataset.pkl', 'rb') as f:
    dataset = pickle.load(f)

features = [calculate_entropy(data) for data, label in dataset]
labels = [label for _, label in dataset]

X = np.array(features).reshape(-1, 1)
y = np.array(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")