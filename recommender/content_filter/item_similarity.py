# This algorithm is a content-based filtering approach that recommends movies based on their content attributes, 
# such as cast, crew, keywords, overview, and title.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import neattext.functions as nt

def content_rec(title, df):

    print('ITEM-SIMILARITY-BASED CONTENT FILTERING')
    print('-' * 50)

    if title not in df['title'].values:
        print("The specified movie title does not exist in the dataset.")
        return

    df['content'] = df['crew'] + ' ' + df['cast'] + ' ' + df['keywords'] + ' ' + df['overview'] + ' ' +  df['title']
    df['content'] = df['content'].apply(nt.remove_stopwords)
    df['content'] = df['content'].apply(nt.remove_special_characters)

    print('Generating the list of movies.....\n')
    print()

    # Extracting genres of the target movie
    target_genres = df.loc[df['title'] == title, 'genres'].values[0]

    # Filtering by genre
    genres_list = target_genres.split(', ')
    genre_filtered_df = df[df['genres'].apply(lambda x: any(genre in x for genre in genres_list))].reset_index(drop=True)

    tf = TfidfVectorizer(max_features=3000) #Limit the number of features to focus on the most indicative content
    vectors = tf.fit_transform(genre_filtered_df['content']).toarray()
    similarity = cosine_similarity(vectors)

    movie_idx = genre_filtered_df[genre_filtered_df['title'] == title].index[0]
    distances = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    print(f"{'ID':<10}{'Movie Title':<60}{'Genre':<20}")
    print("-" * 110)

    for i in movie_list:
        movie_id = str(genre_filtered_df.iloc[i[0]]['id'])
        movie_title = genre_filtered_df.iloc[i[0]]['title'].ljust(60)
        genres = genre_filtered_df.iloc[i[0]]['genres']

        print(f"{movie_id:<10}{movie_title:<40}{genres}")