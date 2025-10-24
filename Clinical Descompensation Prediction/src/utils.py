"""General utilities: reports, paths, etc."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generar_reporte_pdf(metrics, output_path="results_report.pdf"):
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
    c = canvas.Canvas(output_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(72, 760, "Reporte de Modelo: Predicción Clínica")
    y = 730
    for label in ("accuracy", "precision_macro", "recall_macro", "f1_macro"):
        val = metrics.get(label, None)
        if isinstance(val, (int, float)):
            c.drawString(72, y, f"{label}: {val:.3f}")
        else:
            c.drawString(72, y, f"{label}: {val}")
        y -= 18
    c.save()
    return output_path
