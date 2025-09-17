from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib, json, os
from pathlib import Path

def main():
    X, y = load_iris(return_X_y=True, as_frame=True)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25,
random_state=42, stratify=y)
    model = LogisticRegression(max_iter=400)
    model.fit(Xtr, ytr)

    Path("artifacts").mkdir(exist_ok=True)
    joblib.dump(model, "artifacts/model.pkl")

    acc = accuracy_score(yte, model.predict(Xte))
    with open("artifacts/metrics.json", "w") as f:
        json.dump({"accuracy": acc}, f, indent=2)
    print("Train OK. Accuracy:", acc)

if __name__ == "__main__":
    main()