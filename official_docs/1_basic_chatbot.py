from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

from IPython.display import Image, display


# 환경변수 설정
load_dotenv()

model = "google"

if model == "google":
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    llm = init_chat_model("google_genai:gemini-2.0-flash", google_api_key=GOOGLE_API_KEY)
elif model == "openai":
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    llm = init_chat_model("openai:gpt-4.1", openai_api_key=OPENAI_API_KEY)

# State 클래스 정의
class State(TypedDict):
    messages: Annotated[list, add_messages]


# 챗봇 노드 정의
def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}


def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


# 그래프 빌더 생성
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# 그래프 컴파일
graph = graph_builder.compile()


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break

# 그래프 시각화
try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
