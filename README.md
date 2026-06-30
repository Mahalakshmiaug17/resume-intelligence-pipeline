Drive link for entire file :  https://drive.google.com/drive/folders/1vKk7d9JS8OpkGF4oRURvmokcfDinwELB?usp=sharing 

**Candidate Data Transformer - Intelligent Resume & CSV Processing Pipeline
**
A modular Python-based data processing pipeline that extracts, normalises, merges and validates candidate information from both structured (CSV) and unstructured (Resume PDF) sources. The system intelligently resolves conflicts using confidence scoring, tracks data provenance and generates clean, standardised JSON output for downstream recruitment systems.

## Features

- 📄 CSV Data Parsing (Structured Input)
- 📑 Resume PDF Parsing (Unstructured Input)
- 🔄 Intelligent Data Normalisation
- 📧 Email Case Normalisation
- 📱 Phone Number Standardisation
- 🛠️ Skills Normalisation
- 🔗 Multi-source Candidate Profile Merging
- 🔍 Duplicate Detection
- ⚖️ Conflict Resolution using Confidence Scores
- 📊 Field-level Confidence Scoring
- ⭐ Overall Candidate Confidence Calculation
- 🧾 Provenance Tracking (CSV / Resume / Both / Unknown)
- ⚠️ Automatic Missing Value Handling (`null`)
- ✅ Output Validation
- 📦 Standardised JSON Generation
- 👥 Multiple Candidate Processing Support

## 📂 Project Structure

```text
candidate-data-transformer/

├── input/
│   ├── Recruiter.csv
│   ├── Resume_1.pdf
│   ├── Resume_2.pdf
│   ├── Resume_3.pdf
│
├── output/
│   └── final_profiles.json
│
├── parsers/
│   ├── csv_parser.py
│   └── pdf_parser.py
│
├── services/
│   ├── normaliser.py
│   ├── merger.py
│   ├── confidence.py
│   ├── provenance.py
│   ├── validator.py
│   └── json_generator.py
│
├── schema/
│   └── profile_schema.json
│
├── main.py
├── requirements.txt
└── README.md
```

**Installation**
1. Clone the repository
2. Install dependencies - pip install -r requirements.txt

**How to Run**
Run the full pipeline: python main.py

## Input
The pipeline accepts the following input files:

- 📄 `Recruiter.csv` – Structured candidate information from recruiters.
- 📑 `Resume_1.pdf` – Resume of Candidate 1.
- 📑 `Resume_2.pdf` – Resume of Candidate 2.
- 📑 `Resume_3.pdf` – Resume of Candidate 3.
- ⚙️ `profile_schema.json` – Defines the standard output schema.
  
**Output**
# Candidate Data Transformer

## Sample Output

```text

========== Candidate Data Transformer ==========


======================================
Processing Candidate ID : 1
======================================

========== CSV Data ==========
{
    "id": 1,
    "full_name": "Mahalakshmi S",
    "email": "maha@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Java",
        "Python",
        "Sql"
    ],
    "experience": "2 Years",
    "gender": "Female"
}

========== Resume Data ==========
{
    "full_name": "Mahalakshmi S",
    "email": "maha@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Java",
        "Python",
        "Sql"
    ],
    "experience": "2 Years"
}

========== Merged Candidate Profile ==========
{
    "full_name": "Mahalakshmi S",
    "email": "maha@gmail.com",
    "phone": "+91 9876543210",
    "skills": [
        "Java",
        "Python",
        "Sql"
    ],
    "experience": "2 Years",
    "age": null,
    "gender": "Female"
}

========== Confidence Scores ==========
{
    "full_name": 1.0,
    "email": 1.0,
    "phone": 1.0,
    "skills": 1.0,
    "experience": 1.0,
    "age": 0.6,
    "gender": 0.8
}

========== Provenance ==========
{
    "full_name": "Both",
    "email": "Both",
    "phone": "Both",
    "skills": "Both",
    "experience": "Both",
    "age": "Unknown",
    "gender": "CSV"
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
            "Java",
            "Python",
            "Sql"
        ],
        "confidence": 1.0,
        "source": "Both"
    },
    "experience": {
        "value": "2 Years",
        "confidence": 1.0,
        "source": "Both"
    },
    "age": {
        "value": null,
        "confidence": 0.6,
        "source": "Unknown"
    },
    "gender": {
        "value": "Female",
        "confidence": 0.8,
        "source": "CSV"
    },
    "overall_confidence": 0.96
}

========== Overall Confidence ==========
0.96

========== Validation Results ==========
{
    "full_name": "Valid",
    "email": "Valid",
    "phone": "Valid",
    "skills": "Valid",
    "experience": "Valid",
    "age": "Missing",
    "gender": "Valid"
}
```
### Edge Cases Handled

1. Missing fields → `null`
2. Duplicate data across sources
3. Email case differences
4. Phone numbers with/without country code
5. Duplicate skills removal
6. Empty or invalid values
7. Conflict resolution using confidence scores
8. Multiple candidate support

**Intelligent Normalisation**

The pipeline automatically standardises data before comparison:
~ Converts email addresses to lowercase to avoid false mismatches.
~ Standardises phone numbers (e.g., 9876543210 → +91 9876543210).
~ Removes duplicate skills.
~ Trims extra spaces and handles inconsistent formatting.

**How to Use in Real Systems**

This pipeline can be extended for:
HR onboarding systems
Resume ranking tools
Candidate matching engines
Data cleaning pipelines

**Status**
✔ CSV Parser
✔ Resume PDF Parser
✔ Data Normalisation
✔ Candidate Merge Engine
✔ Duplicate Detection
✔ Confidence Scoring
✔ Overall Confidence Calculation
✔ Provenance Tracking
✔ Missing Value Handling
✔ Output Validation
✔ JSON Generation
✔ Multiple Candidate Support
