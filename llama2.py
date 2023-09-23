import os

os.environ["REPLICATE_API_TOKEN"] = "r8_ZY40SsHGf8yTLoRcmJMG4AZrUgBEFQ03vQUvr"

import replicate

# Prompts
pre_prompt = "Quiero que respondas en español"


# Generate LLM response
output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',"temperature":0.1, "top_p":0.9, "max_length":128, "repetition_penalty":1) # Model parameters

output

full_response = ""

for item in output:
  full_response += item

print(full_response)