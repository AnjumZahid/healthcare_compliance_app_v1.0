from pydantic import BaseModel
from typing import List
# import operator

# --- State ---
class ChatState(BaseModel):
    query: str = ""              # prompt text
    # query: Annotated[List[str], operator.add] = []  # allows multiple queries


    answer: List[str] = []       # list of generated questions
    # answer: Annotated[list[str], operator.add] = []
   
    pdf_hist_path: str = ""         # stores uploaded PDF path
    # pdf_hist_path: Annotated[list[str], operator.add] = []
    history_text: str = ""
    # history_text: Annotated[list[str], operator.add] = []

    image_path: str = ""       # store the uploaded image path
    # image_path: Annotated[list[str], operator.add] = []
    image_text: str = ""
    # image_text: Annotated[list[str], operator.add] = []
    
    medicine_text: str = ""      # raw string: "drug1, drug2, drug3"
    # medicine_text: Annotated[list[str], operator.add] = []
    
    context: str = ""            # retrieved chunks
    # context: Annotated[list[str], operator.add] = []
    
    compliance_query: str = ""   # constructed compliance prompt
    # compliance_query: Annotated[list[str], operator.add] = []
    compliance_answer: str = ""  # final LLM compliance output
    # compliance_answer: Annotated[list[str], operator.add] = []

    medicine_query: str = ""     # single drug extracted from medicine_text
    # medicine_query: Annotated[list[str], operator.add] = []
    fda_info: str = ""           # FDA info fetched from MCP
    # fda_info: Annotated[list[str], operator.add] = []