import openai

prompt = '''한국어를 영어로 번역해줘.
    한국어 : 저것은 귀여운 고양이이다.
    영어 : 
'''

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt = prompt,
    temperature = 0,
    # max_tokens = 150
)

print(response.choices[0].text)
# print(response)