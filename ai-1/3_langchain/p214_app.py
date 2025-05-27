# # from langchain.llms import OpenAI
# from langchain.chat_models import ChatOpenAI
# from langchain.schema import(
#     SystemMessage,
#     HumanMessage,
#     AIMessage
# )

# chat_llm = ChatOpenAI(
#     model = "gpt-3.5-turbo",
#     temperature = 0.9
# )

# message = [
#     HumanMessage(content = "고양이 울음소리는?"),
# ]
# print("-" * 50)
# result = chat_llm(message)
# print(result.content)

# message_list = [
#     [HumanMessage(content = "고양이 울음소리는?")],
#     [HumanMessage(content = "까마귀 울음소리는?")]
# ]

# print("-" * 50)
# result = chat_llm.generate(message_list)
# print("result 0 : ", result.generations[0][0].text)
# print("result 1 : ", result.generations[1][0].text)
# print("llm output : ", dict(result.llm_output))


## -----------------------------------------------------------------------

# from langchain.chat_models import ChatOpenAI
# from langchain.schema import HumanMessage

# chat_llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.9)

# # 단일 메시지
# message = [HumanMessage(content="고양이 울음소리는?")]
# print("-" * 50)
# result = chat_llm(message)
# print(result.content)

# # 복수 메시지를 반복처리
# message_list = [
#     [HumanMessage(content="고양이 울음소리는?")],
#     [HumanMessage(content="까마귀 울음소리는?")]
# ]

# print("-" * 50)
# for i, msg in enumerate(message_list):
#     response = chat_llm(msg)
#     print(f"result {i} : {response.content}")

## -----------------------------------------------------------------------



from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat_llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.9
)

message = [HumanMessage(content="고양이 울음소리는?")]
print("-" * 50)
result = chat_llm(message)
print(result.content)

message_list = [
    [HumanMessage(content="고양이 울음소리는?")],
    [HumanMessage(content="까마귀 울음소리는?")]
]

print("-" * 50)
results = []
for msg in message_list:
    res = chat_llm(msg)
    results.append(res)

print("result 0 :", results[0].content)
print("result 1 :", results[1].content)
