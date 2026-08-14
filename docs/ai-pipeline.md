# AI & ML Pipeline Documentation

The **AI Career Intelligence Platform** integrates NLP, ML ATS Scoring, RAG (Retrieval-Augmented Generation), and Google Gemini LLMs to process candidate resumes and generate career insights.

---

## Architecture Overview

```
Resume (PDF/DOCX)
      │
      ▼
┌──────────────────┐
│  PDF/DOCX Parser │ (PyPDF2, pdfplumber, python-docx)
└────────┬─────────┘
         │ Extracted Text
         ▼
┌──────────────────┐
│   NLP Engine     │ (Regex, Tokenizer, Skill Taxonomy)
└────────┬─────────┘
         │ Extracted Skills & Sections
         ▼
┌──────────────────┐
│  ATS Calculator  │ (7-Component Weighted Algorithm)
└────────┬─────────┘
         │ ATS Score Breakdown
         ▼
┌──────────────────┐
│  Gemini & RAG    │ (TF-IDF Vector Index + Gemini 1.5 Flash)
└────────┬─────────┘
         │
         ▼
Structured Career Insights (Skill Gaps, Role Recommendations, Cover Letters, Roadmaps)
```

---

## 1. NLP Parser & Extraction Engine
- **Text Extraction**: Converts PDF and DOCX documents to raw text.
- **Section Segmentation**: Regex-based segmenter partitions resumes into `Education`, `Experience`, `Skills`, and `Projects`.
- **Contact Info Extraction**: Regex patterns extract email, phone number, LinkedIn URL, and GitHub profile link.
- **Skill Extraction**: Matches candidate text against a predefined taxonomy of 40+ technical skills (`Python`, `Flask`, `SQL`, `Docker`, `PostgreSQL`, `pytest`, `REST API`, `Git`, `Machine Learning`, `Pandas`, etc.).

---

## 2. ATS Compatibility Scoring Algorithm
The ATS compatibility score (0-100) is calculated using a 7-component weighted formula:

| Component | Weight | Description |
| :--- | :--- | :--- |
| **Skills Match** | **35%** | Ratio of candidate skills matching target role requirements |
| **Keywords Match** | **20%** | Frequency and presence of domain keywords |
| **Resume Structure** | **15%** | Presence of key sections (Contact, Experience, Education, Skills) |
| **Experience Quality**| **10%** | Detection of work metrics, bullet points, and year ranges |
| **Action Verbs** | **10%** | Frequency of high-impact action verbs (*Architected*, *Engineered*, *Optimized*) |
| **Education** | **5%** | Degree/university terminology recognition |
| **Formatting** | **5%** | Word count within ideal bounds (250-900 words) |

---

## 3. RAG Subsystem
- **Document Chunking**: Partitions career knowledge base into semantic chunks.
- **Vector Embeddings**: Generates TF-IDF term frequency vector representations for chunks.
- **Retrieval Index**: Performs cosine similarity search over vector store to inject relevant context into LLM prompts.

---

## 4. LLM Integration
- **Model**: `gemini-1.5-flash` / Google Generative AI
- **Features**:
  - Executive Resume Summarization
  - Customized Cover Letter Generation (Professional, Concise, Technical)
  - Interactive Career Coaching Chatbot
  - Automated Mock Interview Evaluation & Feedback
