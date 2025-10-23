import os, io

def test_requirements_contains_streamlit():
    path = os.path.join('app', 'requirements.txt')
    assert os.path.exists(path)
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read().lower()
    assert 'streamlit' in txt
