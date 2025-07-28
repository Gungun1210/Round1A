import os
import json
import fitz  

from headings import extract_headings
from titles import extract_title

INPUT_FOLDER = "./input"
OUTPUT_FOLDER = "./output"

def process_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        title = extract_title(doc)
        outline = extract_headings(doc)
        return {
            "title": title,
            "outline": outline
        }
    except Exception as e:
        return {
            "title": "Error",
            "outline": [],
            "error": str(e)
        }

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    pdf_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ No PDF files found in the input folder.")
        return

    for file_name in pdf_files:
        input_path = os.path.join(INPUT_FOLDER, file_name)
        output_path = os.path.join(OUTPUT_FOLDER, file_name.replace(".pdf", ".json"))

        print(f"📄 Processing: {file_name}")
        result = process_pdf(input_path)

        with open(output_path, "w", encoding="utf-8") as out_file:
            json.dump(result, out_file, indent=4, ensure_ascii=False)

        print(f"✅ Output saved to: {output_path}")

if __name__ == "__main__":
    main()
