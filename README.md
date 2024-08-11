# Netflix Movie and Series Recommendation System
![Netflix Movie and Series Recommendation System](https://github.com/rdcodings/Netflix-Movie-and-Series-Recommendation-System/blob/5a88d46d337310b997c30dbfe60a59faebb8c3e7/Netflix.webp)

## Introduction
The Netflix Movie and Series Recommendation System is a project designed to recommend both movies and series based on the available dataset from Netflix up to 2021. This system leverages different recommendation algorithms to provide personalized suggestions for users looking to explore new content on Netflix.

## Objective
The primary objective of this project is to develop a recommendation system that can suggest relevant movies and series based on user preferences. By utilizing content-based filtering techniques and analyzing various features from the dataset, the system aims to enhance user experience by offering tailored recommendations.

## Datasets
1. **Netflix Dataset**: Contains comprehensive information about movies and series available on Netflix until 2021. Key features include titles, descriptions, cast, director, and genre.
2. **IMDb Dataset**:
   - `IMDb ratings.csv`: Includes IMDb ratings data.
   - `IMDb movies.csv`: Contains information about movie titles, years, and genres.

## Methodology
1. **Data Preprocessing**: 
   - Clean and preprocess the Netflix dataset by handling missing values and converting text features to a uniform format.
   - Use TF-IDF Vectorizer for analyzing movie descriptions to compute cosine similarity and generate recommendations.
   - Implement content-based filtering on multiple features including title, director, cast, genre, and description to refine recommendations.

2. **Recommendation Algorithms**:
   - **Content-Based Recommendation System**: Utilizes TF-IDF Vectorizer to analyze movie descriptions and compute cosine similarity for generating recommendations based on the content similarity.
   - **Content-Based Filtering on Multiple Metrics**: Combines various features from the dataset into a "soup" of words, which is then analyzed using Count Vectorizer to compute cosine similarity and provide recommendations based on multiple features.

3. **Deployment**: 
   - The recommendation system is deployed using Streamlit, allowing users to interact with the system via a web interface. The deployment script is included in the repository.

## Conclusion
This project demonstrates the effectiveness of content-based filtering techniques for building a recommendation system tailored to both movies and series. By analyzing various features from the Netflix dataset and incorporating additional IMDb data, the system provides users with relevant suggestions. For practical use, the system has been deployed using Streamlit, and a file with the Streamlit deployment code is attached in the repository.

## Additional Information
There is also a file attached in the repository where the recommendation system is deployed using Streamlit, allowing users to interact with the system through a web interface.

---

![Sample](https://github.com/rdcodings/Netflix-Movie-and-Series-Recommendation-System/blob/4b2594f3afe80616c54098e364014ff79e7f2ade/sample.JPG)


Author - *Rajarshi Das*
