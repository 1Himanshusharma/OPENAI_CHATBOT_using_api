import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key = os.getenv('API_KEY')
)
#accesssing the api_key
print(client.api_key)



#golden point this is not optimized chatbot
# means we already know LLM models usually hallucinate that is why we can optimized the bot by......add()
# defining different roles 
def get_completion(prompt, model = "gpt-3.5-turbo"):
  messages = [{"role" : "user", "content": prompt}]
  response = client.chat.completions.create(
    model = model,
    messages = messages,
    temperature = 0,
    max_tokens = 100
  )
  #if we just return response.choices[0] then it will return
  #Choice(finish_reason='stop', index=0, message=ChatCompletionMessage(content='The capital of India is New Delhi.', role='assistant', function_call=None, tool_calls=None), logprobs=None)
  #this whole i just need to print the content section 
  # that is why we usally do this
  return response.choices[0].message.content


#response
print("Enter your text: ")
p = input()
response = get_completion(p)
print("The response: ",response)