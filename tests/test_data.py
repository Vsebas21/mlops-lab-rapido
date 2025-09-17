from sklearn.datasets import load_iris

def test_iris_has_150_rows_and_4_features():
    X, y = load_iris(return_X_y=True, as_frame=True)
    assert X.shape == (150, 4)
    assert len(y) == 150
buildspec.yml
version: 0.2
phases:
    install:
        commands:
            - python -m pip install --upgrade pip
            - pip install -r requirements.txt
            - mkdir -p artifacts
    build:
        commands:
            - echo "1) Pruebas unitarias"
            - pytest -q
            - echo "2) Entrenamiento y generación de métricas"
            - python src/train.py
            - echo "3) Evaluación con umbral"
            - python src/evaluate.py
artifacts:
    files:
        - artifacts/**
    discard-paths: no