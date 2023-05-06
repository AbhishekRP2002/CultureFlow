import streamlit as st
import pandas as pd
import PyPDF2
import openpyxl
import re

def extract_contact_numbers(text):
    phone_regex = re.compile(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]')
    numbers = re.findall(phone_regex, text)
    return numbers

def extract_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    return extract_contact_numbers(text)

def extract_from_excel(file):
    df = pd.read_excel(file, engine='openpyxl', sheet_name=None)
    numbers = []
    for sheet_name, sheet_data in df.items():
        for col in sheet_data.columns:
            for value in sheet_data[col]:
                if isinstance(value, str):
                    numbers += extract_contact_numbers(value)
    return numbers

def extract_from_csv(file):
    df = pd.read_csv(file)
    numbers = []
    for col in df.columns:
        for value in df[col]:
            if isinstance(value, str):
                numbers += extract_contact_numbers(value)
    return numbers

def extract_from_text(file):
    with open(file.name, 'r') as f:
        text = f.read()
    return extract_contact_numbers(text)

def extract_numbers(file):
    if file.type == 'application/pdf':
        numbers = extract_from_pdf(file)
    elif file.type == 'text/plain':
        numbers = extract_from_text(file)
    elif file.type == 'text/csv':
        numbers = extract_from_csv(file)
    elif file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
        numbers = extract_from_excel(file)
    else:
        numbers = []
    return numbers

def display_numbers(numbers):
    if not numbers:
        st.write("No contact numbers found.")
    else:
        st.write("Contact numbers found:")
        for number in numbers:
            st.write(number)

def extractInfo(file):
        if file is not None:
            numbers = extract_numbers(file)
            display_numbers(numbers)
        else:
            st.write("Upload a  valid file!")