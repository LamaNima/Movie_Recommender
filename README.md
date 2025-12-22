# 🎬 Movie Recommendation System (Content-Based)

## 📌 Overview
This project is a **content-based movie recommender system** that suggests movies similar to a given title by analyzing intrinsic movie features.  
Using the **TMDB 5000 Movies Dataset**, the system evaluates attributes such as **genres, keywords, cast, crew, and movie overviews** to compute similarity scores.

The recommendation engine uses **cosine similarity** to measure how closely related movies are based on their feature vectors.  
Unlike collaborative filtering, this system does **not rely on user ratings**, making it effective even without historical user interaction data.

---

## 🌐 Live Demo

🚀 **The project is deployed and accessible here:**  
👉 **https://nima-movie-recommender.streamlit.app/**

Users can:
- Enter a movie title
- Instantly receive content-based movie recommendations
- Interact with a clean and intuitive web interface built using **Streamlit**

---

## ✨ Features

- **Data Preprocessing**  
  Cleans and transforms raw movie metadata into a structured format for analysis.
  
- **Content-Based Filtering**  
  Recommends movies based on similarity in genres, keywords, cast, crew, and storyline.

- **Natural Language Processing (NLP)**  
  - Text normalization using stemming  
  - Feature extraction using **CountVectorizer**  
  - Combines multiple text attributes into a unified representation

- **Cosine Similarity**  
  Calculates similarity between movies using vector space modeling.

- **Interactive Web Application**  
  Deployed using **Streamlit**, allowing users to explore recommendations in real time.

---

## 📊 Dataset

This project uses the **TMDB 5000 Movies Dataset** sourced from **Kaggle**, which includes:

- **Movies Metadata**  
  (genres, keywords, overview, etc.)

- **Credits Data**  
  (cast and crew information)

These datasets are merged and processed to build a comprehensive feature set for the recommendation system.

---

## 🛠️ Technologies & Dependencies

The following Python libraries are used:

- `numpy`
- `pandas`
- `ast`
- `nltk`  
  - PorterStemmer
- `scikit-learn`  
  - CountVectorizer  
  - cosine_similarity
- `streamlit` (for deployment)

---

## 🎯 Learning Outcomes

This project demonstrates:
- Building a **content-based recommendation system**
- Applying **NLP techniques** to real-world datasets
- Feature engineering from unstructured text data
- Measuring similarity using **cosine similarity**
- Deploying machine learning applications using **Streamlit**

---

