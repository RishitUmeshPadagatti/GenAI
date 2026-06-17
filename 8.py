# Install LangChain and Cohere, load a document, and create a formatted prompt template.

import os
from langchain_cohere import ChatCohere

os.environ["COHERE_API_KEY"] = "..."

file_path = "8.text1.txt"
with open(file_path, "r", encoding="utf-8") as file:
    document_text = file.read()
print("Original Document:\n", document_text)

llm = ChatCohere()

prompt = f"""
You are a helpful assistant.
Given the following document, summarize it in bullet points.

Document:
{document_text}

Summary:
"""

response = llm.invoke(prompt)

print(response.content)











# import os
# from langchain_cohere import ChatCohere
# from langchain_core.prompts import PromptTemplate

# os.environ["COHERE_API_KEY"] = "..."

# file_path = "8.text1.txt"
# with open(file_path, "r", encoding="utf-8") as file:
#     document_text = file.read()
# print("Original Document:\n", document_text)

# llm = ChatCohere()

# prompt = PromptTemplate(
#     input_variables=["document"],
#     template="""
# You are a helpful assistant
# Give the following document, summarize it in bullet points
# Document:
# {document}

# Summary:
# """
# )

# chain = prompt | llm

# response = chain.invoke({"document": document_text})

# print("\nSummary: \n", response.content)