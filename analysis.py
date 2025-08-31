from pymongo import MongoClient
from textblob import TextBlob
import pandas as pd

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://abhinavsk5899:3nrstpbOWZ9U6qfZ@cluster0.45hnw79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["amazon-reviews"]        
col = db["iqoo_reviews"]              

# Load reviews from MongoDB
data = list(col.find({}, {"_id": 0}))
df = pd.DataFrame(data)

# Debug: Show structure
print("📦 Columns in DataFrame:", df.columns.tolist())
print("🔍 Sample rows:\n", df.head())

# Check and clean review column
if "review" in df.columns:
    df = df[df["review"].notnull()]
    df = df[df["review"].str.strip() != ""]

    # Apply sentiment analysis
    df["sentiment"] = df["review"].apply(lambda x: TextBlob(x).sentiment.polarity)

    # Add sentiment label
    def label(p):
      if p > 0.1:
         return "Positive"
      elif p < -0.1:
         return "Negative"
      else:
         return "Neutral"
      
    df["sentiment_label"] = df["sentiment"].apply(label)

    # Push updated data back to MongoDB
    col.delete_many({})
    col.insert_many(df.to_dict(orient="records"))
    print("✅ Updated MongoDB with sentiment scores.")

    # Save to CSV
    df.to_csv("reviews.csv", index=False)
    print("✅ Saved reviews.csv with sentiment scores.")
else:
    print("❌ 'review' column not found. Check MongoDB data structure.")





