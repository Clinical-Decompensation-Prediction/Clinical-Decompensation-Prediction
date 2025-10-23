"""Evaluation helpers for plots."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

CLASS_LABELS = {-1: "Sin enfermedad", 0: "Diabetes", 1: "Hipertensión", 2: "Comorbilidad"}

def plot_confusion_matrix(cm):
    cm_df = pd.DataFrame(
        cm, index=[CLASS_LABELS[i] for i in [-1,0,1,2]],
        columns=[CLASS_LABELS[i] for i in [-1,0,1,2]]
    )
    fig, ax = plt.subplots(figsize=(5,4), dpi=150)
    sns.heatmap(cm_df, annot=True, fmt="d", cmap="Blues", cbar=False, ax=ax)
    ax.set_xlabel("Predicción"); ax.set_ylabel("Real")
    return fig
