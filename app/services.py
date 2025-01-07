from langchain_openai import ChatOpenAI

chat_client = ChatOpenAI(
    openai_api_base="http://localhost:8000/v1",
    model_name="/root/.cache/llama.cpp/microsoft_Phi-3-mini-4k-instruct-gguf_Phi-3-mini-4k-instruct-q4.gguf"
)
