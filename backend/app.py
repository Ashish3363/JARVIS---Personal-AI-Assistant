
# from fastapi import FastAPI
# from pydantic import BaseModel
# from langchain.chains import RetrievalQA
# from langchain.vectorstores import Pinecone
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.llms import Ollama
# from pinecone import Pinecone

# # Initialize components
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
# pc = Pinecone(api_key="pcsk_64zipo_EQFuDb54th96KgS6jxF837KYRvu9xEJhTQJqVecUpqfMm7vHGAPdvaSUf6H4Q8U")
# index = pc.Index("personal-assistant")

# vectorstore = Pinecone.from_existing_index(index_name="personal-assistant", embedding=embeddings)
# retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# llm = Ollama(model="llama2")

# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="stuff",
#     retriever=retriever,
#     return_source_documents=True
# )

# app = FastAPI()

# class Query(BaseModel):
#     question: str

# @app.post("/ask")
# def ask(q: Query):
#     response = qa_chain(q.question)
#     answer = response["result"]
#     sources = [doc.page_content for doc in response["source_documents"]]
#     return {"answer": answer, "sources": sources}
