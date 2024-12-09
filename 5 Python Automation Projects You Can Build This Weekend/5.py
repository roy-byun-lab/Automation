"""
Personal Movie Recommendation System

This system works out similarities between users of their ratings of movies and recommends movies based on these similarities
If you have ever used Netflix or Spotify, you have interacted with a similar recommendation engine.

What You’ll Need:
    1.pandas (For data handling)
    2.sklearn (For collaborative filtering)
    3.numpy (For numerical operations)
"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Example user-movie rating data (you can load your own dataset)
data = {
    'user': ['Alice', 'Bob', 'Charlie', 'David'],
    'Movie A': [5, 4, 1, 0],
    'Movie B': [3, 5, 2, 0],
    'Movie C': [4, 3, 5, 0],
    'Movie D': [0, 1, 3, 5]
}
df = pd.DataFrame(data)

# Compute the cosine similarity between users
user_ratings = df.drop('user', axis=1).values
"""
user_ratings
[
    [5, 3, 4, 0],  # Alice
    [4, 5, 3, 1],  # Bob
    [1, 2, 5, 3],  # Charlie
    [0, 0, 0, 5]   # David
]
"""
cosine_sim = cosine_similarity(user_ratings)
"""
cosine_sim
[
 #  Alice       Bob            Charlie    David
    [1.        , 0.97590007, 0.56613852, 0.        ],  # The similarity between Alice and other users
    [0.97590007, 1.        , 0.76063883, 0.        ],  # Bob
    [0.56613852, 0.76063883, 1.        , 0.        ],  # Charlie
    [0.        , 0.        , 0.        , 1.        ]   # David
]
 ⇒ Alice is similar to Bob.
"""

# Create a function to recommend movies based on similarity
def recommend_movies(user_id):
    similar_users = list(enumerate(cosine_sim[user_id]))
    similar_users = sorted(similar_users, key=lambda x: x[1], reverse=True)
    
    recommended_movies = []
    for i, _ in similar_users[1:]:
        recommended_movies.append(df.columns[i+1])
    
    return recommended_movies

# Example: Recommend movies for user 0 (Alice)
recommended = recommend_movies(0)
print(f"Recommended movies for Alice: {recommended}")