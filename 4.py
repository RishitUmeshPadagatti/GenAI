# Use word embeddings to improve prompts for Generative AI model. 
# Retrieve similar words using word embeddings. Use the similar words to enrich a GenAI prompt. 
# Use the AI model to generate responses for the original and enriched prompts. 
# Compare the outputs in terms of detail and relevance.


import os
import gensim.downloader as api
from langchain_cohere import ChatCohere

os.environ["COHERE_API_KEY"] = "..."

# model = api.load("glove-wiki-gigaword-100")
model = api.load("word2vec-google-news-300")

llm = ChatCohere()

prompt = input("Enter prompt: ")

word = input("Enter keyword to enrich: ")

similar_words = []
for word, score in model.most_similar(word, topn=5):
    similar_words.append(word)

enriched_prompt = (
    prompt +
    "\nInclude these related concepts: " +
    ", ".join(similar_words)
)

original = llm.invoke(prompt)
enriched = llm.invoke(enriched_prompt)

print("\nSimilar Words:")
print(similar_words)

print("\nOriginal Response:")
print(original.content)

print("\nEnriched Response:")
print(enriched.content)