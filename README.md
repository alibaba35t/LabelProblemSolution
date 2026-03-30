# 🚀 AffectNet-Toolkit: High-Performance Preprocessing for Labeling

A robust data engineering tool designed to handle the **AffectNet** dataset (20,000+ images). This toolkit solves common real-world data issues such as **path inconsistencies**, **case-sensitivity conflicts** between OS/Cloud environments, and **data leakage** prevention.

---

### 🛠️ Key Features

* **Lightning-Fast File Discovery:** Utilizes `pathlib.rglob` for recursive globbing, offering significantly faster file indexing compared to traditional `os.walk`.
* **Automated Subset Mapping:** Automatically determines and assigns `train` or `test` labels to each row in `labels.csv` based on the physical directory structure.
* **Environment Agnostic:** Automatically handles naming discrepancies (e.g., `Anger/` vs. `anger/`) between local PC storage and cloud environments like **Google Colab** (Kagglehub).
* **Data Integrity Guard:** Identifies and flags duplicate images found in both Train and Test folders to prevent **Data Leakage** and biased model evaluation.

---

### 🧠 The Problem & The Solution

When working with large-scale datasets like AffectNet, `labels.csv` often lacks explicit subset information or contains paths that don't match the actual folder structure due to extraction errors.

| Problem | Solution in this Toolkit |
| :--- | :--- |
| **Slow Indexing** | Switched to `Path.rglob()` for optimized filesystem traversal. |
| **Path Mismatch** | Normalizes directory names to handle lowercase/uppercase conflicts. |
| **Data Leakage** | Logic to detect files existing in both subsets simultaneously. |
| **Missing Files** | Automated validation to skip or log non-existent image paths. |

---

### 📂 Project Structure

```text
.
├── 
│   └── main.py   # Core logic for rglob and path matching
│   └── solve_problem.py # More advanced features like comparison 
├── 
│   └── labels.csv   # main file which was used for pathlib operations
│   └── new_labels*.csv  # files which have subset and other useful features 
├
└── README.md
```

### 🚀 Performance Benchmark
By moving from a standard nested loop approach to a pathlib-based mapping, the processing time for 20,000+ rows was reduced significantly, making the data loading pipeline much smoother for FER (Facial Emotion Recognition) models.

### 📈 Future Goals
* MySQL Integration: Move from CSV to a relational database for faster querying.

* Image Hashing: Implement Perceptual Hashing (pHash) to find visually identical duplicates with different filenames.

* PyPI Readiness: Refactoring the core logic into a reusable library.
