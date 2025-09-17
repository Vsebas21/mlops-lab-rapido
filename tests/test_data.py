from sklearn.datasets import load_iris

def test_iris_has_150_rows_and_4_features():
    X, y = load_iris(return_X_y=True, as_frame=True)
    assert X.shape == (150, 4)
    assert len(y) == 150