from flask import Flask, render_template
from pymongo import MongoClient
import pandas as pd

app= Flask(__name__)

# mongoDB connection
client= MongoClient("mongodb+srv://abhinavsk5899:3nrstpbOWZ9U6qfZ@cluster0.45hnw79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db= client["amazon-reviews"]
col= db["iqoo_reviews"]

@app.route("/")
def home():
    # load reviews from MongoDB
    data= list(col.find({},{"_id":0}))
    df= pd.DataFrame(data)

    # add sentiment labels if not already present
    if "sentiment" in df.columns:
        def label(p):
            if p>0.1:
                return "Positive"
            elif p< -0.1:
                return "Negative"
            else:
                return "Neutral"
            
        df["sentiment_label"]= df["sentiment"].apply(label)
    else:
        df["sentiment_label"]= "Unknown"

    # convert to list of dicts for HTML rendering
    reviews= df.to_dict(orient="records")
    return render_template("index.html", reviews= reviews)

if __name__== "__main__":
    app.run(debug= True)