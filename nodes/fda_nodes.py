from state.chat_state import ChatState
from services.mcp_client import query_fda

async def fda_node(state: ChatState) -> ChatState:
    # take first medicine
    first_medicine = state.medicine_text.split(",")[0].strip()
    state.medicine_query = first_medicine
    # call MCP client
    fda_info = await query_fda(first_medicine)
    state.fda_info = fda_info
    return state