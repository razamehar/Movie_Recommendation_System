# RECOMMENDER SYSTEM

## OBJECTIVE
This project utilizes several recommendation techniques to provide effective suggestions. Popularity-based recommendations are implemented using Bayesian averages to rank items. Content-based recommendations leverage cosine similarity to suggest items similar to a user's preferences. Additionally, collaborative filtering is implemented using the Surprise library, incorporating both user-based and item-based approaches to enhance personalization.

## ALGORITHMS
### Content-Based Filtering
This algorithm recommends movies based on their content attributes, such as cast, crew, keywords, overview, and title. The algorithm utilizes TF-IDF Vectorization and Cosine Similarity to determine the similarity between movies.

### Collaborative Filtering
Collaborative filtering is further divided into two methods:

#### User-Based Collaborative Filtering
This algorithm recommends movies based on the preferences of users who are similar to the target user. It uses user ratings to identify and suggest movies that similar users have rated highly.

#### Item-Based Collaborative Filtering
This algorithm recommends movies based on the similarity of items that the user has liked or rated highly in the past.

### Popularity-Based Recommendations
This algorithm leverages both movie popularity and ratings to provide balanced recommendations. It calculates a Bayesian average of movie ratings to score movies effectively.

## INSTALLATION
To set up the project, run the following commands:
```bash
pip install pandas==2.2.3
pip install surprise==1.1.4
pip install neattext==0.1.3
```

## USAGE
1. Clone the repository
```bash
git clone <repository-url>
cd <repository-folder>
```

2. Run the scrip
```bash
python script_name.py
```

3. Follow the prompts to choose a recommendation method:

- Enter 1 for Data Review
- Enter 2 for Popularity-Based Content Filtering
- Enter 3 for Item-Similarity-Based Content Filtering
- Enter 4 for User-Based Collaborative Filtering
- Enter 5 for Item-Based Collaborative Filtering

## Data Sources
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset?select=ratings.csv

## License
This project is licensed under the Raza Mehar License. See the LICENSE.md file for details.

## Contact
For any questions or clarifications, please contact Raza Mehar at [raza.mehar@gmail.com].