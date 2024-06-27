from openai import OpenAI
client = OpenAI(api_key = "sk-proj-P6vzasUQ2rwGZUEg2FUYT3BlbkFJ14lNkQVYQtyr2YHZA57g")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": " tell me about you"},
    ]
)
# print('out put is ')
# print(response)
