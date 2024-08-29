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

class GPT4o:
	"""
	Represents the GPT-4o

	Attributes:
		name (str): The name of the model.
		input_per_token (float): The input cost per token.
		output_per_token (float): The output cost per token.
	"""
	def __init__(self):
		self.name = "gpt-4o"
		self.short_name = "gpt4o"
		self.input_per_token = 5/1000000
		self.output_per_token = 15/1000000


class GPT4oMini:
	"""
	Represents the GPT-4o Mini

	Attributes:
		name (str): The name of the model.
		input_per_token (float): The input cost per token.
		output_per_token (float): The output cost per token.
	"""
	def __init__(self):
		self.name = "gpt-4o-mini"
		self.short_name = "gpt4omini"
		self.input_per_token = 0.15/1000000
		self.output_per_token = 0.6/1000000



models = [
	GPT4oMini(),
	GPT4o(),
	GPT4(),
	GPT3(), 
]