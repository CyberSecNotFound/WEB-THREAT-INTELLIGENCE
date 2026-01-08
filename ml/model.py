import joblib

model = joblib.load("ml/model.pkl")

def ml_predict(url, score):
    features = [[len(url), url.count("."), score]]
    return model.predict(features)[0]
