from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pymongo import MongoClient
import time

def scrape_reviews(product_id="B0F2T7B9TM"):
    service = Service("E:\PWSKILLS\PROJECT\ML\Amazon-Reviews\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(f"https://www.amazon.in/product-reviews/{product_id}")
    time.sleep(59)

    # Scroll to load reviews
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(59)

    # Use robust selector
    reviews = driver.find_elements(By.CSS_SELECTOR, '[data-hook="review-body"]')
    data = [{"review": r.text.strip()} for r in reviews if r.text.strip()]
    driver.quit()

    print(f"✅ Scraped {len(data)} reviews.")
    return data


def save_to_mongo(data):
    if not data:
        print("⚠️ No reviews to save. Skipping MongoDB insert.")
        return

    client = MongoClient("mongodb+srv://abhinavsk5899:3nrstpbOWZ9U6qfZ@cluster0.45hnw79.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["amazon-reviews"]  
    col = db["iqoo_reviews"]       

    col.delete_many({})
    col.insert_many(data)
    print("✅ Data saved to MongoDB.")

if __name__ == "__main__": # Ensures the following only runs when this file is executed directly
    reviews = scrape_reviews() # Scrapes reviews using default ASIN (or pass a different one).
    save_to_mongo(reviews) # Persists the scraped reviews to MongoDB.





