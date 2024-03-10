# import openai
# import re

key = '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'
# openai.api_key = key
# openai.api_key = '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'

# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         return file.read()

# def ask_question(prompt, question):
#     response = openai.ChatCompletion.create(
#         model='gpt-3.5-turbo',
#         messages=[
#             {'role':'system', 'content':'You are a helpful assistant. The first prompt will be a long text,'
#                                         'and any messages that you get be regarding that. Please answer any '
#                                         'questions and requests having in mind the first prompt '},
#             {'role':'user', 'content': prompt},
#             {'role':'user', 'content': question}
#         ]
#     )
#     return response.choices[0].message['content']

# # Read your file's content
# file_content = read_file('FILENAME.txt')

# # Ask a question about the file's content
# question = input('What is your question?: ')
# response = ask_question(file_content, question)
# formatted_response = re.sub(r'(\. )', '.\n', response)

# print(formatted_response)

import os
import openai
openai.api_key = key
openai.File.create(
  file=open("mydata.jsonl", "rb"),
  purpose='fine-tune'
)