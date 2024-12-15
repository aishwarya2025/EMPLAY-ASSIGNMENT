#!/usr/bin/env python
# coding: utf-8

# In[14]:


pip install ipywidgets==7.7.2


# In[17]:


pip install --upgrade transformers


# In[21]:


pip install bitsandbytes


# In[28]:


pip install tf-keras


# In[30]:


pip install tensorflow==2.11


# In[31]:


pip install tensorflow==2.12.0


# In[32]:


pip install keras==2.11


# In[33]:


pip install keras==2.12.0


# In[3]:


import os
import json
from bs4 import BeautifulSoup
import pdfplumber
from transformers import pipeline

# Define structured data fields
FIELDS = [
    "Bid Number", "Title", "Due Date", "Bid Submission Type", "Term of Bid",
    "Pre Bid Meeting", "Installation", "Bid Bond Requirement", "Delivery Date",
    "Payment Terms", "Any Additional Documentation Required", "MFG for Registration",
    "Contract or Cooperative to use", "Model_no", "Part_no", "Product", 
    "contact_info", "company_name", "Bid Summary", "Product Specification", "Value"
]

# Initialize a Language Model pipeline (e.g., OpenAI or Hugging Face models)
nlp = pipeline("question-answering")

# Function to extract text from HTML files
def extract_text_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup.get_text()

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    extracted_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text()
    return extracted_text

# Function to structure extracted information
def structure_information(text):
    structured_data = {}
    for field in FIELDS:
        try:
            # Use NLP to extract relevant information for each field
            response = nlp({
                "context": text,
                "question": f"What is the {field}?"
            })
            structured_data[field] = response.get("answer", "").strip()
        except Exception as e:
            structured_data[field] = f"Error extracting {field}: {str(e)}"
    return structured_data

# Main function to process all documents and save outputs
def process_documents(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Parse based on file type
        if file_name.endswith(".html"):
            text = extract_text_from_html(file_path)
        elif file_name.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            print(f"Unsupported file type: {file_name}")
            continue

        # Structure information
        structured_data = structure_information(text)

        # Save the output as a JSON file
        output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.json")
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(structured_data, json_file, indent=4, ensure_ascii=False)
        print(f"Processed {file_name}: Output saved to {output_file}")

# Entry point
if __name__ == "__main__":
    input_folder = "C:/Users/deept/OneDrive/Desktop/Campus hiring-2024-2025 assignment/Bid1" # Replace with your folder path
    output_folder = "./output_jsons"  # Folder to save output JSON files

    # Ensure input folder exists
    if not os.path.exists(input_folder):
        print(f"Input folder not found: {input_folder}")
    else:
        process_documents(input_folder, output_folder)
        print(f"Processing complete. All outputs saved in {output_folder}")


# In[4]:


import os
import json
from bs4 import BeautifulSoup
import pdfplumber
from transformers import pipeline

# Define structured data fields
FIELDS = [
    "Bid Number", "Title", "Due Date", "Bid Submission Type", "Term of Bid",
    "Pre Bid Meeting", "Installation", "Bid Bond Requirement", "Delivery Date",
    "Payment Terms", "Any Additional Documentation Required", "MFG for Registration",
    "Contract or Cooperative to use", "Model_no", "Part_no", "Product", 
    "contact_info", "company_name", "Bid Summary", "Product Specification", "Value"
]

# Initialize a Language Model pipeline (e.g., OpenAI or Hugging Face models)
nlp = pipeline("question-answering")

# Function to extract text from HTML files
def extract_text_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup.get_text()

# Function to extract text from PDF files
def extract_text_from_pdf(file_path):
    extracted_text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text()
    return extracted_text

# Function to structure extracted information
def structure_information(text):
    structured_data = {}
    for field in FIELDS:
        try:
            # Use NLP to extract relevant information for each field
            response = nlp({
                "context": text,
                "question": f"What is the {field}?"
            })
            structured_data[field] = response.get("answer", "").strip()
        except Exception as e:
            structured_data[field] = f"Error extracting {field}: {str(e)}"
    return structured_data

# Main function to process all documents and save outputs
def process_documents(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Parse based on file type
        if file_name.endswith(".html"):
            text = extract_text_from_html(file_path)
        elif file_name.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        else:
            print(f"Unsupported file type: {file_name}")
            continue

        # Structure information
        structured_data = structure_information(text)

        # Save the output as a JSON file
        output_file = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.json")
        with open(output_file, "w", encoding="utf-8") as json_file:
            json.dump(structured_data, json_file, indent=4, ensure_ascii=False)
        print(f"Processed {file_name}: Output saved to {output_file}")

# Entry point
if __name__ == "__main__":
    input_folder = "C:/Users/deept/OneDrive/Desktop/Campus hiring-2024-2025 assignment/Bid2" # Replace with your folder path
    output_folder = "./output_jsons"  # Folder to save output JSON files

    # Ensure input folder exists
    if not os.path.exists(input_folder):
        print(f"Input folder not found: {input_folder}")
    else:
        process_documents(input_folder, output_folder)
        print(f"Processing complete. All outputs saved in {output_folder}")


# In[ ]:




