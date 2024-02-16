# Data Extraction and NLP

This repository contains a Python script for data extraction and text analysis, focusing on Natural Language Processing (NLP) techniques.

### Objective

The objective of this assignment is to extract textual data articles from the given URL and perform text analysis to compute variables that are explained below.


### Data Extraction

For each of the articles, given in the input.xlsx file, extract the article text and save the extracted article in a text file with URL_ID as its file name.

* Functionality:
  * The data extraction process is defined in the extract_article_text(url) function.
  * It sends a GET request to the provided URL using the requests library.
  * Upon successful request (status code 200), BeautifulSoup is used to parse the HTML.
    
* Title Extraction: The function attempts to find the title tag within the HTML (soup.find('title')). If found, it extracts the text of the title; otherwise, it defaults to 'No Title Found'.
  
* Article Text Extraction: It collects the text from all paragraph (<p>) tags using a list comprehension.
  
* Implementation:
  * The main functionality is encapsulated within the main() function, which iterates through the rows of an input DataFrame (input_df).
  * For each URL in the DataFrame, it calls extract_article_text(url) to retrieve the article title and text.
  * If the extraction is successful, it writes the title and text to a text file named after the URL ID.
  
### Data Analysis

For each of the extracted texts from the article, perform textual analysis and compute variables, given in the output structure excel file. You need to save the output in the exact order as given in the output structure file, “Output Data Structure.xlsx”

* Functionality:
  * Data analysis begins with loading an Excel file (Output Data Structure (1).xlsx) containing information about URLs and their corresponding IDs.
  * Text analysis is performed on each article using functions like clean_text, calculate_sentiment_scores, and calculate_variables.
  * The results are stored in a Pandas DataFrame (result_df), and the DataFrame is saved to an Excel file (Textual_Analysis_Result.xlsx).

* Variables
   * POSITIVE SCORE
   * NEGATIVE SCORE
   * POLARITY SCORE
   * SUBJECTIVITY SCORE
   * AVG SENTENCE LENGTH
   * PERCENTAGE OF COMPLEX WORDS
   * FOG INDEX
   * AVG NUMBER OF WORDS PER SENTENCE
   * COMPLEX WORD COUNT
   * WORD COUNT
   * SYLLABLE PER WORD
   * PERSONAL PRONOUNS
   * AVG WORD LENGTH

* Definition of the variables
Objective of this document is to explain methodology adopted to perform text analysis to drive sentimental opinion, sentiment scores, readability, passive words, personal pronouns
and etc.

### Table of Contents
     -Sentimental Analysis 
       -Cleaning using Stop Words Lists 
       -Creating dictionary of Positive and Negative words 
       -Extracting Derived variables 
    -Analysis of Readability 
    -Average Number of Words Per Sentence 
    -Complex Word Count 
    -Word Count 
    -Syllable Count Per Word 
    -Personal Pronouns 
    -Average Word Length
  
  1 Sentimental Analysis
Sentimental analysis is the process of determining whether a piece of writing is positive, negative, or neutral. The below Algorithm is designed for use in Financial Texts. It consists
of steps:
    1.1 Cleaning using Stop Words Lists
The Stop Words Lists (found in the folder StopWords) are used to clean the text so that Sentiment Analysis can be performed by excluding the words found in Stop Words List.
    1.2 Creating a dictionary of Positive and Negative words
The Master Dictionary (found in the folder MasterDictionary) is used for creating a dictionary of Positive and Negative words. We add only those words in the dictionary if they
are not found in the Stop Words Lists.
    1.3 Extracting Derived variables
We convert the text into a list of tokens using the nltk tokenize module and use these tokens to calculate the 4 variables described below:
       * Positive Score: This score is calculated by assigning the value of +1 for each word if found in the Positive Dictionary and then adding up all the values.
       * Negative Score: This score is calculated by assigning the value of -1 for each word if found in the Negative Dictionary and then adding up all the values. We multiply the score with -1 so that the score is a positive number.
       * Polarity Score: This is the score that determines if a given text is positive or negative in nature. It is calculated by using the formula:
Polarity Score = (Positive Score – Negative Score)/ ((Positive Score + Negative Score) + 0.000001) Range is from -1 to +1
       * Subjectivity Score: This is the score that determines if a given text is objective or subjective.It is calculated by using the formula:
Subjectivity Score = (Positive Score + Negative Score)/ ((Total Words after cleaning) + 0.000001) Range is from 0 to +1

  2 Analysis of Readability
Analysis of Readability is calculated using the Gunning Fox index formula described below.
Average Sentence Length = the number of words / the number of sentences Percentage of Complex words = the number of complex words / the number of words
Fog Index = 0.4 * (Average Sentence Length + Percentage of Complex words)

  3 Average Number of Words Per Sentence
The formula for calculating is:
Average Number of Words Per Sentence = the total number of words / the total number of sentences

  4 Complex Word Count
Complex words are words in the text that contain more than two syllables.

  5 Word Count  
We count the total cleaned words present in the text by
     1. removing the stop words (using stopwords class of nltk package).
     2. removing any punctuations like ? ! , . from the word before counting.

  6 Syllable Count Per Word

We count the number of Syllables in each word of the text by counting the vowels present in each word. We also handle some exceptions like words ending with &quot;es&quot;,&quot;ed&quot; by not counting them as a syllable.

  7 Personal Pronouns
To calculate Personal Pronouns mentioned in the text, we use regex to find the counts of the words - “I,” “we,” “my,” “ours,” and “us”. Special care is taken so that the country name US
is not included in the list.

  8 Average Word Length
Average Word Length is calculated by the formula: Sum of the total number of characters in each word/Total number of words

### Dependencies:

* For Data Extraction:
```Python
requests
beautifulsoup4
```

* For Data Analysis:
```pandas
nltk
```

* Additionally, download NLTK resources by running these commands in Python:

```import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

By following these instructions, we can successfully extract data from URLs, perform text analysis, and generate the desired output. If you encounter any issues or have questions, feel free to reach out.

