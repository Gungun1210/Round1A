import re
from titles import is_noise

def is_heading(text):
    if not text or is_noise(text):
        return False
    if re.match(r'^\d+(\.\d+)*\s+.+', text): 
        return True
    if re.match(r'^\d+\.\s+.+', text):     
        return True
    if text.strip().lower() in [
        "revision history", "table of contents", "acknowledgements",
        "introduction", "references", "glossary"
    ]:
        return True
    if 3 < len(text.split()) <= 10 and text[0].isalpha():
        return True
    return False

def get_level(text):
    if re.match(r'^\d+\.\d+', text): return "H2"
    if re.match(r'^\d+\.', text): return "H1"
    return "H1"

def extract_headings(doc):
    headings = []
    seen = set()
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                line_text = " ".join([span["text"].strip() for span in line.get("spans", [])]).strip()
                if not line_text or line_text in seen:
                    continue
                if is_heading(line_text):
                    seen.add(line_text)
                    headings.append({
                        "level": get_level(line_text),
                        "text": line_text + (" " if not line_text.endswith(" ") else ""),
                        "page": page_num
                    })
    return headings
