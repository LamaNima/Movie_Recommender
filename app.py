import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommended_movies = []
    for item in movies_list:
        movie_id = item[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[item[0]]['title'])

    return recommended_movies

similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

movies_list = movies['title'].values
st.title("Movie Recommender")

selected_movie_name = st.selectbox(
    '',movies_list
)

if st.button('RECOMMEND'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

