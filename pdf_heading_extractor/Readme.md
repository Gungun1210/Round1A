# PDF Heading Extractor

This project reads a PDF file and creates a structured outline as JSON.  
It finds the **title** and headings (H1, H2, etc.) along with their **page numbers**.

## ✨ Features
-Fully offline and CPU-only
-Supports multiple PDFs in /input
-Font-based heading detection using font-size, font-style (bold), flags
-Dynamically infers heading levels (H1, H2, H3) from font metrics
-Multilingual support (Japanese, Chinese, Arabic, Hindi, Cyrillic, etc.)
-Ignores noise (dates, copyright, page numbers, currency, repeated headers)
-Adds optional confidence scores per heading
-De-duplicates repeated page headers/footers
-Fast: Processes 50-page PDFs in under 10 seconds
-Lightweight: No ML models, ≤200MB, works on 8-core CPU with 16GB RAM
-Dockerized backend, ready to deploy or test



## 🧪 How to Use

### 1. Put your PDFs in the `input` folder.

### 2. Build the Docker container:
```bash
docker build --platform linux/amd64 -t pdf_extractor .
