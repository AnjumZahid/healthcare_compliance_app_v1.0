from pydantic import BaseModel
from typing import List
# import operator

# --- State ---
class ChatState(BaseModel):
    query: str = ""              # prompt text
    answer: List[str] = []       # list of generated questions
    manual_questions: List[str] = []  # ✅ New field for doctor-entered questions
  
    pdf_hist_path: str = ""         # stores uploaded PDF path
    history_text: str = ""

    image_path: str = ""       # store the uploaded image path
    image_text: str = ""
    
    medicine_text: str = ""      # raw string: "drug1, drug2, drug3"
    context: str = ""            # retrieved chunks
   
    compliance_query: str = ""   # constructed compliance prompt
    compliance_answer: str = ""  # final LLM compliance output
    medicine_query: str = ""     # single drug extracted from medicine_text
    fda_info: str = ""           # FDA info fetched from MCP
