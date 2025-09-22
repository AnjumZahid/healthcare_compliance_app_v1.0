from state.chat_state import ChatState
from data.models.image_classifier import classify_xray

def extract_image_node(state: ChatState) -> ChatState:
    if state.image_path:  # use the uploaded path
        image_result = classify_xray(state.image_path)
        return state.model_copy(update={"image_text": image_result})
    return state
