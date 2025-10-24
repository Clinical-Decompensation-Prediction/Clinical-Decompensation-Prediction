# Models directory

- `best_model.pkl`: mejor modelo vigente.
- `model_v1.pkl`: primera versión persistida.
- `imputer.pkl`: imputador asociado al modelo.

> Estos archivos se generan al ejecutar:
```bash
python -m src.train --data dataset_balanceado_SMOTEENN.csv --out models
```
