

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student Marks Detection App", layout="wide")

st.title("🎓 Student Marks Detection Application")

uploaded_file = st.file_uploader("Upload Student Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Uploaded Dataset")
    st.dataframe(df.head())

    # Calculate correct total and result
    df["Calculated_Total"] = df["Maths"] + df["Science"] + df["English"] + df["History"] + df["Computer"]
    df["Calculated_Result"] = df["Calculated_Total"].apply(lambda x: "Pass" if x >= 200 else "Fail")

    # Check correctness
    df["Marks_Correct"] = df["Total"] == df["Calculated_Total"]
    df["Result_Correct"] = df["Result"] == df["Calculated_Result"]

    st.subheader("✅ Validation Output")
    st.dataframe(df)

    st.subheader("🔍 Filters")

    result_filter = st.selectbox("Select Pass/Fail", ["All", "Pass", "Fail"])

    if result_filter != "All":
        df = df[df["Calculated_Result"] == result_filter]

    correctness_filter = st.selectbox("Select Correctness", ["All", "Correct", "Incorrect"])

    if correctness_filter == "Correct":
        df = df[(df["Marks_Correct"] == True) & (df["Result_Correct"] == True)]
    elif correctness_filter == "Incorrect":
        df = df[(df["Marks_Correct"] == False) | (df["Result_Correct"] == False)]

    st.subheader("📊 Filtered Records")
    st.dataframe(df)

    st.write("Total records:", len(df))