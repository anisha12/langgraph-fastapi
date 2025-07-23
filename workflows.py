from langgraph.graph import StateGraph
from langchain_openai import ChatOpenAI
from typing import TypedDict


# Define the state schema
class GraphState(TypedDict):
    messages: list[str]


# Initialize the OpenAI LLM
llm = ChatOpenAI(
    model="gpt-4o",  # or "gpt-3.5-turbo"
    openai_api_key="" # replace with your API key
)


# Define a node for summarization
def summarize_text(state: GraphState) -> GraphState:
    user_message = state["messages"][-1]
    response = llm.invoke(f"Summarize: {user_message}")
    state["messages"].append(response.content)
    return state


# Create a graph
graph = StateGraph(state_schema=GraphState)
graph.add_node("summarizer", summarize_text)
graph.set_entry_point("summarizer")


# Compile the graph
graph_app = graph.compile()


