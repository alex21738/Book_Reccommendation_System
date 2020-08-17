# Final-Project-Rec-System

## Outline

- Project Background

- Dataset Introduction

- EDA

- Model

- Front End

- Further Exploration

## Project Goal

The goal of this project is to create a content-based item-to-item recommendation system for books. 

## Data Introduction

The data was collected from Figshare, originally web scrapped from audible.com by Figshare account XinYuan Wang 2020. The data obtained 2 CSV files which covers all released books in the second half year of 2019. Important features in data includes book title, book author, book genre and book description.The files contain approximately 30,000 observations. 

## EDA

The graphic below shows distribution of each genre.
![Distribution_of_genres.png](Pictures/Distribution_of_genres.png)

The graphic below shows average description word counts of each genre.
![Average_description_word_count_by_genre.png](Pictures/Average_description_word_count_by_genre.png)

The graphic below shows the top 30 frequent words in 1000 randomly chosed samples with no limitation.

![Most_frequent_words_in_1000_samples_(original).png](Pictures/Most_frequent_words_in_1000_samples_(original).png)

The graphic below shows the top 30 frequent words in 1000 randomly chosed samples which captures only nouns.

![Most_frequent_words_in_1000_samples_(noun_only).png](Pictures/Most_frequent_words_in_1000_samples_(noun_only).png)

The graphic below shows the different top 20 frequent nouns between fiction and nonfiction.

![Most_frequent_words_in_fiction_vs_nonfiction.png](Pictures/Most_frequent_words_in_fiction_vs_nonfiction.png)

The graphic below shows the different word cloud between fiction and nonfiction.

![Fiction_word_cloud.png](Pictures/Fiction_word_cloud.png)
![Nonfiction_word_cloud.png](Pictures/Nonfiction_word_cloud.png)

## Data Prepping

- Remove HTML signs by Regex before tokenozed each word.

- Create function for NLP to filter noun only in book descriptions.

## Model

### Cosine Similarity

### Euclidean Similarity

### Spacy

- Accuracy results: Cosine similarity >= Spacy >> Euclidean similarity
  
## Insightful Analysis

- Adopt Gensim corpus model
 
- Choose words only show 30 times or more

- Remove words show more than 50% 

## Front End Video
- Click the picture below to see how book recommendation system works on Youtube

<a href="https://youtu.be/maAx_2QrXkY"
 target="_blank"><img src="https://bookishivy.files.wordpress.com/2015/09/book-recs.png?w=500&h=200&crop=1" 
alt="Front End Demonstration" width="240" height="180" border="10" /></a>

 
## Further Exploration
 
- Enlarge the database to be more precise on making recommendations

- Adopt A/B test to examine recommendation system performances

- Create a user-friendly searching environment by returning recommendations based on the closest input 

## Powerpoint Link

- https://docs.google.com/presentation/d/1wbjuVWIcBha6r8QYgq8sT3KRWGvLQbgOvF6AJrtOs3M/edit?usp=sharing
