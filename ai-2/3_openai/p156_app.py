import openai
import os

# 원래 적어줘야하는데 .bashrc에 적어두면 이거 안해도 OPENAI_API_KEY 감지한다?
openai.api_key = os.environ["OPENAI_API_KEY"]

models = openai.Model.list()

print(models["data"][0]["id"])