WORKING VIDEO-->https://drive.google.com/file/d/1gxN0Hox9zGkvXn2cI72yZu5Yq-ZFu5xk/view?usp=sharing

JARVIS is a locally hosted personal AI assistant designed to provide intelligent and context-aware responses.
It integrates Ollama (using the TinyLlama model) as its core AI engine to process natural language queries efficiently without relying on cloud-based APIs.
The assistant can retrieve answers from user-provided data as well as generate intelligent responses using the model’s internal knowledge when question is out of ingested data.

Key Components and Functionality:
1.Local AI Model (Ollama with TinyLlama):
  The TinyLlama model runs locally via Ollama, ensuring data privacy and fast inference.
  This eliminates dependency on external servers, making JARVIS a secure and offline-capable assistant.
2.Vector Database (Pinecone):
  JARVIS uses Pinecone as a vector database to store and manage ingested data embeddings.
  When a user provides new information (documents, notes, etc.), that data is processed and converted into vector embeddings, which are stored in Pinecone.
  During query time, Pinecone performs semantic similarity searches to find the most relevant pieces of information related to the user’s question.
3.Data Ingestion:
  Users can upload or input their own data (text files, notes, knowledge base, etc.).
  The system encodes and stores this data in the vector database to make it searchable and retrievable later.
4.Query Processing:
  When a user asks a question, JARVIS first searches for relevant information in the ingested data using the vector similarity search from Pinecone.
  If relevant data is found, the model uses only that information to generate an accurate and context-specific answer.
  If the question is not covered in the ingested data, the model relies on its own trained intelligence (TinyLlama’s base knowledge) to generate a response.
5.Backend and API:
  The backend of JARVIS is built using FastAPI, a modern, high-performance Python web framework.
  FastAPI acts as the server that connects the frontend (user interface) with the Ollama model and Pinecone database.
