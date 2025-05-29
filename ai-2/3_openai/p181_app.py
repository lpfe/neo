# import openai
# from IPython.display import Image, display

# org_img_file = "./data/fish.png"
# mask_img_file = "./data/fish_mask.png"

# response = openai.Image.create_edit(
#     image = open(org_img_file, 'rb'),
#     mask = open(mask_img_file, 'rb'),
#     prompt = "Happy robots swimming in the water",
#     n = 1,
#     size = "512x512"
# )

# image_url = response['data'][0]['url']
# print(image_url)
# display(Image(url=image_url))
# print("-" * 50)



import openai
import requests

org_img_file = "./data/fish.png"
mask_img_file = "./data/fish_mask.png"

with open(org_img_file, "rb") as image, open(mask_img_file, "rb") as mask:
    response = requests.post(
        "https://api.openai.com/v1/images/edits",
        # headers={
        #     "Authorization": f"Bearer {openai.api_key}"
        # },
        files={
            "image": ("fish.png", image, "image/png"),
            "mask": ("fish_mask.png", mask, "image/png")
        },
        data={
            "prompt": "Happy robots swimming in the water",
            "n": 1,
            "size": "512x512"
        }
    )

result = response.json()
print(result["data"][0]["url"])
