import json, sys

# Umbral mínimo aceptable (si lo subes, forzarás un FAIL)
MIN_ACC = 0.99

def main():
    with open("artifacts/metrics.json") as f:
        metrics = json.load(f)
    acc = metrics.get("accuracy", 0.0)
    print("Evaluación -> accuracy:", acc)
    if acc < MIN_ACC:
        print("FAIL: accuracy por debajo del umbral", MIN_ACC)
        sys.exit(1)
    print("Evaluación OK")

if __name__ == "__main__":
    main()