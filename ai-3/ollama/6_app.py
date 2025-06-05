from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

model = OllamaLLM(model= "llama3.2:latest")

template = """
You are an English vocalbulary tutor.
When given a word, explain its meaning in simple terms, and provide an example sentence.
If the word has multiple meanings, explain each with examples.

Here's the input :

Word : {word}

Output format :
1. Definition : [Brief explanation is simple English]
2. Example Sentence : [A sentence using the word in context]
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def get_definition(word) :
    return chain.invoke({"word" : word})

if __name__ == '__main__' :
    while True :
        word = input("Enter word : ")
        if word == '/bye' :
            break
        print(get_definition(word))
        print()