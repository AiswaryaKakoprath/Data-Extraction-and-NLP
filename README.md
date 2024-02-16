# Data Extraction and NLP

This repository contains a Python script for data extraction and text analysis, focusing on Natural Language Processing (NLP) techniques.

### Data Extraction

* Functionality:
  * The data extraction process is defined in the extract_article_text(url) function.
  * It sends a GET request to the provided URL using the requests library.
  * Upon successful request (status code 200), BeautifulSoup is used to parse the HTML.
    
* Title Extraction: The function attempts to find the title tag within the HTML (soup.find('title')). If found, it extracts the text of the title; otherwise, it defaults to 'No Title Found'.
  
* Article Text Extraction: It collects the text from all paragraph (<p>) tags using a list comprehension.
  
*Implementation:
  * The main functionality is encapsulated within the main() function, which iterates through the rows of an input DataFrame (input_df).
  * For each URL in the DataFrame, it calls extract_article_text(url) to retrieve the article title and text.
  * If the extraction is successful, it writes the title and text to a text file named after the URL ID.
  
### Data Analysis


* Functionality:
  * Data analysis begins with loading an Excel file (Output Data Structure (1).xlsx) containing information about URLs and their corresponding IDs.
  * Text analysis is performed on each article using functions like clean_text, calculate_sentiment_scores, and calculate_variables.
  *The results are stored in a Pandas DataFrame (result_df), and the DataFrame is saved to an Excel file (Textual_Analysis_Result.xlsx).

### Dependencies:

* For Data Extraction:
```Python
requests
beautifulsoup4
```
  * Install them using:

```pip install requests beautifulsoup4
```

* For Data Analysis:
```pandas
nltk
```
  * Install them using:

```pip install pandas nltk
```

* Additionally, download NLTK resources by running these commands in Python:

```import nltk
nltk.download('stopwords')
nltk.download('punkt')
```

By following these instructions, we can successfully extract data from URLs, perform text analysis, and generate the desired output. If you encounter any issues or have questions, feel free to reach out.

