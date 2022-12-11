# import the necessary modules and libraries
import openai_secret_manager

assert "chatgpt" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secrets("chatgpt")

print(secrets)

# define the function that will generate an answer from chatGPT
def generate_answer(question):
  # use the chatGPT library to generate an answer to the question
  response = chatGPT.generate(
      engine="text-davinci-002",
      prompt=question,
      max_tokens=1024,
      temperature=0.5,
      frequency_penalty=0,
      presence_penalty=0
  )

  # return the generated answer
  return response

# ask the user for a question
question = input("What is your question? ")

# generate an answer using chatGPT
answer = generate_answer(question)

# print the answer
print("Answer: ", answer)