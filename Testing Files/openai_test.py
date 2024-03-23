import openai
#from openai import OpenAI
#client = OpenAI()

#client = openai.OpenAIAPI()

openai.api_key = "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"

response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write an email to my boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)


"""from openai import OpenAI
client = OpenAI()

response = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt="Write a tagline for an ice cream workshop.\n\n\nWrite a tagline for an ice cream workshop.\n\n\n\"Indulge in creativity, one scoop at a time.\"",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)"""