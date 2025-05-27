from langchain.chains import LLMChain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

## 첫번째 체인
template = """

당신은 극작가 입니다. 연극 제목이 주어졌을 때, 그 줄거리를 작성하는 것이 당신의 업무입니다.
제목 : {title}
시놉시스 : 

"""

prompt = PromptTemplate(
    input_variables = ["title"],
    template = template
)

chain_1 = LLMChain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature = 0
    ),
    prompt = prompt,
)

# print(llm_chain.predict(subject = "고양이", target = "poetry"))

## 두번째 체인

template = """

당신은 연극 평론가입니다. 연극의 시놉시스가 주어졌을 때 그 리뷰를 작성하는 것이 당신의 업무입니다.
시놉시스 : {synopsis}
리뷰 : 

"""

prompt = PromptTemplate(
    input_variables = ["synopsis"],
    template = template
)

chain_2 = LLMChain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature = 0
    ),
    prompt = prompt,
)

# print(chain_1.predict(title = ))
overall_chain = SimpleSequentialChain(
    chains = [chain_1, chain_2],
    verbose = True
)

print(overall_chain.run("서울 랩소디"))