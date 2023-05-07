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

# def extract_from_csv(file):
#     df = pd.read_csv(file)
#     numbers = []
#     for col in df.columns:
#         for value in df[col]:
#             if isinstance(value, str):
#                 numbers += extract_contact_numbers(value)
#     return numbers

# def extract_from_text(file):
#     with open(file.name, 'r') as f:
#         text = f.read()
#     return extract_contact_numbers(text)

def extract_contact_info(text):
    name_pattern = re.compile(r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b')
    phone_pattern = re.compile(r'\b\d{10}\b|\b\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}\b|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    names = name_pattern.findall(text)
    phone_numbers = phone_pattern.findall(text)
    email_ids = email_pattern.findall(text)

    return names, phone_numbers, email_ids

def process_file(input_file):
    data = pd.read_csv(input_file)
    text = ' '.join(data.values.flatten())

    names, phone_numbers, email_ids = extract_contact_info(text)

    extracted_data = pd.DataFrame({'Name': names, 'Phone': phone_numbers, 'Email': email_ids})
    extracted_data.to_csv('extracted_contacts.csv', index=False)

    return extracted_data


def display_numbers(numbers):
    if not numbers:
        st.write("No contact numbers found.")
    else:
        st.write("Contact numbers found:")
        for number in numbers:
            st.write(number)

def extractInfo(file):
        if file is not None:
            if file.type == 'application/pdf':
                numbers = extract_from_pdf(file)
                display_numbers(numbers)
            
            elif file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                numbers = extract_from_excel(file)
                display_numbers(numbers)

            elif file.type == 'text/plain':
                text = file.read().decode('utf-8')
                names, phone_numbers, email_ids = extract_contact_info(text)
                st.write("Names:", names)
                st.write("Phone Numbers:", phone_numbers)
                st.write("Email IDs:", email_ids)
            
            elif file.type == "text/csv":
                extracted_data = process_file(file)
                st.write(extracted_data)

                if st.button('Download Extracted Contacts'):
                        st.download_button(
                            label="Download CSV",
                            data=extracted_data.to_csv(index=False).encode('utf-8'),
                            file_name="extracted_contacts.csv",
                            mime="text/csv",
                        )
            
        else:
            st.write("Give valid file!")