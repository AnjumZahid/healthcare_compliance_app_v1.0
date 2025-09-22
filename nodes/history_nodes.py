from state.chat_state import ChatState
from services.doc_extractor import extract_from_multiple

# --- Node 0: Extract history from files ---
def extract_history_node(state: ChatState) -> ChatState:
    # Expect file paths in history_text, comma-separated
    files = [f.strip() for f in state.pdf_hist_path.split(",")]
    combined_text = extract_from_multiple(files)
    return state.model_copy(update={"history_text": combined_text})