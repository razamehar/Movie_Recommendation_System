### Data Download & Review
import pandas as pd
from recommender.content_filter.popularity import popularity_rec
from recommender.content_filter.item_similarity import content_rec
from recommender.collaborative_filter.item import item_rec
from recommender.collaborative_filter.user import user_rec


from review import review
from preprocess import preprocess

print('Loading the data......\n')

movies_df = pd.read_csv('data/movies.csv', low_memory=False) #  loads the whole CSV file at once
credits_df = pd.read_csv('data/credits.csv')
keywords_df = pd.read_csv('data/keywords.csv')

print('Processing the data......\n')
final_df = preprocess(movies_df, credits_df, keywords_df)

print('Select an option based on the following:')
print('-' * 50)
print('Enter 1 for Data Review')
print('Enter 2 for Popularity-Based Content Filtering')
print('Enter 3 for Item-Similarity-Based Content Filtering')
print('Enter 4 for User-Based Collaborative Filtering')
print('Enter 5 for Item-Based Collaborative Filtering')
print('Enter any other key to quit')

user_inp = input()

try:
    user_inp = int(user_inp)
    
    if user_inp == 1:
        ratings_df = pd.read_csv('data/ratings_small.csv', low_memory=False)
        review(movies_df)
        review(credits_df)
        review(keywords_df)
        review(ratings_df)

    elif user_inp == 2:
        final_df = final_df.sample(5000).reset_index(drop=True)
        count = input('How many recommendations do you want? ')
        if count.strip() == '' or not count.isdigit():
            popularity_rec(final_df)
        else:
            count = int(count)
            popularity_rec(final_df, count)

    elif user_inp == 3:
        final_df = final_df.sample(5000).reset_index(drop=True)
        movie_title = input('Type a movie title: ')
        content_rec(movie_title, final_df)

    elif user_inp == 4:
        user_id = int(input('Enter the user_id: '))
        ratings_df = pd.read_csv('data/ratings_small.csv', low_memory=False)
        item_rec(ratings_df, final_df, user_id)
        
    elif user_inp == 5:
        user_id = int(input('Enter the user_id: '))
        ratings_df = pd.read_csv('data/ratings_small.csv', low_memory=False)
        user_rec(ratings_df, final_df, user_id)

    else:
        print("\nInvalid option, quitting...")
        quit()

except ValueError as E:
    print(f"\nInvalid input, quitting...{E}")
    quit()


