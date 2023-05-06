import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


def visualize():
    st.title("Visualize and Analyze your data")
    st.info("An interactive dashboard that displays the results of the NLP analysis, including sentiment scores, topic distributions, and text classification results")
    data_file = st.file_uploader("Upload your data",type=['csv' , 'xlsx'])
    if data_file is not None:
        df = pd.read_csv(data_file)
        st.dataframe(df.head())
        profile = ProfileReport(df)
        st_profile_report(profile)
      
        