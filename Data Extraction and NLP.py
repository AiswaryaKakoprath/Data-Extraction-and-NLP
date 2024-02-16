#!/usr/bin/env python
# coding: utf-8

# # Data Extraction and NLP
# 

# In[1]:


pip install pandas requests beautifulsoup4


# Objective
# * The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables 
# 

# In[3]:


import pandas as pd


# In[3]:


input_df=pd.read_excel(r"C:\Users\aksha\Downloads\Input.xlsx")


# In[4]:


input_df.head()


# In[5]:


input_df.shape


# # Data extraction

# In[6]:


import requests
from bs4 import BeautifulSoup


# In[7]:


def extract_article_text(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract article title and text
        title = soup.find('title').get_text() if soup.find('title') else 'No Title Found'
        article_text = ' '.join([p.get_text() for p in soup.find_all('p')])
        
        return title, article_text
    else:
        print(f"Failed to retrieve content from {url}")
        return None, None


# In[8]:


def main():
    for index, row in input_df.iterrows():
        url_id = row['URL_ID']
        url = row['URL']
        
        # Extract article text
        title, article_text = extract_article_text(url)
        
        if title and article_text:
            # Save the extracted article in a text file
            with open(f"{url_id}.txt", 'w', encoding='utf-8') as file:
                file.write(f"Title: {title}\n\n")
                file.write(f"Article Text:\n{article_text}")
            print(f"Article for {url_id} extracted and saved successfully.")
        else:
            print(f"Article extraction failed for {url_id}.")


# In[10]:


if __name__ == "__main__":
    main()


# # Data Analysis

# In[23]:


get_ipython().system('python -m spacy download en_core_web_sm')


# In[11]:


pip install pandas spacy


# In[1]:


pip install textblob


# In[4]:


import spacy
from textblob import TextBlob


# In[5]:


output_df = pd.read_excel(r"C:\Users\aksha\Downloads\Output Data Structure (1).xlsx")


# In[6]:


output_df.head()


# In[38]:


import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re


# In[39]:


nltk.download('stopwords')
nltk.download('punkt')


# In[94]:


import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re
import os

nltk.download('stopwords')
nltk.download('punkt')

def analyze_readability(text, words, complex_words):
    average_sentence_length = len(words) / len(sent_tokenize(text))
    percentage_complex_words = len(complex_words) / len(words)
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    return average_sentence_length, percentage_complex_words, fog_index

def calculate_variables(text):
    stop_words = set(stopwords.words('english'))
    
    # Load positive and negative dictionaries
    positive_dict = set(pd.read_csv(r"C:\Users\aksha\Downloads\MasterDictionary-20240125T084343Z-001\MasterDictionary\positive-words.txt", header=None, encoding='latin1')[0].tolist())
    negative_dict = set(pd.read_csv(r"C:\Users\aksha\Downloads\MasterDictionary-20240125T084343Z-001\MasterDictionary\negative-words.txt", header=None, encoding='latin1')[0].tolist())
    
    # Clean text
    cleaned_words = clean_text(text, stop_words)
    
    # Sentiment Analysis
    positive_score, negative_score, polarity_score, subjectivity_score = calculate_sentiment_scores(
        cleaned_words, positive_dict, negative_dict)
    
    # Analysis of Readability
    complex_words = [word for word in cleaned_words if len(word) > 2]
    average_sentence_length, percentage_complex_words, fog_index = analyze_readability(text, cleaned_words, complex_words)
    
    # Average Number of Words Per Sentence
    avg_words_per_sentence = len(cleaned_words) / len(sent_tokenize(text))
    
    # Complex Word Count
    complex_word_count = len([word for word in cleaned_words if len(word) > 2])
    
    # Word Count
    word_count = len(cleaned_words)
    
    # Syllable Count Per Word
    syllables_per_word = sum(len(re.findall(r'[aeiou]+', word)) for word in cleaned_words)
    
    # Personal Pronouns
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, flags=re.IGNORECASE))
    
    # Average Word Length
    avg_word_length = sum(len(word) for word in cleaned_words) / len(cleaned_words)
    
    return positive_score, negative_score, polarity_score, subjectivity_score, \
           average_sentence_length, percentage_complex_words, fog_index, \
           avg_words_per_sentence, complex_word_count, word_count, \
           syllables_per_word, personal_pronouns, avg_word_length



# In[95]:


# Create an empty DataFrame to store the computed variables
result_df = pd.DataFrame(columns=output_df.columns)

for index, row in output_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    print(f"Processing {url_id} - {url}")

    # Update the file path using os.path.join
    input_file = os.path.join(r"C:\Users\aksha\DS PRO", f"{url_id}.txt")
    print(f"Input file: {input_file}")

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        variables = calculate_variables(text)

        result_df = pd.concat([result_df, pd.DataFrame({
            'URL_ID': [url_id],
            'URL': [url],
            'POSITIVE SCORE': [variables[0]],
            'NEGATIVE SCORE': [variables[1]],
            'POLARITY SCORE': [variables[2]],
            'SUBJECTIVITY SCORE': [variables[3]],
            'AVG SENTENCE LENGTH': [variables[4]],
            'PERCENTAGE OF COMPLEX WORDS': [variables[5]],
            'FOG INDEX': [variables[6]],
            'AVG NUMBER OF WORDS PER SENTENCE': [variables[7]],
            'COMPLEX WORD COUNT': [variables[8]],
            'WORD COUNT': [variables[9]],
            'SYLLABLE PER WORD': [variables[10]],
            'PERSONAL PRONOUNS': [variables[11]],
            'AVG WORD LENGTH': [variables[12]],
        })], ignore_index=True)

    except FileNotFoundError:
        print(f"File not found: {input_file}. Skipping...")


# In[91]:


result_df.head()


# In[93]:


result_df.to_excel(r"C:\Users\aksha\OneDrive\Desktop\Textual_Analysis_Result.xlsx")

