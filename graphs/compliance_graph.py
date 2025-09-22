from langgraph.graph import StateGraph, START, END
from state.chat_state import ChatState
from nodes.history_nodes import extract_history_node
from nodes.image_nodes import extract_image_node
from nodes.prompt_nodes import build_prompt_node, build_compliance_prompt
from nodes.retrieval_nodes import retrieve_chunks_node
from nodes.compliance_nodes import generate_compliance_questions_node, compliance_check_llm
from nodes.fda_nodes import fda_node

# --- Graph definition ---
graph = StateGraph(ChatState)

# --- Add nodes ---
graph.add_node("extract_history", extract_history_node)
graph.add_node("extract_image", extract_image_node)
graph.add_node("build_prompt", build_prompt_node)
graph.add_node("generate_questions", generate_compliance_questions_node)
graph.add_node("retrieve_chunks", retrieve_chunks_node)

# New nodes
graph.add_node("fda_lookup", fda_node)
graph.add_node("build_compliance_prompt", build_compliance_prompt)
graph.add_node("compliance_check_llm", compliance_check_llm)

# --- Define flow ---
graph.add_edge(START, "extract_history")
graph.add_edge("extract_history", "extract_image")
graph.add_edge("extract_image", "build_prompt")
graph.add_edge("build_prompt", "generate_questions")
graph.add_edge("generate_questions", "retrieve_chunks")

# Add compliance checking path
graph.add_edge("retrieve_chunks", "fda_lookup")
graph.add_edge("fda_lookup", "build_compliance_prompt")
graph.add_edge("build_compliance_prompt", "compliance_check_llm")
graph.add_edge("compliance_check_llm", END)

# Compile app
app = graph.compile()
