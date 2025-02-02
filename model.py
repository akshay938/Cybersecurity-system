import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score
import pickle

def build_model():
    # Read the dataset
    df = pd.read_csv('sms-spam.csv', encoding='latin-1')
    
    # Keep only the first two columns (label and message)
    df = df.iloc[:, 0:2]
    
    # Rename columns for clarity
    df.columns = ['label', 'message']
    
    # Convert spam/ham to binary labels
    df['label'] = df['label'].map({'spam': 1, 'ham': 0})
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        df['message'], 
        df['label'], 
        test_size=0.2, 
        random_state=42
    )
    
    # Create and fit the TF-IDF vectorizer
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train the model
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    
    # Make predictions on test set
    y_pred = model.predict(X_test_tfidf)
    
    # Print model performance
    print("Model Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Create a dictionary containing both the model and vectorizer
    spam_detector = {
        'model': model,
        'vectorizer': vectorizer
    }
    
    # Save the model and vectorizer
    with open('model.pkl', 'wb') as f:
        pickle.dump(spam_detector, f)
    
    print("\nModel saved as 'model.pkl'")

if __name__ == "__main__":
    build_model()