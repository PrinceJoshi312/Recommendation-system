# 🎬 Movie Recommendation System

A **content-based movie recommender system** built with **Streamlit**, powered by **TMDB 5000 Movie Dataset** and **scikit-learn**, that suggests similar movies based on your selection.
This project is designed for educational purposes and interactive demos.

---

## 🚀 Features

* ✅ Recommend similar movies based on title selection
* ✅ Uses cosine similarity between movie overviews, genres, cast, and crew
* ✅ Clean, responsive Streamlit UI
* ✅ Loads data efficiently with pickled preprocessing

---

## 🧠 How It Works

1. **Data** from TMDB 5000 Movies & Credits is cleaned and merged.
2. **Features** like genres, keywords, cast, director are extracted and combined.
3. **Vectorization** using CountVectorizer.
4. **Cosine Similarity** is computed to find the most similar movies.

---

## 📁 Project Structure

```
.
├── app.py                     # Streamlit web app
├── recomm.py                 # Recommendation logic
├── movie_list.pkl            # Pickled movie list for faster loading
├── Recommendation System.ipynb  # Development notebook
├── tmdb_5000_movies.csv      # Movie dataset
├── tmdb_5000_credits.csv     # Credits dataset
├── requirements.txt          # Python dependencies
├── .gitignore
└── README.md
```

---

## 🛠️ Installation

1. **Clone the repo**

```bash
git clone https://github.com/PrinceJoshi312/<your-repo-name>.git
cd <your-repo-name>
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

---

## 📦 Requirements

All dependencies are listed in `requirements.txt`. Key libraries include:

* `pandas`
* `scikit-learn`
* `nltk`
* `streamlit`
* `pickle`


## 🙋‍♂️ Author

**Prince Joshi**
GitHub: [@PrinceJoshi312](https://github.com/PrinceJoshi312)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
.
