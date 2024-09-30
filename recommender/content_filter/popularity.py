# This algorithm is a popularity-based recommendation algorithm that leverages both movie popularity and ratings 
# to provide a more balanced list of recommendations.

from utility import customer_scaler, fetch_details
import pandas as pd

def bayesian_avg(R, v, m, C):
    return (v * 1/(v + m)) * R + ((m * 1/(v + m))) * C

def popularity_rec(df, count=5):

    print('POPULARITY-BASED CONTENT FILTERING')
    print('-' * 50)

    max_value = df['popularity'].max()

    df['popularity'] = df['popularity'].apply(lambda x: customer_scaler(x, max_value) if pd.notna(x) else x)
    m = df['vote_count'].quantile(0.90)
    C = df['vote_average'].mean()
    
    df['bayesian_avg'] = bayesian_avg(df['vote_average'], df['vote_count'], m, C)
    df['score'] = round(df['popularity'] * 0.4 + df['bayesian_avg'] * 0.6, 3)
    movies_list = df.sort_values(by='score', ascending=False, inplace=True)
    
    print(f"{'ID':<10}{'Movie Title':<60}{'Genre':<60}{'Score':<10}")
    print("-" * 140)
    
    for i in range(count):
        movie_id = str(df.iloc[i]['id']).ljust(10)
        title = df.iloc[i]['title'].ljust(60)
        genres = df.iloc[i]['genres'].ljust(60) if isinstance(df.iloc[i]['genres'], str) else ', '.join(df.iloc[i]['genres']).ljust(60)
        score = str(df.iloc[i]['score']).ljust(10)
        
        print(f"{movie_id}{title}{genres}{score}")