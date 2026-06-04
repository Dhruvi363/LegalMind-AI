import streamlit as st

from app.graph.workflow import graph

st.set_page_config(
    page_title="AI Legal Assistant",
    layout="wide"
)

st.title("AI Legal Assistant")

query = st.text_area(
    "Describe your legal issue",
    height=200
)

if st.button("Analyze Case"):

    if query.strip():

        with st.spinner("Analyzing..."):

            result = graph.invoke(
                {
                    "user_query": query
                }
            )

        st.subheader("Category")
        st.write(result.get("legal_category", ""))

        st.subheader("IPC/BNS Sections")
        st.write(result.get("ipc_sections", ""))

        st.subheader("Legal Analysis")
        st.write(result.get("analysis", ""))

        st.subheader("Draft Complaint")
        st.write(result.get("draft_document", ""))

    else:
        st.warning("Please enter a legal issue.")