import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'
# return everything that the user inputs.
# pass message into chatgpt api .send() the answer.

@cl.on_message
async def main(message : str):
    response = openai.ChatCompletion.create(
        model = 'gpt-4',
        messages =[
    {"role":"assistant","content": "you are a helpful assistant"},
    {"role":"user","content": message}
    ],
        temperature =1,
    )
    await cl.Message(content=f"{response['choices'][0]['message']['content']}").send()
