# ResumeIQ-AI

## 1. About the project
ResumeIQ-AI is a small Streamlit application that reads a text-based PDF resume and compares its detected skills with a job description.

## 2. Problem statement
Applicants may overlook skills mentioned in a job advertisement. This project gives a simple checklist of detected matching and missing terms.

## 3. Features
- Upload and read a PDF resume.
- Paste a job description.
- Detect skills from an editable dictionary.
- Show matching skills, missing skills and a keyword match percentage.
- Give basic improvement suggestions.

The percentage is not an official ATS score and should not be used to predict whether an employer will shortlist someone.

## 4. Technologies used
Python, Streamlit, PyMuPDF and regular expressions.

## 5. Project folder structure
See the folders and files in this repository. `app.py` contains the interface, `resume_analyzer.py` contains the analysis functions and `skills.py` contains the editable skill list.

## 6. How to install
Use Python 3.10 or later.

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## 7. How to run
```bash
streamlit run app.py
```
Open the local URL printed in the terminal.

## 8. How it works
PyMuPDF reads selectable text from each PDF page. Regular expressions look for terms in `skills.py`. The program compares two sets of detected skills. The percentage is matching job-description skills divided by all detected job-description skills.

## 9. Screenshots
The `screenshots/` folder contains instructions. Capture your own screenshot after running the app; no sample screenshot is presented as a real app capture.

## 10. What I learned
PDF text extraction, functions, lists and sets, regular expressions, basic text matching, input validation and Streamlit.

## 11. Limitations
- Scanned PDFs need OCR, which is not included.
- Skill matching depends on the dictionary and exact wording.
- It does not understand context, skill proficiency, work history or ATS formatting.
- A listed missing skill may be present under a different name.

## 12. Future improvements
Add OCR, synonyms, editable skill categories and a more advanced semantic comparison.

## 13. Dataset/API credits
No external dataset or API is required. Only use resumes that you have permission to process.
