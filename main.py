# MartinGPT
# Simple program to ask chatgpt in terminal
#
# Author: Martin Bravo
# Website: https://mbravo.me
# Github: https://github.com/MartinEBravo

# Import openai and os
import openai
import os

# Import models and functions
from services.models import GPT3, GPT4, models
from services.get_tokens import num_tokens_from_string

# Import dotenv
from dotenv import load_dotenv
load_dotenv()

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# load usage of the bot in the file usage.txt
ubication = os.path.dirname(os.path.abspath(__file__))
usage = float(open(ubication + "/utils/usage.txt", "r").read())

# print robot.txt file
ubication = os.path.dirname(os.path.abspath(__file__))
robot = open(ubication + "/utils/robot.txt", "r").read()
print(robot)

# Initial Model
model = models[0]

# Current Session Cost	
cost = 0

# Initial Message
messages = []
messages.append(
	{"role": "system", "content": "You are a helpful assistant"}
)

while True: 
	message = input("User : ") 

	# If the message is "exit" the program will stop
	if message == "exit":
		break

	# If we want to change the model
	for modelClass in models:
		if message == modelClass.short_name:
			model = modelClass
			print("Model changed to", model.name)
			break
		
	# Answer the message
	else:
			
		# We add the new message
		messages.append( 
			{"role": "user", "content": message}, 
		)

		# We add the cost of the input
		for prompt in messages:
			cost += model.input_per_token * num_tokens_from_string(prompt["content"], model)

		# Request the response
		stream = openai.chat.completions.create(
			model=model.name,
			messages=messages,
			temperature=0.7,
			stream=True
		)

		# Print the response
		print("MartinGPT : ", end="")
		response = ""
		for chunck in stream:
			if chunck.choices[0].delta.content is not None:
				print(chunck.choices[0].delta.content, end="")
		print()

		# We add the response
		messages.append(
			{"role": "system", "content": response},
		)

		# We add the cost of the response
		cost += model.output_per_token * num_tokens_from_string(response, model)

		# Add the cost to the usage
		usage += cost

		# Write the usage in the file
		with open(ubication + "/utils/usage.txt", "w") as file:
			file.write(str(usage))

		# We print the current cost and the total usage
		print("Current cost: $", cost)
		print("Total usage: $", usage)