class GPT3:
	"""
	Represents the GPT-3.5 Turbo model.

	Attributes:
		name (str): The name of the model.
		input_per_token (float): The input cost per token.
		output_per_token (float): The output cost per token.
	"""
	def __init__(self):
		self.name = "gpt-3.5-turbo"
		self.short_name = "gpt3"
		self.input_per_token = 0.0005/1000
		self.output_per_token = 0.002/1000

class GPT4:
	"""
	Represents the GPT-4.0125 Preview model.

	Attributes:
		name (str): The name of the model.
		input_per_token (float): The input cost per token.
		output_per_token (float): The output cost per token.
	"""
	def __init__(self):
		self.name = "gpt-4-0125-preview"
		self.short_name = "gpt4"
		self.input_per_token = 0.01/1000
		self.output_per_token = 0.03/1000

models = [
	GPT4(),
	GPT3(), 
]