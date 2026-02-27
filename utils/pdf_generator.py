from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors


def generate_pdf(text, filename="report.pdf"):

    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()

    custom_style = ParagraphStyle(
        'Custom',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=12,
        leading=15,
    )

    for line in text.split("\n"):
        elements.append(Paragraph(line, custom_style))
        elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)

    return filename
