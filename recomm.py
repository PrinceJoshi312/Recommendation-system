import numpy as np
import pandas as pd
import ast
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets from Kaggle
movies = pd.read_csv('C:/Users/HP/OneDrive/Desktop/recommend/tmdb_5000_movies.csv')
credits = pd.read_csv('C:/Users/HP/OneDrive/Desktop/recommend/tmdb_5000_credits.csv')

# Merge datasets
movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

# Functions for data processing
def convert(text):
    try:
        return [i['name'] for i in ast.literal_eval(text)]
    except:
        return []

def convert3(text):
    try:
        return [i['name'] for i in ast.literal_eval(text)[:3]]
    except:
        return []

def fetch_director(text):
    try:
        return [i['name'] for i in ast.literal_eval(text) if i['job'] == 'Director']
    except:
        return []

def collapse(L):
    return [i.replace(" ", "") for i in L]

# Apply transformations
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert3)
movies['crew'] = movies['crew'].apply(fetch_director)

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)

# Process overview and create "tags" column
movies['overview'] = movies['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
movies = movies[['movie_id', 'title', 'tags']]

# Convert tags to string format
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

# Vectorization using TF-IDF
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vector = tfidf.fit_transform(movies['tags']).toarray()

# Compute similarity
similarity = cosine_similarity(vector)

# Save preprocessed data
pickle.dump(movies, open('movie_list.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

# Load saved models
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found"]
    
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), reverse=True, key=lambda x: x[1])
    
    recommended_movies = [movies.iloc[i[0]].title for i in distances[1:6]]
    
    return recommended_movies

# Example usage
print(recommend("Batman"))
