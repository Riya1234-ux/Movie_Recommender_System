import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{int(movie_id)}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=10
        )
        response.raise_for_status()

        data = response.json()

        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:]

    recommended_movies = []
    recommended_movie_posters = []

    for i in movies_list:
        movie_id = int(movies.iloc[i[0]].movie_id)

        poster = fetch_poster(movie_id)

        # Skip movies with missing posters
        if poster is None:
            continue

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(poster)

        if len(recommended_movies) == 5:
            break

    return recommended_movies, recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    names,posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i], use_container_width=True)


