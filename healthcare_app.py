import streamlit as st
import pandas as pd
import plotly.express as px

# ============================
# Title & Headers
# ============================
st.title("Healthcare Web Application")
st.header("Healthcare Data Visualization")
st.write("##### Interactive Healthcare Dashboard using Streamlit & Plotly")
st.markdown("<h2 style='color: green;'>Healthcare Data Analysis</h2>", unsafe_allow_html=True)

# ============================
# Load Dataset
# ============================
st.subheader("Load Cleaned Dataset")

dff = pd.read_csv("mah_test_healthcare_dataset_clean.csv")

st.write("### Sample of Data (Top 5 Rows)")
st.dataframe(dff.head())

# Show all data button
if st.button("Show All Data"):
    st.write("### Full Dataset")
    st.dataframe(dff)

st.markdown("---")

# ============================
# EDA Options
# ============================
st.subheader("Basic EDA Options")

option = st.selectbox(
    "Select Visualization Type:",
    (
        "Age Distribution",
        "Billing Amount Distribution",
        "Medical Condition Counts",
        "Admission Type Counts",
        "Test Results Counts",
        "Age vs Billing (Scatter)"
    )
)

st.markdown("---")

# ============================
# Age Histogram
# ============================
if option == "Age Distribution":
    st.write("### Distribution of Age")
    fig = px.histogram(dff, x="Age", nbins=30, title="Age Distribution")
    st.plotly_chart(fig)

# ============================
# Billing Amount Histogram
# ============================
elif option == "Billing Amount Distribution":
    st.write("### Distribution of Billing Amount")
    fig = px.histogram(dff, x="Billing Amount", nbins=40, title="Billing Amount Distribution")
    st.plotly_chart(fig)

# ============================
# Medical Condition Counts
# ============================
elif option == "Medical Condition Counts":
    st.write("### Count of Medical Conditions")
    df_cnt = dff["Medical Condition"].value_counts().reset_index()
    df_cnt.columns = ["Medical Condition", "Count"]
    fig = px.bar(df_cnt, x="Medical Condition", y="Count", title="Medical Condition Counts")
    st.plotly_chart(fig)

# ============================
# Admission Type Counts
# ============================
elif option == "Admission Type Counts":
    st.write("### Admission Type Counts")
    df_cnt = dff["Admission Type"].value_counts().reset_index()
    df_cnt.columns = ["Admission Type", "Count"]
    fig = px.bar(df_cnt, x="Admission Type", y="Count", title="Admission Type Counts")
    st.plotly_chart(fig)

# ============================
# Test Results Counts
# ============================
elif option == "Test Results Counts":
    st.write("### Test Results Counts")
    df_cnt = dff["Test Results"].value_counts().reset_index()
    df_cnt.columns = ["Test Results", "Count"]
    fig = px.bar(df_cnt, x="Test Results", y="Count", title="Test Results Counts")
    st.plotly_chart(fig)

# ============================
# Age vs Billing (Scatter)
# ============================
elif option == "Age vs Billing (Scatter)":
    st.write("### Age vs Billing Amount")
    fig = px.scatter(
        dff,
        x="Age",
        y="Billing Amount",
        color="Gender",
        size="Length_of_Stay",
        hover_data=["Medical Condition", "Admission Type"],
        title="Age vs Billing Amount"
    )
    st.plotly_chart(fig)

st.markdown("---")

# Footer
st.success("Healthcare Streamlit Application Loaded Successfully!")
