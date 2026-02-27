import os
import re
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib import colors


def clean_text(text):
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\#", "", text)
    text = re.sub(r"\*", "•", text)
    return text


def generate_pdf(report_text):

    filename = os.path.abspath("report.pdf")

    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()

    # Title Style (Default font)
    title_style = ParagraphStyle(
        name="TitleStyle",
        parent=styles["Heading1"],
        fontSize=18,
        alignment=1,
        textColor=colors.darkgreen
    )

    normal_style = styles["Normal"]

    report_text = clean_text(report_text)

    elements.append(
        Paragraph("Farmer Agricultural Benefits Report", title_style))
    elements.append(Spacer(1, 0.4 * inch))

    paragraphs = report_text.split("\n")

    for para in paragraphs:
        if para.strip() != "":
            elements.append(Paragraph(para, normal_style))
            elements.append(Spacer(1, 0.2 * inch))

    doc.build(elements)

    return filename
