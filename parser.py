import requests
import string
import re

from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords

# pip install Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Tentukan User-Agent untuk menyamar sebagai browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# entry
web = requests.get('https://e-facility.itb.ac.id/', headers=headers).text

# Tentukan parser secara eksplisit
soup = BeautifulSoup(web, 'html.parser')

for s in soup(['script', 'style']):
    s.decompose()

# Gabungkan teks yang tersisa
teks = ' '.join(soup.stripped_strings)

teks = teks.lower()
teks = re.sub(r"\d+","",teks)
teks = teks.translate(str.maketrans("","",string.punctuation))
teks = teks.strip()

factory = StemmerFactory()
stemmer = factory.create_stemmer()
output = stemmer.stem(teks)

tokens = [t for t in output.split()]

clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('indonesian'):
        clean_tokens.remove(token)

# 
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ":" + str(val))