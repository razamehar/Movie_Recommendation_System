from utility import fetch_details
import pandas as pd
import ast

def preprocess(movies_df, credits_df, keywords_df):

    movies_df.drop(['belongs_to_collection', 'budget', 'homepage', 'imdb_id', 'poster_path', 'production_companies', 'production_countries', 
                'revenue', 'runtime', 'release_date', 'spoken_languages', 'tagline', 'original_title', 'video', 'status'], axis=1, inplace=True)

    
    # Handle missing and duplicate values.
    movies_df.dropna(inplace=True)
    movies_df.drop_duplicates(inplace=True)

    # Typecast id and popularity columns appropriately.
    movies_df['id'] = movies_df['id'].astype('int')
    movies_df['popularity'] = movies_df['popularity'].astype('float64')

    # Merge the the data frames.
    sub_merged_df = pd.merge(movies_df, credits_df, on='id', how='left')
    final_df = pd.merge(sub_merged_df, keywords_df, on='id', how='left')

    # Handle missing values after the merge.
    final_df.dropna(inplace=True)
    final_df = final_df.dropna(subset=['title', 'genres'])

    # Delete the data frames that are no longer required.
    del movies_df, credits_df, keywords_df, sub_merged_df
 
    final_df['genres'] = final_df['genres'].apply(lambda x: fetch_details(ast.literal_eval(x)))
    final_df['crew'] = final_df['crew'].apply(lambda x: fetch_details(ast.literal_eval(x), director=True))
    final_df['cast'] = final_df['cast'].apply(lambda x: fetch_details(ast.literal_eval(x), character=True))
    final_df['keywords'] = final_df['keywords'].apply(lambda x: fetch_details(ast.literal_eval(x)))

    return final_df
