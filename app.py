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
from nlp_task.language_detection_translation import (
    langDetect,
    langTranslate)
from nlp_task.contact_info_extraction import extractInfo

from visualize import visualize
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
                help= "Choose an NLP task to perform",
                
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
                st.subheader("Perform Sentiment Analysis on Text Data")
                sentiment_analysis()

        # language detection and translation
        elif nlp_task == "Language Detection & Translation":
                Languages = {'afrikaans':'af','albanian':'sq','amharic':'am','arabic':'ar','armenian':'hy','azerbaijani':'az','basque':'eu','belarusian':'be','bengali':'bn','bosnian':'bs','bulgarian':'bg','catalan':'ca','cebuano':'ceb','chichewa':'ny','chinese (simplified)':'zh-cn','chinese (traditional)':'zh-tw','corsican':'co','croatian':'hr','czech':'cs','danish':'da','dutch':'nl','english':'en','esperanto':'eo','estonian':'et','filipino':'tl','finnish':'fi','french':'fr','frisian':'fy','galician':'gl','georgian':'ka','german':'de','greek':'el','gujarati':'gu','haitian creole':'ht','hausa':'ha','hawaiian':'haw','hebrew':'iw','hebrew':'he','hindi':'hi','hmong':'hmn','hungarian':'hu','icelandic':'is','igbo':'ig','indonesian':'id','irish':'ga','italian':'it','japanese':'ja','javanese':'jw','kannada':'kn','kazakh':'kk','khmer':'km','korean':'ko','kurdish (kurmanji)':'ku','kyrgyz':'ky','lao':'lo','latin':'la','latvian':'lv','lithuanian':'lt','luxembourgish':'lb','macedonian':'mk','malagasy':'mg','malay':'ms','malayalam':'ml','maltese':'mt','maori':'mi','marathi':'mr','mongolian':'mn','myanmar (burmese)':'my','nepali':'ne','norwegian':'no','odia':'or','pashto':'ps','persian':'fa','polish':'pl','portuguese':'pt','punjabi':'pa','romanian':'ro','russian':'ru','samoan':'sm','scots gaelic':'gd','serbian':'sr','sesotho':'st','shona':'sn','sindhi':'sd','sinhala':'si','slovak':'sk','slovenian':'sl','somali':'so','spanish':'es','sundanese':'su','swahili':'sw','swedish':'sv','tajik':'tg','tamil':'ta','telugu':'te','thai':'th','turkish':'tr','turkmen':'tk','ukrainian':'uk','urdu':'ur','uyghur':'ug','uzbek':'uz','vietnamese':'vi','welsh':'cy','xhosa':'xh','yiddish':'yi','yoruba':'yo','zulu':'zu'}
                st.subheader("Language Detection & Translation on Textual Source")
                if st.button("Detect Language"):
                    detection_result = langDetect(text_data)
                    if detection_result != "":
                        st.write(detection_result)
                        
                        option0 = st.selectbox('Output language',
                       ('malayalam', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu'))
                        value0 = Languages[option0]

                        if st.button("Translate"):
                            translation_result = langTranslate(detection_result,value0,text_data)
                            st.write(translation_result)
                              
                    else:
                        st.error("Please upload a file first!")

                st.subheader("Language Detection & Translation on Custom Text Input")
                text = st.text_area("Enter text:",height=None,max_chars=None,key=None,help="Enter your text here")
                
                option1 = st.selectbox('Input language',
                      ('english', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch',  'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'malayalam', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu') , 
                      key='input_lang')

                option2 = st.selectbox('Output language',
                       ('malayalam', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'azerbaijani', 'basque', 'belarusian', 'bengali', 'bosnian', 'bulgarian', 'catalan', 'cebuano', 'chichewa', 'chinese (simplified)', 'chinese (traditional)', 'corsican', 'croatian', 'czech', 'danish', 'dutch', 'english', 'esperanto', 'estonian', 'filipino', 'finnish', 'french', 'frisian', 'galician', 'georgian', 'german', 'greek', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi', 'hmong', 'hungarian', 'icelandic', 'igbo', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kazakh', 'khmer', 'korean', 'kurdish (kurmanji)', 'kyrgyz', 'lao', 'latin', 'latvian', 'lithuanian', 'luxembourgish', 'macedonian', 'malagasy', 'malay', 'maltese', 'maori', 'marathi', 'mongolian', 'myanmar (burmese)', 'nepali', 'norwegian', 'odia', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian', 'russian', 'samoan', 'scots gaelic', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian', 'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'telugu', 'thai', 'turkish', 'turkmen', 'ukrainian', 'urdu', 'uyghur', 'uzbek', 'vietnamese', 'welsh', 'xhosa', 'yiddish', 'yoruba', 'zulu') , key='output_lang')

                value1 = Languages[option1]
                value2 = Languages[option2]
                if st.button('Translate Sentence'):
                    if text == "":
                        st.warning('Please **enter text** for translation')

                    else:
                        response = langTranslate(value1,value2,text)
                        st.write(response)
                    
        
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
             st.subheader("Extract Contact Numbers")
             if st.button("Extract"):
                  extractInfo(uploaded_file)
                  

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
        visualize()

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
