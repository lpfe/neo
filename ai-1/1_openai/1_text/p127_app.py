import openai

prompt = '''
# "Hello World!' 표시
def helloworld() : 
'''

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt = prompt,
    temperature = 0,
    # max_tokens = 150
)

print(response.choices[0].text)
