# Load a pre-trained Hugging Face summarization pipeline and generate a summary from input text.

from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

long_text = """
The Industrial Revolution, which took place from the 18th to the 19th centuries,
was a period during which predominantly agrarian, rural societies in Europe and
America became industrial and urban.
"""

summary = summarizer(
    long_text,
    max_length=40,
    min_length=30,
    do_sample=False
)

print("Summary:")
print(summary[0]['summary_text'])