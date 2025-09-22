# --- Node 1: Build Prompt ---
from state.chat_state import ChatState

def build_prompt_node(state: ChatState) -> ChatState:
    # if not (state.history_text and state.image_text and state.medicine_text):
    #     return state  # wait until all inputs are ready
    
    query_text = f"""
    You are a medical compliance assistant.
    Your task is to support doctors by checking prescribed medicines against WHO rules and guidelines.

    Context Provided

    Patient history: {state.history_text}.
    Medical image analysis results: {state.image_text}.
    Doctor’s prescribed medicines: {state.medicine_text}.
    
    Your Role

    For each prescribed medicine, generate 3 precise and distinct questions that should be asked to verify compliance with WHO rules and medical best practices.

    Guidelines

    Questions must be clear, specific, and relevant to the medicine and patient case.

    Focus on WHO guidelines for dosage, contraindications, interactions, and suitability for the patient’s condition.

    Do not answer the questions yourself — only generate them.

    Output Instructions

    Generate a single numbered list of all compliance-checking questions.

    Each question must explicitly mention the medicine name within the question text.

    Do not separate medicines as headings.

    If 3 medicines are prescribed, there should be 9 listed questions in total, 3 for each.

    Return plain text only, without any special characters around words.
        """
    
       # 👇 print prompt for debugging/inspection
    # print("\n===== PROMPT CONTEXT SENT TO MODEL =====\n")
    # print(query_text)
    # print("\n========================================\n")

    # return ChatState(query=query_text, answer=state.answer)
    return state.model_copy(update={"query": query_text})


# =================================================================================


def build_compliance_prompt(state: ChatState) -> ChatState:
    """
    Builds a structured compliance query for the LLM using
    history, image, medicine text, and WHO context.
    """
    prompt = f"""
    You are a WHO compliance checker.

    Context from WHO standards:
    {state.context}

    Context from openFDA API End Points:
    {state.fda_info}

    Patient history:
    {state.history_text}

    Image findings:
    {state.image_text}

    Doctor’s prescribed medicine(s):
    {state.medicine_text}

    Task:
    Check whether the suggested medicine is compliant with WHO treatment guidelines.
    Give a concise doctor-facing response with:
    - Compliance status (Yes/No)
    - Justification (short, clear)
    """

    return state.model_copy(update={"compliance_query": prompt.strip()})


