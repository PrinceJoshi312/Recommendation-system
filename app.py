import streamlit as st
import pickle

import gdown
import os


# Google Drive File ID (Replace with your actual File ID)
FILE_ID = "1D013wiAbMWBv-2uQgkdm4PBynyeaiZqC"
OUTPUT_FILE = "similarity.pkl"

# Function to download similarity.pkl if it doesn’t exist
def download_similarity():
    if not os.path.exists(OUTPUT_FILE):
        url = f"https://drive.google.com/uc?id={FILE_ID}"
        gdown.download(url, OUTPUT_FILE, quiet=False)
        print("✅ similarity.pkl downloaded successfully!")

# Download the file before loading it
download_similarity()

# Load similarity.pkl
similarity = pickle.load(open(OUTPUT_FILE, "rb"))


# Load preprocessed data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    
    recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    
    return recommended_movies

# Streamlit UI
st.title("🎬 Movie Recommendation System")

# Dropdown to select a movie
selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.write("### Recommended Movies:")
    for rec in recommendations:
        st.write(f"- {rec}")
