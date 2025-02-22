# Re-import necessary libraries after execution state reset
import nltk
import pandas as pd
import numpy as np
import torch
import transformers
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import shap

# Download necessary NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample policy-related textual data
documents = [
    "The new traffic policy has significantly improved congestion.",
    "Many drivers are frustrated with the toll increases.",
    "Public transportation reliability has worsened in the past year.",
    "The expansion of bike lanes has been beneficial for commuters.",
    "The government’s investment in new highways is controversial.",
    "Traffic congestion has been reduced by the new bus lanes.",
    "Highway tolls are increasing financial burdens on low-income drivers.",
    "Cycling infrastructure improvements have been welcomed by urban communities.",
    "The latest transport reforms have led to unexpected travel delays.",
    "Carpooling incentives have increased shared vehicle usage."
]

# Sentiment Analysis
sentiments = [sia.polarity_scores(text)['compound'] for text in documents]
df_nlp = pd.DataFrame({"Text": documents, "Sentiment_Score": sentiments})

# Visualizing sentiment scores
plt.figure(figsize=(8,5))
sns.histplot(df_nlp["Sentiment_Score"], bins=5, kde=True, color="blue")
plt.axvline(df_nlp["Sentiment_Score"].mean(), color='red', linestyle='dashed', linewidth=2, label="Mean Sentiment Score")
plt.title("Sentiment Score Distribution in Transportation Policy Texts")
plt.xlabel("Sentiment Score (Negative to Positive)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Preprocessing text for topic modeling
stop_words = set(stopwords.words('english'))
preprocessed_docs = [" ".join([word.lower() for word in text.split() if word.isalnum() and word.lower() not in stop_words]) for text in documents]

# Topic Modeling using LDA
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(preprocessed_docs)

lda = LatentDirichletAllocation(n_components=2, random_state=42)
lda.fit(X)

# Extracting top words for each topic
feature_names = vectorizer.get_feature_names_out()
topics = {}
for topic_idx, topic in enumerate(lda.components_):
    topics[f"Topic {topic_idx+1}"] = [feature_names[i] for i in topic.argsort()[:-6:-1]]

# Convert topics into a DataFrame for visualization
topic_df = pd.DataFrame(topics)
display(topic_df)

# Visualizing topic distribution
plt.figure(figsize=(8,5))
sns.barplot(x=topic_df.columns, y=lda.components_.sum(axis=1), palette="viridis")
plt.title("Topic Importance in Transport Policy Texts")
plt.ylabel("Topic Weight")
plt.xlabel("Topic Number")
plt.show()
