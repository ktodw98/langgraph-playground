#%% 1. 필요한 라이브러리와 .py 파일의 함수를 가져옵니다.
from IPython.display import Image, display
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from official_docs.basic_chatbot import create_graph  # 우리가 만든 .py 파일에서 함수 임포트

#%% 2. 그래프 생성에 필요한 LLM을 초기화합니다.
#    .py 파일과 동일한 방식으로 설정합니다.
load_dotenv()
llm = init_chat_model("google_genai:gemini-1.5-flash")


#%% 3. 함수를 호출하여 그래프 객체를 가져옵니다.
compiled_graph = create_graph(llm)

#%% 4. 시각화 코드를 실행합니다.
print("LangGraph 전체 구조도:")
display(Image(compiled_graph.get_graph().draw_mermaid_png()))