import streamlit as st
import os

uploaded_file = st.file_uploader("Upload a file", type=["json"])


if uploaded_file is not None:
    # Save the uploaded file to the pages directory
    file_path = os.path.join('pages', uploaded_file.name)
    with open(file_path, 'wb') as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"File saved to {file_path}")       
    
    