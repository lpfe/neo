from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import OpenAI

prompt = PromptTemplate(
    input_variables = ["product"],
    template = "{product}을 만드는 새로운 회사 이름을 하나 제안해줘"
)

chain = LLMChain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature = 0.9
    ),
    prompt = prompt
)

# print(prompt.format(product = "컴퓨터 게임"))
# print("-" * 50)
# print(chain.run("컴퓨터 게임"))

product = "컴퓨터게임"
print(prompt.format(product = product))
print(chain.run(product))