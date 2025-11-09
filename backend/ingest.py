import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
import pinecone
from dotenv import load_dotenv

# ---------------- CONFIG ----------------
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") 
PINECONE_ENV = "us-east1-gcp"
INDEX_NAME = "personal-ai-notes"       # your index name
PDF_FILE = "my_notes.pdf"              # PDF file path
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"  # 384-dim embeddings
# ---------------------------------------

print("📄 Loading PDF:", PDF_FILE)
loader = PyPDFLoader(PDF_FILE)
docs = loader.load()

print("✂️ Splitting into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(docs)

print("🔢 Creating embeddings...")
embedder = HuggingFaceEmbeddings(model_name=EMBED_MODEL)

# Initialize Pinecone client
pc = pinecone.Client(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

# Create index if it doesn't exist
if INDEX_NAME not in pc.list_indexes():
    print("🆕 Creating Pinecone Index:", INDEX_NAME)
    pc.create_index(
        name=INDEX_NAME,
        dimension=384,
        metric="cosine"
    )

# Connect to index
index = pc.index(INDEX_NAME)

print("⬆️ Uploading embeddings to Pinecone...")
vectors = []
for i, chunk in enumerate(chunks):
    vector = embedder.embed_query(chunk.page_content)
    vectors.append(
        (f"id-{i}", vector, {"text": chunk.page_content})
    )

# Upsert vectors in batches if needed
index.upsert(vectors)

print("✅ Ingestion complete! Your data is now in Pinecone.")
