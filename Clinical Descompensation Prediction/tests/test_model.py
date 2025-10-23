from src.model import create_model

def test_create_model_and_imputer():
    model, imputer = create_model()
    assert hasattr(model, 'fit')
    assert hasattr(imputer, 'fit')
