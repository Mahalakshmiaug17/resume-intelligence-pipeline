Resume & CSV Intelligence Pipeline

An intelligent data processing system that parses resumes and CSV files, normalizes structured data, merges inputs, resolves conflicts, and generates validated, confidence-scored JSON output.

Features

- 📄 CSV Parsing with structured extraction
- 📑 Resume Parsing (unstructured → structured data)
- 🔄 Data Normalization across multiple sources
- 🔗 Intelligent Merging of candidate profiles
- ⚖️ Conflict Resolution using confidence scoring
- 📊 Confidence Score assignment for each field
- 🧾 Data Provenance tracking (source transparency)
- ✅ Schema Validation for clean outputs
- ⚙️ Runtime Config support for flexible execution
- 📦 Final JSON output generation

---

System Pipeline

Input (CSV / Resume)
        ↓
Parsing Layer
        ↓
Normalization Layer
        ↓
Merge Engine
        ↓
Conflict Resolver
        ↓
Confidence Scoring
        ↓
Validation Layer
        ↓
Final JSON Output

Project Structure
project-root/
│
├── parser/
│ ├── csv_parser.py
│ ├── resume_parser.py
│
├── core/
│ ├── normalize.py
│ ├── merge.py
│ ├── conflict_resolver.py
│ ├── confidence.py
│
├── utils/
│ ├── validation.py
│ ├── config.py
│
├── output/
│ ├── sample_output.json
│
├── main.py
├── requirements.txt
└── README.md

Installation

```bash
git clone <repo-link>
cd project-root
pip install -r requirements.txt

Usage
python main.py

This will:

Parse input files
Process and normalize data
Merge profiles
Resolve conflicts
Output final structured JSON

Sample Output
{
  "name": "John Doe",
  "email": "john@example.com",
  "skills": ["Python", "Machine Learning"],
  "experience": [
    {
      "company": "ABC Corp",
      "role": "Data Analyst",
      "confidence": 0.92,
      "source": "resume"
    }
  ],
  "overall_confidence": 0.89
}

Design Highlights
Confidence-based conflict resolution instead of overwrite logic
Source tracking for every field (provenance-aware system)
Modular architecture for easy scaling
Strict validation layer before final output

Notes
Designed for internship-level data engineering / backend assessment
Focus on correctness, traceability, and structured output quality

Final Status

✔ All core modules completed
✔ Validation + confidence system implemented
✔ Production-ready JSON output pipeline