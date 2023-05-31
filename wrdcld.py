import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Sample emotions and keywords (replace with your own data)
emotions = {
    "emotion": ["Emotion Detection", "Sentiments", "Speech", "emotional", "excited","vision","non-verbal", "depression", "processing","attitude", "depression", "classification", "fusion", "affective", "micro-expression","computing","expressions","features", "love", "pressure", "motivate", "stress", "behaviour", "emotions", "auditory", "affect", "feeling", "Multi-modality","physiological" ],
}
# Combine all keywords into a single list
all_keywords = [keyword for keywords in emotions.values() for keyword in keywords]

# Create a word cloud from the keywords
wordcloud = WordCloud(width=800, height=400).generate(' '.join(all_keywords))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
