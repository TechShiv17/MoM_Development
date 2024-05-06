import re

import nltk

nltk.download('punkt')

# Define regular expressions for tokenization #
comma_pattern = r','  # comma pattern
quotes_pattern = r'"'  # Quotes
single_quote_pattern = r"'|\'"  # single Quotes
square_bracket_pattern = r'\[|\]'  # Square brackets
new_line = re.compile(r'\n')  # for new line
word_pattern = r'\b\w+\b'  # Match word characters
digit_pattern = r'\d+'  # Match digits
currency_pattern = r'\$[\d\.]+'  # Match currency symbols followed by numbers (e.g., $10.50)
non_whitespace_pattern = r'\S+'  # Match non-whitespace characters as a fallback
punctuation_pattern = r'[^\w\s]'  # Match punctuation
email_pattern = r'[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}'  # Match email addresses
hashtag_pattern = r'#\w+'  # Match hashtags
mention_pattern = r'@\w+'  # Match mentions
emoticon_pattern = r'[:;]-?[)D\[\]\/\\(|\*]+'  # Match emoticons
abbreviation_pattern = r'[A-Za-z]\.(?![A-Za-z])'  # Match single-letter abbreviations followed by a period
date_pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b'  # Match dates
time_pattern = r'\b\d{1,2}:\d{2}\s?(?:[ap]m)?\b'  # Match times
url_pattern = r'(http|https|ftp)://[^\s/$.?#].[^\s]*'  # Match URLs
phone_number_pattern = r'\b\d{3}[\s.-]?\d{3}[\s.-]?\d{4}\b'  # Match phone numbers
acronym_pattern = r'([A-Z]\.)+'  # Match acronyms
contraction_pattern = r'\b\w+\'(?:\w+)?\b'  # Match contractions


def read_file(file_path):
    file = open(file_path, 'r')
    read_content = file.read()
    file.close()
    return read_content


def write_into_file(file_path, content_to_write):
    file = open(file_path, 'w')
    file.write(content_to_write)
    file.close()


file_text = read_file("transcript.txt")


def remove_pattern(text, pattern):
    return re.sub(pattern, '', text)


# add different patterns according to your need for filtering
def clean(text):
    text = remove_pattern(text, comma_pattern)
    text = remove_pattern(text, quotes_pattern)
    text = remove_pattern(text, single_quote_pattern)
    text = remove_pattern(text, square_bracket_pattern)
    text = remove_pattern(text, new_line)
    return text


cleaned_text = clean(file_text)
write_into_file("file1.txt", cleaned_text)
