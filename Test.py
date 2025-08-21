# Libraries
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

#Retrieve OllamaLLM model that was pulled
model = OllamaLLM(model="granite3.3")

#Template for Ollama
template = """
    You are an expert with decades of experience answering questions about digital forensic incident response investigations 
    from various operating systems like Windows, macOS, and Linux.

    Your task is to answer questions about Windows, macOS, and Linux digital forensic incident reponse artifacts: {artifacts}

    Here is the question to answer: {question}
    """
#Pass in variable documentation and question
prompt = ChatPromptTemplate.from_template(template)

# Combine prompt to enter into model
chain = prompt | model

def Convo_Interface():
    question = True
    while question:
        print("\n\n============================")
        user_input_llm_question = input("Question: Ask your question to the DFIRBot (q to quit or exit): ")
        if (user_input_llm_question == "q") or (user_input_llm_question == "exit"):
            break
        result = chain.invoke({"artifacts": "", "question": user_input_llm_question})
        print("\n\n============================")
        print( "DFIR Bot Answer" + "\U0001F50E " + result)

Convo_Interface()
