"""Main module.
"""

from docx import Document

from .config import config


def generate_document():
    doc = Document()

    doc.add_paragraph(config["doc_title"])

    doc.save(config["filename"])
