import streamlit as st
from app.graph.workflow import graph

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="LegalMind AI",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;500;600&display=swap');

/* ── Root variables ── */
:root {
    --ink:        #1a1a2e;
    --ink-soft:   #3d3d5c;
    --gold:       #c9a84c;
    --gold-light: #e8c97a;
    --cream:      #faf8f3;
    --cream-mid:  #f2ede2;
    --border:     #ddd5c0;
    --red:        #c0392b;
    --green:      #1e6b45;
    --shadow:     rgba(26,26,46,0.08);
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    color: var(--ink);
    background-color: var(--cream);
}

.stApp {
    background-color: var(--cream);
    background-image:
        radial-gradient(ellipse at 0% 0%, rgba(201,168,76,0.07) 0%, transparent 55%),
        radial-gradient(ellipse at 100% 100%, rgba(30,107,69,0.05) 0%, transparent 55%);
    min-height: 100vh;
}

/* ── Hide default streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 2rem !important;
    max-width: 1400px !important;
}

/* ── Collapse all default Streamlit element gaps ── */
.stTextArea, .stButton, [data-testid="stVerticalBlock"] > div {
    margin-bottom: 0 !important;
}
div[data-testid="stVerticalBlock"] > div + div {
    margin-top: 0 !important;
}

/* ── Header ── */
.lm-header {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 1.5rem 0 1.2rem;
    border-bottom: 2px solid var(--border);
    margin-bottom: 1.8rem;
}
.lm-gavel {
    font-size: 2.4rem;
    line-height: 1;
}
.lm-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 700;
    color: var(--ink);
    letter-spacing: -0.5px;
    margin: 0;
    line-height: 1.1;
}
.lm-subtitle {
    font-size: 0.85rem;
    font-weight: 400;
    color: var(--ink-soft);
    margin: 0;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

/* ── Label ── */
.lm-label {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    color: var(--ink-soft);
    margin: 0 0 6px 0;
    display: block;
}

/* ── Textarea override ── */
.stTextArea > label { display: none !important; }
.stTextArea textarea {
    background: #fff !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 6px !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-size: 0.97rem !important;
    color: var(--ink) !important;
    padding: 14px 16px !important;
    box-shadow: inset 0 1px 3px var(--shadow) !important;
    transition: border-color 0.2s !important;
    resize: vertical !important;
    caret-color: #000  !important;
    cursor: text !important;
}
.stTextArea textarea:focus {
    border-color: var(--gold) !important;
    outline: none !important;
    box-shadow: 0 0 0 3px rgba(201,168,76,0.15) !important;
    caret-color: #000  !important;
}

/* ── Button ── */
.stButton > button {
    background: var(--ink) !important;
    color: var(--gold-light) !important;
    border: none !important;
    border-radius: 5px !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
    padding: 0.65rem 2rem !important;
    cursor: pointer !important;
    transition: background 0.2s, transform 0.1s !important;
    white-space: nowrap !important;
    width: 100% !important;
    line-height: 1.2 !important;
}
.stButton > button:hover {
    background: #2d2d4e !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active {
    transform: translateY(0) !important;
}

/* ── Result card ── */
.result-card {
    background: #fff;
    border: 1px solid var(--border);
    border-left: 4px solid var(--gold);
    border-radius: 6px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px var(--shadow);
    transition: box-shadow 0.2s, transform 0.2s;
}
.result-card:hover {
    box-shadow: 0 4px 16px rgba(26,26,46,0.13);
    transform: translateY(-1px);
}
.result-card h4 {
    font-family: 'Playfair Display', serif;
    font-size: 1rem;
    font-weight: 600;
    color: var(--ink);
    margin: 0 0 0.7rem 0;
    display: flex;
    align-items: center;
    gap: 8px;
}
.result-card p, .result-card div {
    font-size: 0.95rem;
    line-height: 1.7;
    color: var(--ink-soft);
    margin: 0;
    white-space: pre-wrap;
}
.result-card.accent-green { border-left-color: var(--green); }
.result-card.accent-red   { border-left-color: var(--red); }
.result-card.accent-blue  { border-left-color: #2c5f8a; }

/* ── Badge ── */
.category-badge {
    display: inline-block;
    background: var(--ink);
    color: var(--gold-light);
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 20px;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: var(--gold) !important;
}

/* ── Warning / error override ── */
.stAlert {
    border-radius: 6px !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-size: 0.9rem !important;
}

/* ── Divider ── */
.lm-divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.5rem 0 1.2rem;
}

/* ── Footer ── */
.lm-footer {
    margin-top: 2.5rem;
    padding-top: 1rem;
    border-top: 1px solid var(--border);
    font-size: 0.75rem;
    color: #aaa;
    text-align: center;
    letter-spacing: 0.5px;
}
            
/* Fix faded markdown content */
.result-card ul,
.result-card ol,
.result-card li {
    color: #1a1a2e !important;
    opacity: 1 !important;
}
            
</style>
""", unsafe_allow_html=True)


# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="lm-header">
    <div class="lm-gavel">⚖️</div>
    <div>
        <p class="lm-title">LegalMind AI</p>
        <p class="lm-subtitle">Intelligent Legal Analysis &amp; Complaint Drafting</p>
    </div>
</div>
""", unsafe_allow_html=True)


# ── Input section ──────────────────────────────────────────────────────────────
st.markdown('<span class="lm-label">Describe your legal issue</span>', unsafe_allow_html=True)

query = st.text_area(
    label="",
    placeholder="e.g. My landlord has been withholding my security deposit for 3 months without any reason...",
    height=180,
    label_visibility="collapsed",
)

analyze = st.button("Analyze Case", use_container_width=True)

st.markdown('<hr class="lm-divider">', unsafe_allow_html=True)


# ── Analysis ───────────────────────────────────────────────────────────────────
if analyze:
    if not query.strip():
        st.warning("Please describe your legal issue before proceeding.")
    else:
        with st.spinner("Analysing your case — this may take a moment..."):
            try:
                result = graph.invoke({"user_query": query})
                
            except Exception as e:
                st.error(f"Analysis failed: {e}")
                st.stop()

        # Category
        category = result.get("legal_category", "—")
        st.markdown(f"""
        <div class="result-card">
            <h4>🗂 Classification</h4>
            <div><span class="category-badge">{category}</span></div>
        </div>
        """, unsafe_allow_html=True)

        # IPC / BNS Sections
        ipc = result.get("ipc_sections", "—")
        st.markdown(f"""
        <div class="result-card accent-red">
            <h4>📋 Applicable IPC / BNS Sections</h4>
            <p>{ipc}</p>
        </div>
        """, unsafe_allow_html=True)




        # Legal Analysis

        
        
        analysis = result.get("analysis", "—")
        st.markdown(f"""
        <div class="result-card accent-blue">
            <h4>🔍 Legal Analysis</h4>
            <p>{analysis}</p>
        </div>
        """, unsafe_allow_html=True)

        # Draft Complaint
        draft = result.get("draft_document", "—")
        st.markdown(f"""
        <div class="result-card accent-green">
            <h4>📝 Draft Complaint</h4>
            <p>{draft}</p>
        </div>
        """, unsafe_allow_html=True)

        # Download
        if draft and draft != "—":
            st.download_button(
                label="⬇ Download Draft (.txt)",
                data=draft,
                file_name="draft_complaint.txt",
                mime="text/plain",
            )


# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="lm-footer">
    LegalMind AI provides general legal information, not legal advice.
    Consult a qualified advocate for guidance specific to your situation.
</div>
""", unsafe_allow_html=True)
