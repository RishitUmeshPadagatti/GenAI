# Explore pre-trained word vectors. Explore word relationships using vector arithmetic. Perform arithmetic operations and analyze results.

import gensim.downloader as api

model = api.load("word2vec-google-news-300")

queen_vector = model["king"] - model["man"] + model["woman"]
queen_words = model.similar_by_vector(queen_vector)
print(f"Top 5 words similar to 'king - man + woman': {queen_words}")

actor_vector = model["actor"] - model["man"] + model["woman"]
actor_words = model.similar_by_vector(actor_vector, topn=5)
print(f"Top 5 words similar to 'actor - man + woman': {actor_words}")