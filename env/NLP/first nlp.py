# आवश्यक NLTK लाइब्रेरीहरू import गर्ने
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
# आवश्यक resource हरू डाउनलोड गर्ने (एकपटक मात्र चलाउनु पर्छ)
nltk.download('punkt')       # Tokenization को लागि
nltk.download('punkt_tab')   # भाषा अनुसार tokenizer चलाउनका लागि
nltk.download('stopwords')   # Stopwords हरू हटाउन

# प्रयोग गर्न लागेको text
nltk.download('stopwords')   # Stopwords हरू हटाउन

# प्रयोग गर्न लागेको text
text = "Natural Language Processing is very exciting and powerful!"

# text लाई सानो अक्षरमा बदल्ने र टोकनमा विभाजित गर्ने
tokens = word_tokenize(text.lower())   # lower() ले सबै शब्द सानो बनाउँछ

# Stopwords (जस्तै: is, the, and, etc.) हटाउने
filtered = [w for w in tokens if w not in stopwords.words('english')]

# Stemming: शब्दलाई मूल रूपमा झार्ने (जस्तै: running → run)
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered]

# अन्तिम नतिजा प्रिन्ट गर्ने
print("Tokenized:", tokens)           # सबै टोकनहरू देखाउने
print("Filtered:", filtered)          # Stopwords हटाइ सकेपछिको शब्दहरू
print("Stemmed:", stemmed_words)      # Root मा झारिएका शब्दहरू
