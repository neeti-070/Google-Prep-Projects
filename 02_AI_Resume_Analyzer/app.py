import streamlit as st
import PyPDF2
import spacy

st.set_page_config(page_title="AI Resume Analyzer", page_icon="🧠", layout="wide")

nlp = spacy.load("en_core_web_sm")

st.title("🧠 AI Resume Analyzer")
st.write("Upload your resume (PDF) and get an instant skill & experience analysis!")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    doc = nlp(text)

    st.subheader("🔍 Extracted Information")

    # Extract skills (basic keywords)
    skills_keywords = ["python", "java", "machine learning", "data", "ai", "react", "cloud", "sql", "c++", "html"]
    found_skills = [word for word in skills_keywords if word.lower() in text.lower()]
    st.write(f"**Skills Detected:** {', '.join(found_skills) if found_skills else 'No skills found'}")

    # Experience check
    experience = [sent.text for sent in doc.sents if "experience" in sent.text.lower()]
    if experience:
        st.write("**Experience Details:**")
        for e in experience:
            st.write(f"- {e}")
    else:
        st.write("No experience information detected.")

    # Education check
    education = [sent.text for sent in doc.sents if "B.Tech" in sent.text or "M.Tech" in sent.text or "degree" in sent.text]
    if education:
        st.write("**Education Details:**")
        for e in education:
            st.write(f"- {e}")
    else:
        st.write("No education details found.")

    st.success("✅ Resume analysis complete!")