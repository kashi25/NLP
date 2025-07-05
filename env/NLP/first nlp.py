import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('punkt_tab')  # यो लाइन थप्नुहोस्
nltk.download('stopwords')

text = "Natural Language Processing is very exciting and powerful!"
tokens = word_tokenize(text.lower())

# Stop words हटाउने
filtered = [w for w in tokens if w not in stopwords.words('english')]

# stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered]

print("Tokenized:", tokens)
print("Filtered:", filtered)
print("Stemmed:", stemmed_words)
