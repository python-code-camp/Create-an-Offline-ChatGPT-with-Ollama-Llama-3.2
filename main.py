# www.youtube.com/@PythonCodeCampOrg

""" Subscribe to PYTHON CODE CAMP or I'll eat all your cookies... """

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.
Here is the conversation history: {history}
Question: {question}
Answer:
"""

model = OllamaLLM(model = "llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    history = ""
    print("Welcome to AI ChatBot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        result = chain.invoke({"history" : history,
                               "question" : user_input})
        print(f"Bot: {result}")
        history += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_conversation()