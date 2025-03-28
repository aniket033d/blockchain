import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set the page title
st.set_page_config(page_title="Enhanced Streamlit App", layout="wide")

# App title
st.title("Enhanced Streamlit App with Dynamic Features")

# Sidebar for file upload
st.sidebar.header("Upload Your CSV Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    data = pd.read_csv(uploaded_file)
    
    # Display basic data insights
    st.write("### Data Preview", data.head())
    st.write(f"Number of rows: {data.shape[0]}, Number of columns: {data.shape[1]}")
    
    # Show columns for selecting relevant data
    columns = data.columns.tolist()
    st.sidebar.subheader("Select Columns for Visualization")
    
    # Select columns for the x and y axes
    x_axis = st.sidebar.selectbox("Select X-axis", columns)
    y_axis = st.sidebar.selectbox("Select Y-axis", columns)
    
    # Option to show summary statistics
    if st.sidebar.checkbox("Show Summary Statistics"):
        st.write("### Summary Statistics", data.describe())

    # Filter the data (Optional)
    st.sidebar.subheader("Filter Data")
    filter_column = st.sidebar.selectbox("Select Column to Filter", columns)
    filter_value = st.sidebar.text_input("Filter Value")
    
    if filter_value:
        filtered_data = data[data[filter_column].astype(str).str.contains(filter_value, case=False)]
        st.write("### Filtered Data", filtered_data)
    else:
        filtered_data = data

    # Scatter plot between selected columns
    st.write(f"### Scatter Plot of {x_axis} vs {y_axis}")
    fig, ax = plt.subplots()
    ax.scatter(filtered_data[x_axis], filtered_data[y_axis], alpha=0.6)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)
    
    # Correlation heatmap
    st.write("### Correlation Heatmap of Numerical Features")
    correlation_matrix = filtered_data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    st.pyplot(plt)
