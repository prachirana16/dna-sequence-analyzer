# 🧬 DNA Sequence Analyzer

A command-line Python tool for basic DNA sequence analysis — built as a pre-college bioinformatics portfolio project.

---

## 🔍 Features

-  Input validation (only A, T, G, C allowed — with clear error messages)
-  Nucleotide frequency count (A, T, G, C)
-  GC Content calculation (as percentage)
-  Complement strand generation
-  Reverse complement strand generation

---

## ▶️ How to Run

```bash
python dna_analyzer.py
```

Enter any valid DNA sequence when prompted:

```
🧬 Welcome to DNA Sequence Analyzer
Enter the DNA Sequence: ATGCGTATCG

========== DNA SEQUENCE ANALYSIS ==========
Sequence Length       : 10
Adenine  (A) Count    : 2
Thymine  (T) Count    : 3
Guanine  (G) Count    : 3
Cytosine (C) Count    : 2
GC Content            : 50.00%
Complement Strand     : TACGCATAGC
Reverse Complement    : CGATACGCAT
===========================================
```

---

## 📦 Requirements

- Python 3.x
- No external libraries needed

---

## 🗂️ Project Structure

```
dna-sequence-analyzer/
│
├── dna_analyzer.py       # Main analysis script
└── README.md             # Project documentation
```

---

## 🛣️ Roadmap

Planned upgrades in future versions:

- [ ] Nucleotide frequency bar chart (Matplotlib)
- [ ] GC content pie/donut chart
- [ ] Double helix SVG animation
- [ ] React-based web interface with Recharts
- [ ] RNA transcription support
- [ ] FASTA file input support

---

## 💡 Why This Project?

DNA sequence analysis is a foundational task in bioinformatics. This project was built to understand:
- How genetic data is structured (A, T, G, C bases)
- Why GC content matters (stability of DNA strands)
- How complement strands work (basis of DNA replication)

---

## 👩‍💻 Author

**Prachi**
BSc Biotechnology student | Aspiring Bioinformatician
Pre-college GitHub portfolio project — more coming soon!

