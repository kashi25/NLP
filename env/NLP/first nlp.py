# आवश्यक NLTK लाइब्रेरीहरू import गर्ने
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# आवश्यक resource हरू डाउनलोड गर्ने (एकपटक मात्र चलाउनु पर्छ)
nltk.download('punkt')       # Tokenization को लागि
nltk.download('punkt_tab')   # भाषा अनुसार tokenizer चलाउनका लागि
nltk.download('stopwords')   # Stopwords हरू हटाउन

"""punkt भनेको NLTK library को pre-trained unsupervised tokenizer हो, जसले sentence टुक्र्याउने र शब्दमा विभाजन गर्ने काम गर्छ।

यो punctuation (., !, ?, etc.) को आधारमा text लाई शुद्ध रूपमा token वा sentence मा विभाजित गर्छ।
त्यसैले यसको नाम punkt = punctuation tokenizer बाट आएको हो।
तिमीले जब nltk.download('punkt') भन्यौ, त्यो बेला tokenizer को main model डाउनलोड हुन्छ।"""

"""punkt_tab भनेको punkt tokenizer को internal language-specific configuration table हो।

यसमा हरेक भाषाको लागि टोकन बनाउने specific नियमहरू र pattern हरू हुन्छन् — जस्तै कि:

कुन punctuation ले sentence टुक्र्याउँछ

कुन word abbreviation हो (e.g., "Dr.", "e.g.")

कुन situation मा sentence टुक्रनु हुँदैन

जब तिमी sent_tokenize(text, language='english') गर्छौ, punkt_tab/english/ बाट त्यो तालिका load हुन्छ।

Stopwords भनेको त्यस्ता सामान्य शब्दहरू हुन् जुन कुनै sentence वा paragraph मा त धेरैपटक आउँछन् तर analysis वा NLP मा खास अर्थ दिन्नन्।
उदाहरणको लागि:
"is", "am", "are", "was", "the", "a", "in", "on", "and", "but" आदि
यी शब्दहरू बिना पनि वाक्यको अर्थ धेरै हदसम्म बुझ्न सकिन्छ।
त्यसैले NLP मा यस्तो शब्दलाई remove गरिन्छ, ताकि हामीले main content वा keyword मात्रमा focus गर्न सकौं।"""


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
