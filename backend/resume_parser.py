# import PyPDF2
# import re

# def extract_text(pdf_path):
#     text = ""
#     with open(pdf_path, "rb") as f:
#         reader = PyPDF2.PdfReader(f)
#         for page in reader.pages:
#             text += page.extract_text() or ""
#     return text

# def lexical_analysis(text):
#     text = re.sub(r"[^a-zA-Z ]", " ", text)
#     return text.lower().split()
import PyPDF2
import re


def extract_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text


def lexical_analysis(text):
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    return text.lower().split()


def generate_parse_tree(tokens):
    tree = "RESUME\n"
    tree += " ├── SECTION: Skills\n"
    tree += " ├── SECTION: Projects\n"
    tree += " ├── SECTION: Education\n"
    tree += " ├── SECTION: Achievements\n"
    tree += " └── TOKENS\n"

    for token in tokens[:25]:
        tree += f"     ├── {token}\n"

    return tree


def generate_ir(tokens):
    ir = ""
    for i, token in enumerate(tokens[:25]):
        ir += f"t{i+1} = LOAD '{token}'\n"

    ir += f"\nTOTAL_TOKENS = {len(tokens)}"
    return ir
