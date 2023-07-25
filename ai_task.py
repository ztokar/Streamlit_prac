import openai

prompt='write a motto for a football team'

response=openai.Completion.create(
model='text-davinci-003',
prompt=prompt,
temperature=0.8,  #controls how much randomness in answer between 0 and 2
max_tokens=1000  #how many tokens to pay

)