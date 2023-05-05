#  Create a new Python file, e.g., `app.py`, and import the required libraries:

import streamlit as st
import pandas as pd
import streamlit.components.v1 as html
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from nlp_task.chatBot import ai_assistant
from nlp_task.about_app import about
from nlp_task.sentiment_analysis import (
    textsource_sentiment_analysis,
    sentiment_analysis,
)
from nlp_task.recommendation import (
    textsource_recommendation_analysis,
    recommend)
from nlp_task.summarizer import (
   summarize , textsource_summarize_analysis
)
from home import home

st.set_page_config(
    page_title="Culture Flow",
    page_icon="bi-braces-asterisk",
    layout="wide",
)

st.markdown(
    """
            <style>
           
           
          #  .css-nqowgj.edgvbvh3{
          #    visibility: hidden;
          #  }
            
            .css-164nlkn.egzxvld1
            {
                visibility: hidden;
            }
            
            .css-1n543e5.edgvbvh10
            {
              background-color: #f5f5f5;
              color: #000000;
              border-radius: 0.25rem;
              padding: 0.5rem 0.75rem;
               transition-duration: 0.2s;
            }
            
            .css-1n543e5.edgvbvh10:hover {
  background-color: blue; 
  color: white;
  border:none;
}
            
            
            </style>
            
            """,
    unsafe_allow_html=True,
)


# declare global variables:
sentiment_result = ""
text_data = ""


# Add the navigation sidebar and menu items:


def main_nav():
    global sentiment_result , summarize_result , text_data , recommend_result
    

    with st.sidebar:
        menu = option_menu(
            menu_title="CultureFlow",
            options=[
                "Home",
                "CultureFlow AI Chatbot",
                "Perform NLP Analysis",
                "Visualization Dashboard",
                "Contact Us",
            ],
            icons=["house", "book", "list-task", "activity","send"],
            menu_icon="app-indicator",
            default_index=0,
            styles={
                "container": {"padding": "5!important"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
              
            },
        )
    #  Create the Home page with file upload functionality:

    if menu == "Home":
       home() 


    # Create the Educate Yourself page:

    elif menu == "CultureFlow AI Chatbot":
        ai_assistant()

    #  Create the Perform Analysis page with a dropdown for NLP tasks:

    elif menu == "Perform NLP Analysis":
        st.title("Perform NLP Analysis")
        st.write("Upload your textual source file below:")
        uploaded_file = st.file_uploader(
            "Choose a file", type=["pdf", "txt", "csv", "xlsx"]
        )
        if uploaded_file is not None:
            if uploaded_file.type == "pdf":
                text_data = uploaded_file.read().decode("utf-8")
            if uploaded_file.type == "text/plain":
                text_data = uploaded_file.read().decode("utf-8")
            elif uploaded_file.type == "application/vnd.ms-excel":
                text_data = pd.read_csv(uploaded_file)
            elif (
                uploaded_file.type
                == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            ):
                text_data = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully!")
           

        nlp_task = st.selectbox(
                "Choose an task to perform",
                [
                    "Sentiment Analysis",
                    "Language Detection & Translation",
                    "Actionable Recommendations",
                    "Text Classification and Context Identification",
                    "Contact Information Extraction",
                    "Summarize Company Data",
                ],
            )

            # sentiment analysis
        if nlp_task == "Sentiment Analysis":
                st.subheader("Sentiment Analysis on Textual Source")
                if st.button("Perform Sentiment Analysis"):
                    sentiment_result = textsource_sentiment_analysis(text_data)
                    if sentiment_result != "":
                        
                         st.write(sentiment_result)
                    else:
                        st.error("Please upload a file first!")
                sentiment_analysis()

        # language detection and translation
        elif nlp_task == "Language Detection & Translation":
             st.write("Performing Language Detection and Translation...")
        elif nlp_task == "Actionable Recommendations":
            #  st.write("Performing Actionable Recommendations...")
            st.subheader("Actionable Recommendations on Textual Source")
            st.info("Get actionable recommendations by our NLP based AI model in order to improve your company culture.")
            if st.button("Perform Analysis"):
                    recommend_result = textsource_recommendation_analysis(text_data)
                    if recommend_result != "":
                        
                         st.write(recommend_result)
                    else:
                        st.error("Please upload a file first!")
            # recommend()
            
        elif nlp_task == "Text Classification and Context Identification":
             st.write("Performing Text Classification...")
      
        elif nlp_task == "Contact Information Extraction":
             st.write("Performing Contact Info  Extraction...")
        elif nlp_task == "Summarize Company Data":
              st.subheader("Text Summarization on Textual Source")
              if st.button("Perform Text Summarization"):
                    summarize_result = textsource_summarize_analysis(text_data)
                    if summarize_result != "":
                        
                         st.write(summarize_result)
                    else:
                        st.error("Please upload a file first!")
              summarize ()
              
    # Create the Visualization Dashboard page:
    elif menu == "Visualization Dashboard":
        st.title("Visualization Dashboard")

    # Create the Contact Us page:
    elif menu == "Contact Us":
        st.title("Contact Us")
        st.markdown(
            """ <style> .font {
    font-size:25px ; font-family: 'Helvetica'; color: 'blue';} 
    </style> """,
            unsafe_allow_html=True,
        )
        st.markdown(
            '<p class="font">Please help us improve. Your valuable feedbacks matter!</p>',
            unsafe_allow_html=True,
        )
        with st.form(
            key="columns_in_form2", clear_on_submit=True
        ):  # set clear_on_submit=True so that the form will be reset/cleared once it's submitted
            # st.write('Please help us improve!')
            Name = st.text_input(label="Enter Your Name")  # Collect user feedback
            Email = st.text_input(label="Enter Email")  # Collect user feedback
            Message = st.text_input(
                label="SHare Your Vews and Feedback!"
            )  # Collect user feedback
            submitted = st.form_submit_button("Submit")
            if submitted:
                st.write(
                    "Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!"
                )


# Run the app:


if __name__ == "__main__":
    main_nav()
