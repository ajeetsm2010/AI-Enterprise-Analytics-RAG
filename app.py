import os
import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st
from dotenv import load_dotenv
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

# Local module imports
from llm.sql_generator import generate_sql

# Load environment variables
load_dotenv()

# Streamlit Page Configuration
st.set_page_config(
    page_title="Enterprise AI Analytics Platform",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for Professional UI Polish
st.markdown("""
<style>

/* Main App */
.main {
    background-color: #F8FAFC;
}

/* Header */
.main-header{
    font-size:42px;
    font-weight:800;
    color:#2563EB;
    margin-bottom:0px;
}

.sub-header{
    color:#64748B;
    font-size:18px;
    margin-bottom:30px;
}

/* KPI Cards */
div[data-testid="metric-container"]{
    background:white;
    border:1px solid #E2E8F0;
    padding:20px;
    border-radius:14px;
    box-shadow:0 4px 15px rgba(0,0,0,.06);
}

/* Dataframe */
[data-testid="stDataFrame"]{
    border-radius:12px;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0F172A;
}

section[data-testid="stSidebar"] *{
    color:white;
}

/* Buttons */
.stButton>button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:8px;
}

.stButton>button:hover{
    background:#1D4ED8;
}

/* Chat */
.stChatMessage{
    border-radius:10px;
    padding:10px;
}

</style>
""", unsafe_allow_html=True)

# Title & Description
st.markdown('<div class="main-header">📊 Enterprise AI Analytics & RAG Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Ask natural language questions to analyze database records, run dynamic SQL, and generate instant business insights.</div>', unsafe_allow_html=True)

# Sidebar Branding & File Upload Setup
st.sidebar.markdown("# 📊 Enterprise AI")
st.sidebar.caption("Business Analytics Platform")
st.sidebar.divider()

uploaded_file = st.sidebar.file_uploader(
    "📂 Upload Business File", 
    type=["csv", "xlsx", "xls"]
)

# Database Connection Setup (In-Memory SQLite)
conn = sqlite3.connect(":memory:", check_same_thread=False)

dash_df = None

if uploaded_file is not None:
    try:
        file_name = uploaded_file.name
        
        # Multi-format Data Reader Logic
        if file_name.endswith('.csv'):
            dash_df = pd.read_csv(uploaded_file)
        elif file_name.endswith(('.xlsx', '.xls')):
            dash_df = pd.read_excel(uploaded_file)
        else:
            st.sidebar.error("Unsupported file format!")
            dash_df = None

        if dash_df is not None:
            # Save into SQLite table named 'uploaded_data'
            dash_df.to_sql("uploaded_data", conn, if_exists="replace", index=False)
            
            st.sidebar.success(f"✅ Successfully loaded `{file_name}` ({len(dash_df)} rows)")
            
            # Show Dataset Preview in Sidebar
            with st.sidebar.expander("👀 View Dataset Schema"):
                st.write("**Columns:**", list(dash_df.columns))
                st.dataframe(dash_df.head(3), use_container_width=True)

            # ===============================================
            # 📊 KPI DASHBOARD METRICS SECTION
            # ===============================================
            st.subheader("📌 Overview Metrics")
            m1, m2, m3, m4 = st.columns(4)

            m1.metric("📄 Total Records", len(dash_df))
            
            numeric_cols_dash = dash_df.select_dtypes(include="number").columns.tolist()
            if numeric_cols_dash:
                revenue = dash_df[numeric_cols_dash[0]].sum()
                avg = dash_df[numeric_cols_dash[0]].mean()

                m2.metric(
                    "📈 Total",
                    f"{revenue:,.2f}"
                )
                m3.metric(
                    "📊 Average",
                    f"{avg:,.2f}"
                )
            else:
                m2.metric("📈 Total", "N/A")
                m3.metric("📊 Average", "N/A")

            m4.metric(
                "🧩 Columns",
                len(dash_df.columns)
            )
            st.divider()
            # ===============================================

    except Exception as e:
        st.sidebar.error(f"Error loading file: {e}")

else:
    st.info("👈 Please upload a business data file (e.g., `Stores.csv`) from the sidebar to begin analysis.")

# PDF Generator Helper Function
def generate_pdf(dataframe):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    elements = []

    table_data = [list(dataframe.columns)] + dataframe.values.tolist()

    table = Table(table_data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.grey),
        ("TEXTCOLOR",(0,0),(-1,0),colors.whitesmoke),
        ("GRID",(0,0),(-1,-1),1,colors.black),
        ("BACKGROUND",(0,1),(-1,-1),colors.beige),
        ("FONTSIZE",(0,0),(-1,-1),8)
    ]))

    elements.append(table)
    doc.build(elements)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf

# Main Query Interface
user_query = st.chat_input("Ask a question about your data (e.g., 'Which store has the maximum capacity?')...")

if user_query:
    st.markdown(f"### 💬 Question: *\"{user_query}\"*")
    
    # 1. Dynamic Schema Extraction & SQL Query Generation
    with st.spinner("Generating SQL query..."):
        if dash_df is not None:
            schema_info = "\n".join(
                [f"{col} ({dash_df[col].dtype})" for col in dash_df.columns]
            )
        else:
            schema_info = "store_id, store_name, city, locality, capacity, latitude, longitude"
            
        sql_query = generate_sql(user_query, schema=schema_info)
    
    # Display Generated SQL
    st.subheader("⚡ Generated SQL")
    st.code(sql_query, language="sql")
    
    # 2. Execute SQL on SQLite Database
    if sql_query:
        try:
            df = pd.read_sql_query(sql_query, conn)
            
            st.subheader("📊 Query Results")
            st.dataframe(df, use_container_width=True)
            
            # Download Buttons (CSV & PDF)
            col1, col2 = st.columns(2)
            
            with col1:
                csv = df.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="📥 Download Results (CSV)",
                    data=csv,
                    file_name="query_results.csv",
                    mime="text/csv",
                    use_container_width=True
                )
                
            with col2:
                if not df.empty:
                    pdf = generate_pdf(df)
                    st.download_button(
                        label="📄 Download Report (PDF)",
                        data=pdf,
                        file_name="query_report.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )
            
            # ===============================================
            # 📈 AUTO CHARTS FEATURE (PLOTLY)
            # ===============================================
            if not df.empty:
                numeric_cols = df.select_dtypes(include="number").columns
                categorical_cols = df.select_dtypes(include="object").columns

                if len(numeric_cols) > 0 and len(categorical_cols) > 0:
                    st.subheader("📈 Auto Visualization")
                    fig = px.bar(
                        df,
                        x=categorical_cols[0],
                        y=numeric_cols[0],
                        title=f"{numeric_cols[0]} by {categorical_cols[0]}"
                    )

                    st.plotly_chart(
                        fig,
                        use_container_width=True
                    )
            # ===============================================

            # 3. AI Business Insight Engine
            st.subheader("💡 Business Insight")
            if df.empty:
                st.warning("No records found for the given query.")
            else:
                if "capacity" in df.columns:
                    max_val = df["capacity"].max()
                    st.success(
                        f"""
### 📌 Business Insight

Maximum Store Capacity:

**{max_val:,} Units**

Recommendation:

Prioritize inventory allocation and workforce planning for high-capacity fulfillment centers.
"""
                    )
                else:
                    st.info("The query successfully extracted targeted records from the database. Use these aggregated data points for operational planning and resource distribution.")
                    
        except Exception as e:
            st.error(f"❌ SQL Execution Error: {e}")

# Footer
st.divider()
st.caption(
    "Built with ❤️ using Python • Streamlit • SQLite • Plotly • ReportLab"
)