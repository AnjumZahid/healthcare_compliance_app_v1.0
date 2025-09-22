# 🏥 Healthcare Compliance App v1.0  

**MVP Prototype** for healthcare compliance checking.  
Uses **MCP protocol** for querying **remote data sources (FDA / WHO APIs)**, and a **local RAG pipeline** for internal compliance knowledge.  

---

## ⚙️ Tech Stack  

- **LangGraph** – Workflow orchestration  
- **LangChain (optional)** – Utilities for chaining  
- **MCP (Model Context Protocol)** – Remote API querying (FDA / WHO)  
- **RAG (Retrieval-Augmented Generation)** – Local compliance document QA  
- **FastAPI** – Backend API services  
- **Streamlit** – Frontend interface  
- **FAISS** – Local Database for compliance storage  
- **Python 3.10+** – Core programming language  
- **Pytest** – Unit testing  

---

## 📌 Features (MVP)
- Upload & process patient history / prescriptions  
- Extract medicines from files (PDF, text, images)  
- **Query FDA/WHO APIs** via MCP  
- **Local RAG pipeline** for knowledge-based compliance checks  
- AI-powered compliance reports  
- Interactive Streamlit dashboard  

---

## 📂 Project Structure


---

## Project Structure
healthcare_compliance_app_v1.0/
│── backend/ # FastAPI backend (handles processing & LangGraph pipeline)
│── frontend/ # Streamlit UI for doctors
│── graphs/ # LangGraph pipeline definition
│── nodes/ # Modular processing nodes (history, image, FDA, compliance, etc.)
│── services/ # Supporting services (MCP server, vectorstore, extractors, etc.)
│── state/ # Shared state definition across LangGraph
│── config/ # Configuration (paths, environment settings)
│── data/ # Models, PDFs, and sample data
│── database/ # Vector store (FAISS index)
│── tests/ # Unit tests
│── test_data/ # Sample test files (images, PDFs)
│── requirements.txt # Dependencies
│── .gitignore # Ignored files and environments

markdown
Copy code

---

## ⚙️ Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/) (interactive UI for doctors)
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (REST API with CORS support)
- **AI Workflow:** [LangGraph](https://github.com/langchain-ai/langgraph) (stateful AI pipeline)
- **Data Retrieval:** RAG with FAISS Vectorstore
- **Compliance Standards:** FDA MCP Server + WHO guidelines
- **ML Models:** TensorFlow/Keras (image classification)

---

##  How It Works
1. Doctor uploads:
   - 📑 Patient history (PDF)
   - 🩻 Diagnostic scan (image)
   - 💊 Prescribed medicines
   - ❓ Optional custom compliance questions
2. System runs an AI-powered compliance workflow:
   - Extracts text from PDF and images
   - Generates compliance-related questions
   - Retrieves relevant medical context
   - Queries FDA / WHO data sources
   - Produces a **final compliance report**
3. Doctor reviews:
   - Generated questions
   - Retrieved context
   - Image findings
   - Final compliance recommendation ✅

---

## ▶️ Running the App

### 1. Clone Repo
```bash
git clone https://github.com/AnjumZahid/healthcare_compliance_app_v1.0.git
cd healthcare_compliance_app_v1.0
