Drive link for entire file : 

**Candidate Data Transformer (Resume + CSV Intelligence Pipeline)
**
A modular data processing system that extracts, normalizes, merges, and validates structured candidate information from both structured (CSV) and unstructured (resume text) sources.
It resolves conflicts using confidence scoring, maintains provenance tracking, and outputs clean validated JSON.

**Features**
- 📄 CSV Data Parsing (structured input)
- 📑 Resume Text Parsing (unstructured input)
- 🔄 Data Normalization (email, phone, skills)
- 🔗 Multi-source Merge Engine
- ⚖️ Conflict Resolution using confidence scoring
- 📊 Confidence Score assignment per field
- 🧾 Provenance tracking (source transparency)
- ✅ Output validation before final result
- 📦 Clean JSON output generation

 **Project Structure**
 candidate-data-transformer/
│
├── input/
│   ├── recruiter.csv
│   ├── resume.pdf
│
├── config/
│   └── config.json
│
├── output/
│   └── candidate.json
│
├── parsers/
│   ├── csv_parser.py
│   └── pdf_parser.py
│
├── services/
│   ├── normalizer.py
│   ├── merger.py
│   ├── confidence.py
│   └── validator.py
│
├── models/
│   └── candidate.py
│
├── main.py
├── requirements.txt
└── README.md

**Installation**
1. Clone the repository
2. Install dependencies - pip install -r requirements.txt

**How to Run**
Run the full pipeline: python main.py

**Input Sources**
1. CSV Input (recruiter.csv)
2. Resume Input(Resume.pdf)

**Output**
**
========== Candidate Data Transformer ==========
========== CSV Data ==========
{
    "full_name": "Mahalakshmi S",
    "email": "maha@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Python",
        "Java",
        "SQL"
    ],
    "experience": "2 Years"
}
========== Resume Data ==========
{
    "full_name": "Mahalakshmi S",
    "email": "maha@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Python",
        "Java",
        "SQL"
    ],
    "experience": "2 Years"
}
========== Merged Candidate Profile ==========
{
    "full_name": "Mahalakshmi S",
    "email": "maha@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Python",
        "Java",
        "SQL"
    ],
    "experience": "2 Years"
}

========== Confidence Scores ==========
{
    "full_name": 1.0,
    "email": 1.0,
    "phone": 1.0,
    "skills": 1.0,
    "experience": 1.0
}
========== Provenance ==========
{
    "full_name": "Both",
    "email": "Both",
    "phone": "Both",
    "skills": "Both",
    "experience": "Both"
}
========== Final Standard JSON ==========
{
    "full_name": {
        "value": "Mahalakshmi S",
        "confidence": 1.0,
        "source": "Both"
    },
    "email": {
        "value": "maha@gmail.com",
        "confidence": 1.0,
        "source": "Both"
    },
    "phone": {
        "value": "+91 9876543210",
        "confidence": 1.0,
        "source": "Both"
    },
    "skills": {
        "value": [
        "Python",
        "Java",
            "SQL"
        ],
        "confidence": 1.0,
        "source": "Both"
    },
    "experience": {
        "value": "2 Years",
        "confidence": 1.0,
        "source": "Both"
    }
}
Final JSON saved to output/final_profile.json

========== Validation Results ==========
{
    "full_name": "Valid",
    "email": "Valid",
    "phone": "Valid",
    "skills": "Valid",
    "experience": "Valid"
}
Project completed successfully!
**

**Edge cases **

1.Missing email in one source
2.Multiple phone numbers
3.Different spellings of candidate name
4.Duplicate skills
5.Conflicting work experience
6.Empty fields
7.Invalid phone/email formats

**How to Use in Real Systems**

This pipeline can be extended for:
HR onboarding systems
Resume ranking tools
Candidate matching engines
Data cleaning pipelines

**Status**
✔ Parsing implemented
✔ Normalization implemented
✔ Merge + conflict resolution implemented
✔ Confidence scoring implemented
✔ Validation added
✔ CLI execution ready
