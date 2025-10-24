"""Model factory for RandomForest + imputer."""
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer

def create_model():
    """Create model and imputer with sensible defaults."""
    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=2,
        min_samples_leaf=1,
        max_features='sqrt',
        criterion='gini',
        class_weight='balanced',
        random_state=42,
        n_jobs=-1
    )
    imputer = SimpleImputer(strategy="median")
    return model, imputer
