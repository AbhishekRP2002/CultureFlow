import streamlit as st
import pandas as pd
import spacy
import re
from spacy import displacy
from collections import defaultdict
import openpyxl

nlp = spacy.load("en_core_web_sm")


# Define a function to extract contact information:


def extract_contact_info(text):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", text)
    phone_numbers = re.findall(r"\b\d{10}\b|\b\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}\b|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b", text)
  
    return {"names": names, "emails": emails, "phone_numbers": phone_numbers}





def extractInfo(text):
        contacts = extract_contact_info(text)
        st.write("Names:", contacts["names"])
        st.write("Emails:", contacts["emails"])
        st.write("Phone Numbers:", contacts["phone_numbers"])

