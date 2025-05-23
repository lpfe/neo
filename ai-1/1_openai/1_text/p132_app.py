import openai

messages = [
    {"role" : "system", "content" : "오타를 수정해줘."},
    {"role" : "user", "content" : "오늘은 정말로 즐거워따."},
]

response = openai.ChatCompletion.create(
model = 'gpt-3.5-turbo-instruct',
prompt = prefix_prompt,
suffix = suffix_prompt,
temperature = 0.7,
max_tokens = 200
)

print(response.choices[0].text)