from llama_index import download_loader, GPTVectorStoreIndex, ServiceContext, LLMPredictor, LangchainEmbedding, Document
# from llama_index.readers import BeautifulSoupReader
from llama_index.readers.web import BeautifulSoupWebReader

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import HuggingFaceEmbeddings

# loader = BeautifulSoupReader
loader = BeautifulSoupWebReader()


# documents = loader.load_data("https://openai.com/index/planning-for-agi-and-beyond/")
documents = loader.load_data(urls=["https://openai.com/index/planning-for-agi-and-beyond/"])

print("-" * 50)
print("Documnets loaded successfully")
print(f'Loaded documents : {documents}')

documnets_objects = [Document(text = doc.text) for doc in documents]

embed_model = LangchainEmbedding(HuggingFaceEmbeddings(
    model_name = "all-MiniLM-L6-v2"
))
print("Embedding Model initialized successfully")

llm_predictor = LLMPredictor(llm = ChatOpenAI(
    temperature = 0,
    model_name = "gpt-3.5-turbo"
))
print("-" * 50)
print("LLM Predictor initialized successfully")

service_context = ServiceContext.from_defaults(
    llm_predictor=llm_predictor,
    embed_model=embed_model
)
print('-' * 50)
print("Service context initialized successfully")

index = GPTVectorStoreIndex.from_documents(
    documnets_objects,
    service_context = service_context
)
print("-" * 50)
print("Index initialized successfully")

query_engine = index.as_query_engine()
print("-" * 50)
print("Query engine created successfully")

print("-" * 50)
query = "이 웹페이지에서 전하고 싶은 말은 무엇인가요? 한국어도 대답해주세요."
response = query_engine.query(query)
print(f'Query : {query}', end = '\n\n')
print(f'Response : {response}')
print("-" * 50)