import openai

image = open('cat_sample.png', 'rb')
mask = open('cat_sample_mask.png', 'rb')

response = openai.Image.create_edit(
    # model="gpt-3.5-turbo-instruct",
    image = image,
    mask = mask,
    prompt = 'Many apples in cardboard box',
    n = 1,
    size = "512x512",
    # temperature = 0,
    # max_tokens = 150
)

image_url = response['data'][0]['url']
print(image_url)
