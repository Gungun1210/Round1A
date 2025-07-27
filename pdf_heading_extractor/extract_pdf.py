import os
import json
import fitz

from headings import extract_headings
from titles import extract_title

INPUT_FOLDER = "./input"
OUTPUT_FOLDER = "./output"

def process_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    title = extract_title(doc)
    outline = extract_headings(doc)
    return {
        "title": title,
        "outline": outline
    }

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_FOLDER, file)
            output_path = os.path.join(OUTPUT_FOLDER, file.replace(".pdf", ".json"))
            result = process_pdf(input_path)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
