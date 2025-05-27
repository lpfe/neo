from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI

with open("akazukin_all.txt") as f:
    text_all = f.read()

text_spliter = CharacterTextSplitter(
    separator = "\n\n",  ## new line 연속 두 개
    chunk_size = 300,
    chunk_overlap = 20
)

texts = text_spliter.split_text(text_all)

print("-" * 50)
print(len(texts))

for text in texts : 
    print(text[:10], ":", len(text))

docs = [Document(page_content = text) for text in texts]

chain = load_summarize_chain(
    llm = OpenAI(
        model = "gpt-3.5-turbo-instruct",
        temperature = 0
    ),
    chain_type = "map_reduce",
)

print("-" * 50)
print(chain.run(docs))