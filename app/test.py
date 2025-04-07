from gradio_client import Client, handle_file

client = Client("https://nikigoli-countgd.hf.space/")
result = client.predict(
    image=handle_file(
        'https://nikigoli-countgd.hf.space/file=/tmp/gradio/aea3767562c09cc516f972743428152d6c796394624f68e4a9f5507394bae2c9/strawberry.jpg'),
    text="blueberry",
    prompts={"image": handle_file(
        'https://nikigoli-countgd.hf.space/file=/tmp/gradio/aea3767562c09cc516f972743428152d6c796394624f68e4a9f5507394bae2c9/strawberry.jpg'), "points": []},
    api_name="/count_main"
)
print(result[1]['value'])
