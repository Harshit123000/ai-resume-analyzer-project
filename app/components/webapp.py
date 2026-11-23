import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get AI-powered analysis and career suggestions.")

# Sidebar
st.sidebar.title("Navigation")

option = st.sidebar.selectbox(
    "Choose an option",
    ["Resume Analyzer", "Career Recommendation"]
)

# Resume Analyzer
if option == "Resume Analyzer":

    st.header("📑 Upload Your Resume")

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"]
    )

    if uploaded_file is not None:

        st.success("Resume uploaded successfully!")

        st.write("**File name:**", uploaded_file.name)

        if st.button("🔍 Analyze Resume"):

            st.subheader("📊 Resume Analysis")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Resume Score", "78/100")

            with col2:
                st.metric("Skills Found", "8")

            with col3:
                st.metric("Experience", "2 Years")

            st.subheader("🛠️ Skills")

            st.write("""
            ✅ Python  
            ✅ SQL  
            ✅ Machine Learning  
            ✅ Pandas  
            ✅ NumPy
            """)

            st.subheader("💡 Suggestions")

            st.write("""
            - Add more measurable achievements to your projects.
            - Mention relevant ML libraries.
            - Add Git/GitHub experience.
            - Improve the project descriptions.
            """)

# Career Recommendation
elif option == "Career Recommendation":

    st.header("💼 Career Recommendation")

    skills = st.text_area(
        "Enter your skills",
        placeholder="Python, SQL, Machine Learning, Pandas..."
    )

    education = st.text_input("Education")

    if st.button("🎯 Recommend Career"):

        if skills and education:

            st.success("Career analysis completed!")

            st.subheader("Recommended Roles")

            st.write("🔹 Data Analyst")
            st.write("🔹 Data Scientist")
            st.write("🔹 Machine Learning Engineer")

        else:
            st.warning("Please enter your skills and education.")