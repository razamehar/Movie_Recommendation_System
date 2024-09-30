# The algorithm provides recommendations based on the movies that the user has liked or rated highly in the past.

from surprise import Dataset, Reader
from surprise.prediction_algorithms import KNNBasic
from collections import defaultdict

def user_rec(ratings_df, final_df, user_id):
    
    if user_id not in ratings_df['userId'].values:
        print("The specified user ID does not exist in the dataset.")
        return
    
    k = 10
    reader = Reader(rating_scale=(1, 5))
    dataset = Dataset.load_from_df(ratings_df[["userId", "movieId", "rating"]], reader)
    trainset = dataset.build_full_trainset()
    
    # Train the KNN model for user-based filtering
    knn = KNNBasic(sim_options={'name': 'cosine', 'user_based': True}, verbose=False)
    knn.fit(trainset)

    # Compute the similarity matrix
    similarity_matrix = knn.compute_similarities()
    
    # Convert the user ID to Surprise's inner ID format
    inner_id = trainset.to_inner_uid(user_id)

    # Get all users who rated the same movies as the target user
    user_ratings = trainset.ur[inner_id]

    # Sort the user's ratings by score (highest first)
    sorted_user_ratings = sorted(user_ratings, reverse=True, key=lambda x: x[1])

    # Create a dictionary to hold candidate movies and their scores
    candidates_movies = defaultdict(float)

    # For each rated movie, find similar users and their ratings for other movies
    for movie_id, rating in sorted_user_ratings:
        similarities = similarity_matrix[inner_id]  # Get similarities for this user
        for other_user_id, score in enumerate(similarities):  # Iterate over similar users
            if inner_id != other_user_id:
                # Get ratings of the similar user
                for other_movie_id, other_rating in trainset.ur[other_user_id]:
                    # Only recommend movies that the target user hasn't rated yet
                    if other_movie_id not in [m[0] for m in sorted_user_ratings]:
                        candidates_movies[other_movie_id] += score * (other_rating / 5)

    # Sort candidates by score and get the top k
    sorted_candidates_movies = sorted(candidates_movies.items(), key=lambda x: x[1], reverse=True)
    top_k_inner_ids = [x[0] for x in sorted_candidates_movies[:k]]

    # Convert inner IDs back to raw IDs
    top_k_raw_ids = [trainset.to_raw_iid(inner_id) for inner_id in top_k_inner_ids]

    print(f"Top recommendation(s) for user {user_id}:")
    for movie_id in top_k_raw_ids:
        movie_info = final_df[final_df['id'] == movie_id]
        if not movie_info.empty:
            movie_title = movie_info['title'].values[0]
            print(movie_title)
        else:
            pass

# Usage
# user_rec(ratings_df, final_df, user_id)
