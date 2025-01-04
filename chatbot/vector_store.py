from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

loader = TextLoader("data/documents.txt")
docs = loader.load()

embedding = OpenAIEmbeddings(model="text-embedding-ada-002")

vectorstore = FAISS.from_documents(docs, embedding)

vectorstore.save_local("db_vector_store")
