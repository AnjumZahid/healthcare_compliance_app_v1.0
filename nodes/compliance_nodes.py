from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from state.chat_state import ChatState
import re
from config.settings import DEFAULT_CHAT_MODEL

# --- Node 2: Generate Questions ---
def generate_compliance_questions_node(state: ChatState) -> ChatState:
    """
    Generates compliance-related questions from the input query
    using Gemini LLM.
    """

    # llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    llm = ChatGoogleGenerativeAI(model=DEFAULT_CHAT_MODEL)

    # Define prompt template
    prompt_template1 = ChatPromptTemplate.from_template("{query}")

    # Build chain
    chain = prompt_template1 | llm

    # Run LLM
    result = chain.invoke({"query": state.query})
    raw_text = result.content.strip()

    # Post-process into clean question list
    questions = []
    for line in raw_text.split("\n"):
        line = line.strip()
        if not line:
            continue
        # Remove numbering like "1. " or "2) "
        line = re.sub(r"^\d+[\.\)]\s*", "", line)
        # Keep only proper questions ending with "?"
        if line.endswith("?"):
            questions.append(line)

# Optional
# ✅ Add manual doctor questions (from frontend only)
    if state.manual_questions:
        manual_cleaned = [
            q.strip() if q.strip().endswith("?") else q.strip() + "?"
            for q in state.manual_questions
            if q.strip()
        ]
        questions = manual_cleaned + questions  # prepend manual Qs

    return state.model_copy(update={"answer": questions})


# ==================================================================================================


def compliance_check_llm(state: ChatState) -> ChatState:
    """
    Uses LLM to evaluate compliance with WHO guidelines
    based on the built compliance prompt.
    """
    
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")  # fast & cheap
    # llm = ChatGoogleGenerativeAI(model=DEFAULT_CHAT_MODEL)  # fast & cheap

    prompt_template2 = ChatPromptTemplate.from_template("{query}")

    # Run LLM
    chain = prompt_template2 | llm
    result = chain.invoke({"query": state.compliance_query})

    return state.model_copy(update={"compliance_answer": result.content.strip()})