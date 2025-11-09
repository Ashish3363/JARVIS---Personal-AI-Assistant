
# # query.py
import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone
from ollama import chat


# ====== CONFIG ======
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "personal-ai-notes"
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLAMA_MODEL = "tinyllama:1.1b"
# ====================

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Connect to the index
index = pc.Index(INDEX_NAME)

# Load embedding model
embedder = SentenceTransformer(EMBED_MODEL)


def get_answer(query_text: str):
    # Embed the query
    query_embedding = embedder.encode(query_text).tolist()

    # Retrieve top 3 matches from Pinecone
    result = index.query(
        vector=query_embedding,
        top_k=3,
        include_metadata=True
    )

    # Combine retrieved chunks as context
    sources = [match['metadata']['text'] for match in result['matches']]
    context = "\n\n".join(sources)

    # Create prompt for TinyLLaMA
    prompt = f"""
You are a helpful AI assistant.

Use ONLY the information provided in the context below to answer the question.
If the answer is not found in the context, respond exactly with: "I don't know."
Do NOT use any outside knowledge or make assumptions.

Context:
{context}

Question: {query_text}
"""

    # Get answer from TinyLLaMA
    response = chat(model=LLAMA_MODEL, messages=[{"role": "user", "content": prompt}])

    return response['message']['content']


if __name__ == "__main__":
    while True:
        q = input("\nAsk something (or 'exit'): ")
        if q.lower() == "exit":
            break
        ans = get_answer(q)
        print("\nAnswer:", ans)




# # query.py
# import os
# from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer
# from pinecone import Pinecone
# from ollama import chat
# import pyttsx3  # <-- Added for speaking

# # ====== CONFIG ======
# PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
# INDEX_NAME = "personal-ai-notes"
# EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
# LLAMA_MODEL = "tinyllama:1.1b"
# # ====================

# # Initialize Pinecone
# pc = Pinecone(api_key=PINECONE_API_KEY)

# # Connect to the index
# index = pc.Index(INDEX_NAME)

# # Load embedding model
# embedder = SentenceTransformer(EMBED_MODEL)

# # Initialize text-to-speech engine
# tts_engine = pyttsx3.init()


# def speak_text(text: str):
#     """Speak the given text using TTS."""
#     tts_engine.say(text)
#     tts_engine.runAndWait()


# def get_answer(query_text: str):
#     # Embed the query
#     query_embedding = embedder.encode(query_text).tolist()

#     # Retrieve top 3 matches from Pinecone
#     result = index.query(
#         vector=query_embedding,
#         top_k=3,
#         include_metadata=True
#     )

#     # Combine retrieved chunks as context
#     sources = [match['metadata']['text'] for match in result['matches']]
#     context = "\n\n".join(sources)

#     # Create prompt for TinyLLaMA
#     prompt = f"""
# You are a helpful AI. 

# Instructions:
# 1. First, try to answer the question using ONLY the information provided in the context.
# 2. If the answer is present in the context, respond using that information.
# 3. If the answer is NOT in the context, you are allowed to answer using your general knowledge.
# 4. Do NOT make up information; always be truthful.

# Context:
# {context}

# Question: {query_text}
# """

#     # Get answer from TinyLLaMA
#     response = chat(model=LLAMA_MODEL, messages=[{"role": "user", "content": prompt}])
#     answer = response['message']['content']

#     # Speak the answer
#     speak_text(answer)

#     return answer


# if __name__ == "__main__":
#     while True:
#         q = input("\nAsk something (or 'exit'): ")
#         if q.lower() == "exit":
#             break
#         ans = get_answer(q)
#         print("\nAnswer:", ans)

