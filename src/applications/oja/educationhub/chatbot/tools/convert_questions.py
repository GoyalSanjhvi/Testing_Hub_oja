"""
convert_questions.py

Converts OJA Master Question Taxonomy
into questions.json.
"""

import json
import re
import zipfile
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

KNOWLEDGE_DIR = BASE_DIR / "knowledge"

INPUT_FILE = KNOWLEDGE_DIR / "OJA_Master_Question_Taxonomy_V1.docx"

OUTPUT_FILE = KNOWLEDGE_DIR / "questions.json"


CATEGORY_PATTERN = re.compile(r"^[A-Z]{1,2}\.\s+(.*)")
QUESTION_PATTERN = re.compile(r"^(\d+)\.\s+(.*)")


def category_key(category):

    return (

        category

        .lower()

        .replace("&", "and")

        .replace("/", " ")

        .replace("-", " ")

        .replace(",", "")

        .replace("(", "")

        .replace(")", "")

        .replace(".", "")

        .replace("  ", " ")

        .strip()

        .replace(" ", "_")

    )


def read_docx(file_path):

    from docx import Document

    document = Document(file_path)

    return [

        p.text.strip()

        for p in document.paragraphs

    ]


def read_text(file_path):

    with open(

        file_path,

        "r",

        encoding="utf-8"

    ) as file:

        return [

            line.strip()

            for line in file.readlines()

        ]


# -----------------------------------
# Detect File Type
# -----------------------------------

try:

    with zipfile.ZipFile(INPUT_FILE):

        print("Microsoft Word Detected")

        lines = read_docx(INPUT_FILE)

except zipfile.BadZipFile:

    print("Plain Text Detected")

    lines = read_text(INPUT_FILE)


questions = []

current_category = None


for line in lines:

    if not line:

        continue

    category = CATEGORY_PATTERN.match(line)

    if category:

        current_category = category.group(1).strip()

        continue

    question = QUESTION_PATTERN.match(line)

    if question:

        questions.append({

            "id": int(question.group(1)),

            "category": current_category,

            "category_key": category_key(current_category),

            "question": question.group(2).strip(),

            "priority": "Regression",

            "enabled": True,

            "expected_keywords": [],

            "tags": []

        })


with open(

    OUTPUT_FILE,

    "w",

    encoding="utf-8"

) as file:

    json.dump(

        questions,

        file,

        indent=4,

        ensure_ascii=False

    )


print("=" * 60)

print(f"Questions : {len(questions)}")

print(f"Saved To  : {OUTPUT_FILE}")

print("=" * 60)