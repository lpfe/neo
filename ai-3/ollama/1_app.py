# Ollama.chat() 사용

import ollama

response = ollama.chat(
    model = 'llama3.2:1b',
    messages = [
        {"role" : "system", "content" : "You are a python expert."},
        {"role" : "user", "content" : "Code a Python function to generate a Fibonacci sequence."},
    ]
)

print(response['message']['content'])