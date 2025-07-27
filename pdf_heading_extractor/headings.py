import re

def is_multilingual(text):
    return bool(re.search(r'[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af\u0600-\u06FF\u0900-\u097F\u0400-\u04FF]', text))

def get_level_from_font(size, base_size):
    if size >= base_size + 4:
        return "H1"
    elif size >= base_size + 2:
        return "H2"
    elif size >= base_size:
        return "H3"
    else:
        return "BODY"

def extract_headings(doc):
    outline = []
    seen_texts = set()
    font_sizes = []

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    font_sizes.append(span.get("size", 0))

    if not font_sizes:
        return outline

    font_sizes.sort()
    base_size = font_sizes[len(font_sizes) // 2]

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            for line in block.get("lines", []):
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span.get("size", 0)
                    flags = span.get("flags", 0)

                    if not text or text in seen_texts:
                        continue

                    is_bold = flags in [20, 21, 22]
                    multilingual = is_multilingual(text)

                    if size >= base_size and (is_bold or multilingual or re.match(r'^\d+(\.\d+)*\s', text)):
                        level = get_level_from_font(size, base_size)
                        confidence = round(0.8 + 0.2 * ((size - base_size) / max(1, base_size)), 2)
                        seen_texts.add(text)
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num,
                            "confidence": confidence
                        })

    return outline
