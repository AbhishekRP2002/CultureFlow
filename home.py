import streamlit as st
import pandas as pd
import streamlit.components.v1 as html
import streamlit.components.v1 as components


def home():
    st.markdown("""
    <style>
        .title {
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding : 0px
            padding-top: 20px;
            margin-top: 10px;
        }
        .subtitle{
            text-align: center;
            font-size: 35px;
            font-weight: 300;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding : 0px;
            line-height: 1;
           padding:0px 50px;
        }
        
   
        
        
        .css-z5fcl4.egzxvld4{
            padding: 0px;
        }
    </style>
    <div class="title-container">
    <div class="title">
        CultureFlow 
    </div>
    <div class="subtitle">
       A platform that helps organizations analyze and improve their company culture.
        </div>
    </div>
""", unsafe_allow_html=True)
    
    st.markdown("""
        
        <style>
        .mission-text{
            text-align: left;
            # font-size: 20px;
            # font-weight: 320;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.25;
            margin: 30px;
            border: 1.5px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            background-color: #FF4B4B;
            color: white;
            
            }
            
        .features-title{
             text-align: left;
            font-size: 30px;
            # font-weight: 700;
            font-family: 'Roboto', sans-serif;
            text-align:center;
            line-height: 1;
            margin:30px 30px;
            }
            
            .features-text{
                text-align: left;
            # font-size: 20px;
            # font-weight: 300;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.25;
            margin: 30px 30px;
            border: 1.5px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            background-color: #FF4B4B;
            color: white;
            }
            
            .streamlit-expanderHeader{

             
                
            }
            
            .css-1fcdlhc.e1s6o5jp0{
                margin: -5px 30px;
            }
        
        
        </style>
        
      <div class="mission-text">
       Our goal is to provide insights into a company's culture by analyzing various sources of textual data, such as employee reviews, feedback, and internal communication channels in order to prioritize building a strong company culture. We believe that a positive work environment fosters innovation, collaboration, and success.
      </div>
      
      <div class="features-title">
      Why choose us?
      </div>
      
      <div class="features-text">
         CultureFlow is a web-based platform that offers features and functionalities to help organizations improve their company culture through NLP analysis and reduction in attrition.
      </div>
      
      <div class=features-list>
      
      
      
      </div>
      
        """
        
        , unsafe_allow_html=True)
  

    features = {
    "Sentiment Analysis": "Use our tool analyze the sentiment of the text data, determining whether the overall tone is positive, negative, or neutral  which will help identify areas of the company culture that may need improvement.",
    "Language Detection and Translation": "Using our tool, you can analyze feedback from employees who speak different languages and identify any cultural or linguistic differences that may be contributing to attrition.",
    "Actionable Recommendations": " Based on the insights gathered from the analysis and your data, our tool will provide actionable recommendations to improve company culture.",
    "Text Classification and  Context Identification": "Use our tool  to identify key themes and trends in the text data related to company culture.",
    "Contact Information Extraction": "Use our tool to extract contact information such as names, phone numbers, and email IDs of the stakeholders/employees responsible for culture building in the identified enterprises.",
    "Text Summarization": "Use our summarization tool for company culture analytics because by condensing large amounts of text(Internal channel , employee feedback..) into a more concise and readable format and quickly identify common themes and issues that need to be addressed in order to improve company culture.",
    "Visualization Dashboard": "Generate comprehensive reports and visualizations that provide insights into the culture-building conversations, including trends, patterns, and key findings with our visualization dashboard.",
    "CultureFlow AI Chatbot": "Use our chatbot to get answers to your questions about company culture and how to improve it.",
}

    for feature, description in features.items():
       with st.expander(feature):
           st.write(description)
    
    
  