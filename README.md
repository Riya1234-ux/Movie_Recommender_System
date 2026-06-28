# 🎬 Movie Recommender System

A **Content-Based Movie Recommendation System** built using **Python**, **Streamlit**, and **Machine Learning**. The application recommends movies based on their semantic similarity by leveraging **Cosine Similarity** over engineered movie feature vectors. It also integrates the **TMDB API** to dynamically fetch high-quality movie posters, providing an interactive and user-friendly recommendation experience.

---

## 🚀 Features

* 🎯 Content-Based Recommendation Engine using **Cosine Similarity**
* 🎬 Recommends the **Top-5 most similar movies**
* 🖼️ Fetches movie posters dynamically using the **TMDB API**
* ⚡ Fast recommendations through precomputed similarity matrices
* 💻 Interactive and responsive web application built with **Streamlit**
* 📦 Optimized model loading using serialized Pickle artifacts

---

## 🛠️ Tech Stack

| Category                 | Technologies                               |
| ------------------------ | ------------------------------------------ |
| Language                 | Python                                     |
| Frontend                 | Streamlit                                  |
| Data Processing          | Pandas, NumPy                              |
| Machine Learning         | Scikit-learn                               |
| Recommendation Algorithm | Content-Based Filtering, Cosine Similarity |
| API                      | TMDB API                                   |
| Serialization            | Pickle                                     |
| Version Control          | Git & GitHub                               |

---

## 📊 Project Overview

* **Dataset:** TMDB 5000 Movies Dataset
* **Recommendation Technique:** Content-Based Filtering
* **Similarity Measure:** Cosine Similarity
* **Movies Indexed:** ~5000
* **Poster Retrieval:** TMDB REST API
* **Deployment:** Streamlit (Cloud-ready)

---

## ⚙️ System Workflow

1. Preprocess movie metadata and extract relevant textual features.
2. Convert features into numerical vector representations.
3. Compute pairwise **Cosine Similarity** between movie vectors.
4. Serialize processed artifacts (`movie_dict.pkl` & `similarity.pkl`) for efficient inference.
5. Recommend the Top-5 most similar movies based on the selected title.
6. Fetch corresponding movie posters using the TMDB API.
7. Display recommendations through an interactive Streamlit interface.

---

## 📂 Project Structure

```text
Movie_Recommender_System/
│── app.py
│── requirements.txt
│── movie_dict.pkl
│── similarity.pkl*
│── .gitignore
│── README.md
```

> **Note:** `similarity.pkl` is excluded from this repository because it exceeds GitHub's 100 MB file size limit. The application is configured to download the file separately during deployment.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/Riya1234-ux/Movie_Recommender_System.git
```

Navigate to the project directory

```bash
cd Movie_Recommender_System
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---
<img width="572" height="370" alt="Screenshot 2026-06-28 215951" src="https://github.com/user-attachments/assets/510664a8-f6f1-44db-85b1-cd5dd0c962d3" />


---

## 🔮 Future Enhancements

* Hybrid Recommendation System (Content-Based + Collaborative Filtering)
* Personalized recommendations using user preferences
* Advanced search with autocomplete
* Genre, language, and rating-based filtering
* Cloud deployment with automated model artifact retrieval
* Recommendation explanation module
