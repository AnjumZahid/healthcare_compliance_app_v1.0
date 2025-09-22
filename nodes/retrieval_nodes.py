from state.chat_state import ChatState
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
# from config.settings import EMBEDDING_MODEL
import os
from config.settings import DB_DIR

faiss_store_PATH = os.path.join(DB_DIR, "faiss_store")

async def retrieve_chunks_node(state: ChatState) -> ChatState:

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    # embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)
    
    vector_store = FAISS.load_local(faiss_store_PATH, embeddings, allow_dangerous_deserialization=True)

    retrieved_chunks = []
    seen = set()

    for question in state.answer:
        results = await vector_store.asimilarity_search(question, k=2)  #  use async
        for doc in results:
            if doc.page_content not in seen:
                seen.add(doc.page_content)
                retrieved_chunks.append(doc.page_content)

    context = "\n\n".join(retrieved_chunks)
    return state.model_copy(update={"context": context})
