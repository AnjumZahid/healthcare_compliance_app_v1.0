import pytest
from state.chat_state import ChatState
from nodes.compliance_nodes import generate_compliance_questions_node, compliance_check_llm

# We will patch the chain.invoke() method to simulate LLM output
class FakeResult:
    def __init__(self, content):
        self.content = content

@pytest.fixture
def fake_chain(monkeypatch):
    def fake_invoke(_self, inputs):
        # Simulate different outputs depending on query
        if "generate questions" in inputs["query"].lower():
            return FakeResult("1. What is the dosage?\n2) Any side effects?\n3. Is it safe for children?")
        elif "compliance" in inputs["query"].lower():
            return FakeResult("This prescription is compliant with WHO guidelines.")
        else:
            return FakeResult("Default response.")
    monkeypatch.setattr("langchain_core.prompts.ChatPromptTemplate.__or__", lambda self, llm: self)
    monkeypatch.setattr("langchain_core.prompts.ChatPromptTemplate.invoke", fake_invoke)
    return fake_invoke


def test_generate_compliance_questions_node(fake_chain):
    state = ChatState(query="Generate questions about Amoxicillin")
    new_state = generate_compliance_questions_node(state)

    assert isinstance(new_state.answer, list)
    assert "What is the dosage?" in new_state.answer
    assert all(q.endswith("?") for q in new_state.answer)


def test_compliance_check_llm(fake_chain):
    state = ChatState(compliance_query="Check compliance for Amoxicillin prescription")
    new_state = compliance_check_llm(state)

    assert isinstance(new_state.compliance_answer, str)
    assert "compliant" in new_state.compliance_answer.lower()
