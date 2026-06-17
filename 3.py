# Train a custom Word2Vec model on a small dataset. 
# Train embeddings on a domain-specific corpus (e.g., legal, medical) and analyze how embeddings capture domain-specific semantics.

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy as np
from gensim.models import Word2Vec

medical_corpus = [
    "The patient was diagnosed with diabetes and hypertension.",
    "MRI scans reveal abnormalities in the brain tissue.",
    "The treatment involves antibiotics and regular monitoring.",
    "Symptoms include fever, fatigue, and muscle pain.",
    "The vaccine is effective against several viral infections.",
    "Doctors recommend physical therapy for recovery.",
    "The clinical trial results were published in the journal.",
    "The surgeon performed a minimally invasive procedure.",
    "The prescription includes pain relievers and anti-inflammatory drugs.",
    "The diagnosis confirmed a rare genetic disorder."
]

processed_corpus = []

for sentence in medical_corpus:
    processed_corpus.append(sentence.lower().split())

model = Word2Vec(
    sentences=processed_corpus,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4,
    epochs=50
)

words = model.wv.index_to_key

embeddings = []

for word in words:
    embeddings.append(model.wv[word])

embeddings = np.array(embeddings)

pca = PCA(n_components=2)
pca_result = pca.fit_transform(embeddings)

plt.figure(figsize=(10, 8))
plt.scatter(pca_result[:, 0], pca_result[:, 1])

for i, word in enumerate(words):
    plt.annotate(
        word,
        (pca_result[i, 0], pca_result[i, 1]),
        fontsize=8
    )

plt.title("Word Embeddings Visualization (Medical Domain)")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.grid(True)
plt.show()

def find_similar_words(input_word, top_n=5):
    try:
        similar_words = model.wv.most_similar(input_word, topn=top_n)

        print(f"\nWords similar to '{input_word}':")

        for word, similarity in similar_words:
            print(f"{word} ({similarity:.2f})")

    except KeyError:
        print(f"'{input_word}' not found in vocabulary.")

find_similar_words("treatment")
find_similar_words("vaccine")