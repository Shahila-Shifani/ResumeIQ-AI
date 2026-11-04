import fitz
from skills import SKILL_TERMS

def extract_text_from_pdf(pdf_bytes):
    """Return readable text from the pages of a PDF file."""
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    pages = [page.get_text() for page in document]
    document.close()
    return "\n".join(pages).strip()

def find_skills(text):
    """Find known skills using case-insensitive whole-word matching."""
    import re
    found = []
    for skill in SKILL_TERMS:
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text, flags=re.IGNORECASE):
            found.append(skill)
    return sorted(found)

def compare_skills(resume_skills, job_skills):
    matching = sorted(set(resume_skills) & set(job_skills))
    missing = sorted(set(job_skills) - set(resume_skills))
    percentage = (len(matching) / len(set(job_skills)) * 100) if job_skills else 0
    return matching, missing, percentage

def get_suggestions(missing_skills, resume_text):
    suggestions = []
    if missing_skills:
        suggestions.append("If you genuinely have experience with these skills, add clear examples: " + ", ".join(missing_skills) + ".")
    if len(resume_text.split()) < 80:
        suggestions.append("Your extracted resume text is quite short. Check that the PDF contains selectable text and all relevant sections.")
    suggestions.append("Use measurable examples where possible, and tailor your experience to the job description without adding skills you do not have.")
    return suggestions
