# return_messages=True 를 지정하면 ChatOpenAI에서 사용하는 채팅 메시지 리스트 형식으로 메모리 변수를 가져올 수 있음

from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(return_messages=True)

memory.chat_memory.add_user_message("배고프다")
memory.chat_memory.add_ai_message("어디 가서 밥 먹을까?")

memory.chat_memory.add_user_message("라면 먹으러 가자")
memory.chat_memory.add_ai_message("지하철역 앞에 있는 분식집으로 가자.")

memory.chat_memory.add_user_message("그럼 출발")
memory.chat_memory.add_ai_message("OK!")

print(memory.load_memory_variables({}))