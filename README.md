# 🧠 Name Matching System using Vector Search (FAISS + Sentence Transformers)

This project implements a **name-matching system** that finds the most similar names from a dataset using **Vector Search (FAISS)** and **Sentence Embeddings**.

---

## 📁 Project Folder Structure

name-matching-vector/
│
├── name_match.py # Main script to run via command line (CLI)
├── name_match_app.py # Optional Streamlit version for web interface
├── requirements.txt # Required Python packages
├── sample_output.txt # Example input-output test run
└── README.md # Documentation (this file)


---

## 🔧 Requirements

- Python 3.8 or above
- Internet connection (for downloading model)
- No external servers or APIs required
- Works on Windows, Linux, or Mac

---

## 📦 Installation Steps

### ✅ Step 1: Open Terminal / Command Prompt

Navigate to your project folder:

```bash
cd name-matching-vector


✅ Step 2: Install Dependencies
Install required libraries:

pip install -r requirements.txt


If requirements.txt is missing, you can install manually:


pip install sentence-transformers faiss-cpu streamlit numpy



▶️ How to Run the Project
💻 Option 1: Run via Command Line
This version works in the terminal. Run:


python name_match.py




Input Example:

Enter a name: Githa



Output:


✅ Best Match:
Geetha (Score: 0.9853)

📋 Top Similar Names:
1. Geetha       - Score: 0.9853
2. Gita         - Score: 0.9741
3. Gitu         - Score: 0.9633
4. Geetanjali   - Score: 0.9348
5. Githika      - Score: 0.9085



📂 Files Explanation


| File Name           | Description                                    |
| ------------------- | ---------------------------------------------- |
| `name_match.py`     | Command-line version of name matcher           |
| `name_match_app.py` | Optional Streamlit-based web app version       |
| `requirements.txt`  | Python dependencies for both CLI and web app   |
| `sample_output.txt` | Sample test result output for verification     |
| `README.md`         | Complete documentation for setup and execution |





🚀 Features
✅ Fast vector-based name matching with FAISS

🤖 Semantic similarity using transformer embeddings

📊 Displays top 5 closest name matches with scores

🌐 Optional browser-based interface using Streamlit

🛠️ Easily customizable name list

📦 Self-contained, no external API or database required






🧪 Test Plan
To test and verify the project locally:

✅ Download or clone the project folder.

✅ Navigate to the folder using the terminal: cd name-matching-vector

✅ Run: pip install -r requirements.txt

✅ Start the CLI: python name_match.py

✅ Enter any test name (e.g., Githa)

✅ Check the output. If it matches sample_output.txt, your test is successful.