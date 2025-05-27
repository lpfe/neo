import langchain
from langchain.cache import InMemoryCache
from langchain.llms import OpenAI

llm = OpenAI(
    model = "gpt-3.5-turbo-instruct",
    temperature = 0
)

langchain.llm_cache = InMemoryCache()

print(llm.generate(['하늘의 색깔은?']))
print("-" * 50)
print(llm.generate(['하늘의 색깔은?']))


'''
generations=[[Generation(text='\n\n하늘의 색깔은 파란색입니다.', generation_info={'finish_reason': 'stop', 'logprobs': None})]] llm_output={'token_usage': {'total_tokens': 28, 'completion_tokens': 17, 'prompt_tokens': 11}, 'model_name': 'gpt-3.5-turbo-instruct'}
--------------------------------------------------

두번쨰껀 캐시에 저장된거 불러오는거라 모델명 안나옴
generations=[[Generation(text='\n\n하늘의 색깔은 파란색입니다.', generation_info={'finish_reason': 'stop', 'logprobs': None})]] llm_output={}
'''