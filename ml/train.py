from sklearn.ensemble import RandomForestClassifier
import joblib

X = [
    [120, 5, 80],
    [60, 1, 10],
    [150, 7, 95],
    [50, 1, 5]
]
y = [1, 0, 1, 0]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "ml/model.pkl")
print("ML Model trained")
