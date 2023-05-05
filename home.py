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
            font-size: 45px;
            font-weight: 700;
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
            font-size: 25px;
            font-weight: 500;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.25;
            margin: 30px;
            border: 1.5px solid #ccc;
            border-radius: 10px;
            padding: 20px;
            background-color: #FF4B4B;
            color: white;
            
            }
            
        .features{
             text-align: left;
            font-size: 40px;
            font-weight: 700;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
         
            line-height: 1;
            margin:30px 30px;
            }
            
            .features-text{
                text-align: left;
            font-size: 20px;
            font-weight: 500;
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
      
      <div class="features">
        How can you use CultureFlow?
      </div>
      
      <div class="features-text">
         CultureFlow is a web-based platform that offers features and functionalities to help organizations improve their company culture through NLP analysis and reduction in attrition.
      </div>
      
      <div class=features-list>
      
      
      
      </div>
      
        """
        
        , unsafe_allow_html=True)
  

    features = {
    "Sentiment Analysis": "Description of Feature 1...",
    "Language Detection and Translation": "Description of Feature 2...",
    "Actionable Recommendations": "Description of Feature 3...",
    "Text Classification": "Description of Feature 4...",
    "Context Identification": "Description of Feature 5...",
    "Contact Information Extraction": "Description of Feature 6...",
    "Summarization of Textual Source": "Description of Feature 7..."
}

    for feature, description in features.items():
       with st.expander(feature):
           st.write(description)
    
    
  