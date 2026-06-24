from langchain_ollama import ChatOllama

# Configure and set llm to local llm, can be changed later
def get_llm():

    return ChatOllama(
        model="qwen3:8b",
        temperature=0
    )