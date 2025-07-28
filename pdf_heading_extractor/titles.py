import re

def is_noise(text):
    keywords = [
        "version", "page", "copyright", "confidential", "draft",
        "©", "™", "®", "jan", "feb", "mar", "apr", "may", "jun", "jul",
        "aug", "sep", "oct", "nov", "dec", "2021", "2022", "2023", "2024", "ISTQB"
    ]
    return any(k in text.lower() for k in keywords) or len(text.strip()) <= 4

def extract_title(doc):
    first_page = doc[0]
    blocks = first_page.get_text("dict")["blocks"]
    spans = []

    for block in blocks:
        for line in block.get("lines", []):
            for span in line.get("spans", []):
                size = span["size"]
                text = span["text"].strip()
                if not is_noise(text) and len(text.split()) > 1:
                    spans.append((size, text))

    if not spans:
        return "Untitled"

    spans.sort(reverse=True)
    top_size = spans[0][0]
    title_lines = [text for size, text in spans if abs(size - top_size) <= 1]

    seen = set()
    clean = [t for t in title_lines if t not in seen and not seen.add(t)]
    return "  ".join(clean).strip()
