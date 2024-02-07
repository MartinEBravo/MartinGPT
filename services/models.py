class GPT3:
	def __init__(self):
		self.name = "gpt-3.5-turbo"
		self.input_per_token = 0.0005/1000
		self.output_per_token = 0.002/1000

class GPT4:
	def __init__(self):
		self.name = "gpt-4-0125-preview"
		self.input_per_token = 0.01/1000
		self.output_per_token = 0.03/1000