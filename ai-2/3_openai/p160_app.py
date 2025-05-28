import openai

messages = [
    {"role" : "user", "content" : "대한민국의 수도는 어디인가요?"}
    # {"role" : "user", "content" : "대한민국의 제2의 도시는 어디인가요?"}
]

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages,
    max_tokens = 100,
    temperature = 0.7,
    n = 1
    # n = 3
)

print("-" * 50)
print(response['choices'][0]['message']['content'])
# print(response['choices'][1]['message']['content'])
# print(response['choices'][2]['message']['content'])