import streamlit as st
from resume_analyzer import extract_text_from_pdf, find_skills, compare_skills, get_suggestions

st.set_page_config(page_title="ResumeIQ-AI", page_icon="📄", layout="centered")
st.title("ResumeIQ-AI")
st.write("A simple tool that compares resume skills with the skills mentioned in a job description.")
st.caption("This is a learning project. The matching percentage is not an official ATS score.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste the job description", height=220, placeholder="Paste the job requirements here...")
if st.button("Analyse Resume", type="primary"):
    if uploaded_file is None:
        st.error("Please upload a PDF resume.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        try:
            resume_text = extract_text_from_pdf(uploaded_file.getvalue())
            if not resume_text.strip():
                st.error("No readable text was found. The PDF may be scanned or empty.")
            else:
                resume_skills = find_skills(resume_text)
                job_skills = find_skills(job_description)
                matching, missing, percentage = compare_skills(resume_skills, job_skills)
                st.subheader("Extracted resume text")
                with st.expander("View extracted text"):
                    st.text(resume_text)
                st.subheader("Skills found")
                st.write(", ".join(resume_skills) if resume_skills else "No skills from the current dictionary were found.")
                st.subheader("Comparison")
                st.metric("Keyword skill match", f"{percentage:.1f}%")
                col1, col2 = st.columns(2)
                with col1:
                    st.write("**Matching skills**")
                    st.success(", ".join(matching) if matching else "No matching skills found.")
                with col2:
                    st.write("**Skills not found in resume**")
                    st.warning(", ".join(missing) if missing else "No missing skills from the detected job skills.")
                st.subheader("Suggestions")
                for suggestion in get_suggestions(missing, resume_text):
                    st.write(f"- {suggestion}")
                st.info("The percentage compares detected skills only. It does not assess formatting, experience quality, seniority, or any employer's ATS rules.")
        except Exception as error:
            st.error(f"Could not analyse this file: {error}")
