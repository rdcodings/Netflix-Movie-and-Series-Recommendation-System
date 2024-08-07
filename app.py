#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load your Netflix dataset
netflix = pd.read_csv(r'C:\Users\Rajarshi Das\Documents\netflix_titles.csv')  # Replace with your dataset path

# Fill NA values
filledna = netflix.fillna('')
def clean_data(x):
    return str.lower(x.replace(" ", ""))

# Apply data cleaning
features = ['title', 'director', 'cast', 'listed_in', 'description']
for feature in features:
    filledna[feature] = filledna[feature].apply(clean_data)

# Create a "soup" of words
def create_soup(x):
    return x['title'] + ' ' + x['director'] + ' ' + x['cast'] + ' ' + x['listed_in'] + ' ' + x['description']

filledna['soup'] = filledna.apply(create_soup, axis=1)

# Vectorize the "soup"
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(filledna['soup'])

# Compute cosine similarity matrix
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

# Reset index and create a series for title indices
filledna = filledna.reset_index()
indices = pd.Series(filledna.index, index=filledna['title'])

# Function to get recommendations
def get_recommendation_new(title, cosine_sim=cosine_sim2):
    title = title.replace(' ', '').lower()
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return netflix['title'].iloc[movie_indices]

# Streamlit app code
st.title('Movie Recommender System')

movie_title = st.text_input('Enter a Movie or Series Title:', 'Type a Movie or Series')

if st.button('Recommend'):
    recommendations = get_recommendation_new(movie_title)
    st.write('Recommended Movies/Series:')
    for movie in recommendations:
        st.write(movie)

