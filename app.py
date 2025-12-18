import os
import streamlit as st
import pickle
import pandas as pd
import requests
from dotenv import load_dotenv
import gdown

load_dotenv()
api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError('API_KEY environment variable is not set')


def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    )
    data = response.json()

    if data.get('poster_path'):
        return 'https://image.tmdb.org/t/p/w500' + data['poster_path']
    else:
        return None

def recommend(movie_name):
    movie_index = movies[movies['title'] == movie_name].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), key=lambda x: x[1], reverse=True)[1:6]

    recommendations = []
    recommendation_posters = []
    for movie in movies_list:
        movie_id = movies.loc[movie[0],'movie_id']
        recommendations.append(movies.loc[movie[0],'title'])
        #fetch poster from API
        recommendation_posters.append(fetch_poster(movie_id))

    return recommendations,recommendation_posters


import streamlit as st

movies_file_id = '1E6laZy9WNY3PgFsPJ3ItkkiiZ6j-JyJq'
similarity_file_id = '1lAs1WmkI5UhtMTAZvE5UFLGEw3ZK2wSF'
@st.cache_data
def load_pickles():
    if not os.path.exists("movies_dict.pkl"):
        gdown.download(f"https://drive.google.com/uc?id={movies_file_id}", "movies_dict.pkl", quiet=False)
    if not os.path.exists("similarity.pkl"):
        gdown.download(f"https://drive.google.com/uc?id={similarity_file_id}", "similarity.pkl", quiet=False)

    with open("movies_dict.pkl", "rb") as f:
        movies_dict = pickle.load(f)
    with open("similarity.pkl", "rb") as f:
        similarity = pickle.load(f)
    return movies_dict, similarity

movies_dict, similarity = load_pickles()
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender')


selected_movie_name = st.selectbox('Choose a movie...',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        if posters[0]:
            st.image(posters[0])
        else:
            st.text('No poster')
    with col2:
        st.text(names[1])
        if posters[1]:
            st.image(posters[1])
        else:
            st.text('No poster')
    with col3:
        st.text(names[2])
        if posters[2]:
            st.image(posters[2])
        else:
            st.text('No poster')
    with col4:
        st.text(names[3])
        if posters[3]:
            st.image(posters[3])
        else:
            st.text('No poster')
    with col5:
        st.text(names[4])
        if posters[4]:
            st.image(posters[4])
        else:
            st.text('No poster')



