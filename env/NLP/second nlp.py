import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

# Raw Text
text = "Hello there!!! I bought 5 apples, 2 bananas & 1 orange. Total: $10.99. Isn't that amazing? aakdam ramilo xaeno ta aane?"

# 1. Lowercasing
text = text.lower()

# 2. Remove numbers
text = re.sub(r'\d+', '', text)

# 3. Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# 4. Remove extra whitespace
text = text.strip()

# 5. Tokenize
tokens = word_tokenize(text)

# 6. Remove stopwords
filtered = [word for word in tokens if word not in stopwords.words('english', 'Nepali')]

# 7. Stemming
stemmer = PorterStemmer()
stemmed = [stemmer.stem(word) for word in filtered]

print("Cleaned:", text)
print("Tokens:", tokens)
print("Filtered:", filtered)
print("Stemmed:", stemmed)
