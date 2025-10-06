# Movie Recommender + Sentiment Analyzer
# Combines basic sentiment detection with movie suggestions

# Predefined lists for sentiment words
positive_words = ["good", "nice", "love", "like", "amazing", "great", "fantastic", "enjoy"]
negative_words = ["bad", "hate", "sad", "terrible", "boring", "awful", "poor"]

# Simple movie dataset by mood
movies = {
    "positive": ["Inception", "Interstellar", "The Secret Life of Walter Mitty", "La La Land", "Up"],
    "negative": ["Joker", "The Pianist", "The Pursuit of Happyness", "Inside Out", "The Green Mile"],
    "neutral": ["The Social Network", "Cast Away", "Forrest Gump", "Moneyball", "Arrival"]
}

# --- Sentiment Analysis ---
sentence = input("What are your thoughts today? : ").lower()
words = sentence.split()
score = 0

for word in words:
    if word in positive_words:
        score += 1
    elif word in negative_words:
        score -= 1

# --- Sentiment Classification ---
if score > 1:
    sentiment = "positive"
    print("\n😊 Sentiment detected: Positive")
elif score < 0:
    sentiment = "negative"
    print("\n😔 Sentiment detected: Negative")
else:
    sentiment = "neutral"
    print("\n😐 Sentiment detected: Neutral")

# --- Movie Recommendation ---
print("\n🎬 Based on your mood, you might enjoy these movies:\n")
for movie in movies[sentiment]:
    print("-", movie)
