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
from services.askai import execute

# Import dotenv
from dotenv import load_dotenv
load_dotenv()

# Set the API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Print the robot.txt file
ubication = os.path.dirname(os.path.abspath(__file__))
print(open(ubication + "/utils/robot.txt", "r").read())

# Execute the program
execute()