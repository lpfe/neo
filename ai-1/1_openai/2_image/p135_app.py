import openai

prompt = '''
Cat dancing on the car
'''

response = openai.Image.create(
    # model="gpt-3.5-turbo-instruct",
    prompt = prompt,
    n = 1,
    size = "512x512",
    # temperature = 0,
    # max_tokens = 150
)

image_url = response['data'][0]['url']
print(image_url)
