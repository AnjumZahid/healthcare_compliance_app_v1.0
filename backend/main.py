# backend/main.py
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"   # suppress TF INFO & WARNING logs
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"  # disable oneDNN custom ops (optional)

from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import asyncio, os, shutil, threading, json
from contextlib import asynccontextmanager

from graphs.compliance_graph import app as graph_app
from state.chat_state import ChatState
from services.start_server import start_fda_server
from config.settings import PDF_DIR, BASE_DIR, IMAGE_DIR


# --- Lifespan Event Handler ---
@asynccontextmanager
async def lifespan(_app: FastAPI):
    print("🚀 Starting FDA MCP server...")
    thread = threading.Thread(target=start_fda_server, daemon=True)
    thread.start()
    print("✅ FDA MCP server started in background.")
    yield
    print("🛑 Shutting down backend...")


# --- FastAPI App ---
app = FastAPI(lifespan=lifespan)

# ✅ Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- API Endpoint ---
@app.post("/process/")
async def process_data(
    file: UploadFile,
    image: UploadFile,
    medicine_text: str = Form(...),
    manual_questions: str = Form("[]"),  # ✅ new field
):
    # --- Save uploaded PDF ---
    os.makedirs(PDF_DIR, exist_ok=True)
    pdf_path = os.path.join(PDF_DIR, file.filename)
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # --- Save uploaded image in uploads/images ---
    # UPLOADS_DIR = os.path.join(BASE_DIR, "uploads", "images")
    os.makedirs(IMAGE_DIR, exist_ok=True)
    img_path = os.path.join(IMAGE_DIR, image.filename)
    # os.makedirs(UPLOADS_DIR, exist_ok=True)

    # img_path = os.path.join(UPLOADS_DIR, image.filename)
    with open(img_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # ✅ Parse manual doctor questions from JSON
    try:
        manual_qs_list = json.loads(manual_questions)
    except Exception:
        manual_qs_list = []

    # --- Build initial state ---
    initial_state = ChatState(
        pdf_hist_path=pdf_path,
        image_path=img_path,
        medicine_text=medicine_text,
        manual_questions=manual_qs_list,   # ✅ store in state
    )

    # --- Run LangGraph pipeline ---
    result = await graph_app.ainvoke(initial_state)

    return {
        "questions": result.get("answer", []),
        "context": result.get("context", ""),
        "image_text": result.get("image_text", ""),
        "compliance_query": result.get("compliance_query", ""),
        "compliance_answer": result.get("compliance_answer", ""),
    }
