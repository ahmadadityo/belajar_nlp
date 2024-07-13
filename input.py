import string
import re
import nltk
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# Minta input teks dari pengguna
teks = input("Masukkan teks: ")

# Proses teks
teks = teks.lower()
teks = re.sub(r"\d+", "", teks)
teks = teks.translate(str.maketrans("", "", string.punctuation))
teks = teks.strip()

# Stemming
factory = StemmerFactory()
stemmer = factory.create_stemmer()
output = stemmer.stem(teks)

# Tokenisasi
tokens = [t for t in output.split()]

# Hapus stopwords
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('indonesian'):
        clean_tokens.remove(token)

# Hitung frekuensi kemunculan token
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(f"{key}: {val}")