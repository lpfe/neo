# 특정 LLM 캐시 비활성화

import langchain
# from langchain.cache import InMemoryCache
from langchain.llms import OpenAI

llm = OpenAI(
    model = "gpt-3.5-turbo-instruct",
    temperature = 0,
)

llm = OpenAI(
    model = "gpt-3.5-turbo-instruct",
    # temperature = 0,
    cache = False
)

print(llm.generate(['오늘 너의 마음을 색깔로 표현해줘']))
print("-" * 50)
print(llm.generate(['오늘 너의 마음을 색깔로 표현해줘']))

