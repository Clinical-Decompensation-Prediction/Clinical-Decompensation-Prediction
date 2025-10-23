import pandas as pd
from src.data_processing import build_feature_table

def test_build_feature_table_minimal():
    df = pd.DataFrame({
        'patient_id':[1,1,2,2],
        'visit':[1,2,1,2],
        'age':[40,41,60,61],
        'blood_glucose_level':[110,120,150,140],
        'HbA1c_level':[5.6,5.8,7.2,7.0],
        'systolic_bp':[120,130,150,145],
        'diastolic_bp':[80,82,95,90],
        'bmi':[25.0,25.5,30.2,29.8],
        'target':[-1,0,1,2]
    })
    X, y, bounds = build_feature_table(df)
    assert X.shape[1] == 7
    assert y.nunique() == 4
    assert 'pulse_pressure' in X.columns
