### Data Download & Review
import pandas as pd
import ast
import neattext.functions as nt
from utility import fetch_details
from recommender.popularity import popularity_rec
from recommender.context import content_rec
from review import review

print('Loading............\n')

movies_df = pd.read_csv('data/movies.csv', low_memory=False) #  loads the whole CSV file at once
credits_df = pd.read_csv('data/credits.csv')
keywords_df = pd.read_csv('data/keywords.csv')

user_inp = input('Do you want to review the data frames? (y/n): ')
if user_inp == 'y':
    review(movies_df)
    print()
else:
    print()

"""### Data Preprocessing"""

movies_df.drop(['belongs_to_collection', 'budget', 'homepage', 'imdb_id', 'poster_path', 'production_companies',
       'production_countries', 'revenue', 'runtime', 'release_date', 'spoken_languages', 'tagline', 'original_title', 'video', 'status'], axis=1, inplace=True)

#print(movies_df.isnull().sum())
movies_df.dropna(inplace=True)
#print(movies_df.isnull().sum())

#print(movies_df.duplicated().sum())
movies_df.drop_duplicates(inplace=True)
#print(movies_df.duplicated().sum())

movies_df['id'] = movies_df['id'].astype('int')
movies_df['popularity'] = movies_df['popularity'].astype('float64')

sub_merged_df = pd.merge(movies_df, credits_df, on='id', how='left')
merged_df = pd.merge(sub_merged_df, keywords_df, on='id', how='left')

#print(movies_df.isnull().sum())
movies_df.dropna(inplace=True)
#print(movies_df.isnull().sum())

final_df = merged_df.sample(3000).reset_index(drop=True)

del movies_df, credits_df, keywords_df, merged_df

final_df = final_df.dropna(subset=['title', 'genres'])

final_df['genres'] = final_df['genres'].apply(lambda x: fetch_details(ast.literal_eval(x)))
final_df['crew'] = final_df['crew'].apply(lambda x: fetch_details(ast.literal_eval(x), director=True))
final_df['cast'] = final_df['cast'].apply(lambda x: fetch_details(ast.literal_eval(x), character=True))
final_df['keywords'] = final_df['keywords'].apply(lambda x: fetch_details(ast.literal_eval(x)))

print('POPULARITY BASED RECOMMENDATION')
count = input('How many recommendation do you want? ')
if count.strip() == '' or not count.isdigit():
    popularity_rec(final_df)
    print()
else:
    count = int(count)
    popularity_rec(final_df, count)
    print()

final_df['content'] = final_df['genres'] + ' ' + final_df['crew'] + ' ' + final_df['cast'] + ' ' + final_df['keywords'] + ' ' + final_df['overview']
final_df['content'] = final_df['content'].apply(nt.remove_stopwords)
final_df['content'] = final_df['content'].apply(nt.remove_special_characters)

print('CONTEXT BASED RECOMMENDATION')
movie_title = input('Type a movie title: ')
content_rec(movie_title, final_df)
print()

