# Overview
This project is a content-based movie recommender system that suggests similar movies based on the features of a given movie. The system uses the TMDB 5000 Movies dataset to analyze movie attributes such as genres, keywords, cast, crew, and overview to compute similarities between movies. The recommendations are generated using cosine similarity, which measures the angle between feature vectors to determine how similar two movies are.

# Features
Content-Based Filtering: Recommends movies based on the similarity of their content (genres, keywords, cast, crew, and overview).

Data Preprocessing: Cleans and transforms raw data into a usable format for analysis.

Natural Language Processing (NLP): Uses stemming to normalize words and CountVectorizer to convert text data into numerical vectors.

Cosine Similarity: Computes the similarity between movies using the cosine of the angle between their feature vectors.

User-Friendly Interface: Provides a simple function to input a movie title and receive recommendations.

# Dataset
The dataset used in this project is the TMDB 5000 Movies Dataset imported from kaggle, which includes:
Movies Metadata and
Credits Data

# Dependencies
To run this project, you will need the following Python libraries:
- numpy
- pandas
- ast
- nltk (with PorterStemmer)
- scikit-learn (for CountVectorizer and cosine_similarity)
