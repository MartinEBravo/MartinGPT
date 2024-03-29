# Import openai
import openai
import os

# Import the models
from services.get_tokens import num_tokens_from_string
from services.models import models

def execute(cost = 0, model = models[0], messages = [{"role": "system", "content": "You are a helpful assistant"}]):
    
    # load usage of the bot in the file usage.txt
    ubication = os.path.dirname(os.path.abspath(__file__))
    usage = float(open( ubication + "/../utils/usage.txt", "r").read())

    message = input("User : ") 

    # If the message is "exit" the program will stop
    if message == "exit":
        return
    
    # If we want to change the model
    for modelClass in models:
        if message == modelClass.short_name:
            model = modelClass
            print("Model changed to", model.name)
            return execute(cost, model, messages)

    # If we want to know the current cost
    if message == "cost":
        print("Current cost: $", cost)
        print("Total usage: $", usage)
        return execute(cost, model, messages)
    
    # If we want to know the current model
    if message == "model":
        print("Current model:", model.name)
        return execute(cost, model, messages)
    
    # If we want to know the help
    if message == "help":
        print("Type 'cost' to know the current cost")
        print("Type 'exit' to stop the program")
        print("Type 'gpt3' to change the model to GPT-3.5 Turbo")
        print("Type 'gpt4' to change the model to GPT-4.0125 Preview")
        print("Type 'model' to know the current model")
        print("Type 'reset' to reset the cost")
        return execute(cost, model, messages)
    
    # If we want to reset the cost
    if message == "reset":
        print("Cost reseted")
        with open(ubication + "/../utils/usage.txt", "w") as file:
            file.write("0")
        return execute(0, model, messages)
    
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
        with open(ubication + "/../utils/usage.txt", "w") as file:
            file.write(str(usage))
        
        return execute(cost, model, messages)