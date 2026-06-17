# Use word embeddings to create meaningful sentences for creative tasks. Retrieve similar words for a seed word. 
# Create a sentence or story using these words as a starting point. Write a program that: Takes a seed word. Generates similar words. 
# Constructs a short paragraph using these words.

import gensim.downloader as api
import random

# model = api.load("glove-wiki-gigaword-100")
model = api.load("word2vec-google-news-300")

def create_paragraph(seed_word):
    if seed_word not in model:
        return f"No similar words found for '{seed_word}'."

    similar_words = []
    for word, score in model.most_similar(seed_word, topn=10):
        similar_words.append(word)

    random.shuffle(similar_words)
    selected_words = similar_words[:5]

    paragraph = f"In a world defined by {seed_word}, "
    paragraph += f"people found themselves surrounded by {', '.join(selected_words[:-1])}, and {selected_words[-1]}. "
    paragraph += f"These ideas shaped their thoughts and actions bringing them closer to understanding the true meaning of {selected_words[0]}."

    return paragraph

seed = "freedom"
print(create_paragraph(seed))