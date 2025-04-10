with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

new_dataset = generate_dataset(20)
X_new = np.array([calculate_entropy(data) for data, _ in new_dataset]).reshape(-1, 1)
y_true = np.array([label for _, label in new_dataset])

y_pred = model.predict(X_new)
accuracy = accuracy_score(y_true, y_pred)

print(f"Evaluation Accuracy: {accuracy * 100:.2f}%")