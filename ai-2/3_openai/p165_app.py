import openai
import textwrap

def response_from_ChatAI(user_content, r_num = 1) :

    messages = [
            {"role" : "user", "content" : user_content}
        ]

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 500,
        temperature = 0.8,
        n = r_num
    )

    assistent_replies = []

    for choice in response['choices'] :
        assistent_replies.append(choice['message']['content'])

        return assistent_replies
    
resps = response_from_ChatAI("두 숫자를 입력받아 더하는 파이썬 함수를 만들어줘")

# for resp in resps :
#     shorten_resp = textwrap.shorten(resp, width = 100, placeholder="[...이하 생략...]")
#     print(shorten_resp, end = "\n\n")

print(resps[0])