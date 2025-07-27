import re

def is_noise(line):
    
    noise_keywords = [
        "version", "page", "copyright", "confidential", "draft",
        "©", "™", "®", "jan", "feb", "mar", "apr", "may", "jun", "jul",
        "aug", "sep", "oct", "nov", "dec", "2013", "2014", "2020", "2021", "2022", "2023", "2024"
    ]
    if any(word in line.lower() for word in noise_keywords):
        return True
    if re.match(r"\d{1,2} [A-Z]{3,9} \d{4}", line):  # e.g., 10 DECEMBER 2023
        return True
    if re.match(r"^\d{4}$", line.strip()):  # Year-only
        return True
    return False

def is_multilingual(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3040-\u30ff\u0600-\u06FF\u0900-\u097F\u0400-\u04FF]', text))

def extract_title(doc):
    first_page = doc[0]
    blocks = first_page.get_text("dict")["blocks"]
    title_lines = []

    for block in blocks:
        for line in block.get("lines", []):
            for span in line["spans"]:
                size = span.get("size", 0)
                text = span.get("text", "").strip()
                if size >= 14 and len(text) > 5 and not is_noise(text):
                    title_lines.append(text)

    if not title_lines:
        largest = ""
        max_size = 0
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    size = span.get("size", 0)
                    text = span.get("text", "").strip()
                    if size > max_size and len(text) > 5 and not is_noise(text):
                        max_size = size
                        largest = text
        title_lines.append(largest)

    return " ".join(title_lines).strip()
