import re
import string
from nltk.corpus import stopwords

def clean_text(text):
    text = text.replace('\\n', ' ').replace('\n', ' ')
    text = text.lower()
    text = re.sub('[\W]+', ' ', text, flags=re.UNICODE)
    text = re.sub(r'\b\w{1,2}\b', ' ', text).strip()
    text = re.sub('['+string.punctuation+']', ' ', text)
    text = re.sub(r"\s+"," ", text, flags = re.UNICODE)
    text = text.split()
    stops = set(stopwords.words('english'))
    text = [w for w in text if not w in stops and len(w) >= 2]
    text = ' '.join(text)
    text = re.sub(r"\s+"," ", text, flags = re.UNICODE)
    text = text.strip()
    return text

# df['text'] = df['text'].map(str).map(lambda line: clean_text(line))
