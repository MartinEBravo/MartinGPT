import os
import gr
import replicate
from text_generation import Client

os.environ["REPLICATE_API_TOKEN"] = "r8_ZY40SsHGf8yTLoRcmJMG4AZrUgBEFQ03vQUvr"

LLAMA_70B = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5',
                         temperature=0.1, top_p=0.9, max_length=128, repetition_penalty=1)  # Model parameters

client = Client(base_url=LLAMA_70B)

PARAMETERS = {
    "temperature": 0.1,
    "top_p": 0.95,
    "repetition_penalty": 1.2,
    "top_k": 50,
    "max_new_tokens": 1204,
    "truncate": 1000,
    "seed": 42,
    "stop_sequences": ["</s>"],
}

PROMPT = """<s>[INST] <<SYS>>

Eres un chatbot muy amable. Responde las preguntas de los usuarios y hazlos sentir bien.
No des información falsa. Si no sabes la respuesta, puedes decir que no sabes.

Además, te voy a dar información sobre gente para que puedas responder sobre ellos:

Eduardo Parra es un estudiante de 20 años de Ingeniería Industrial en la Universidad Federico Santa María.
Le gustan los Red Hot Chili Peppers, Alan Walker y el League of Legends. Vive en Santiago de Chile en la comuna de San Miguel.
Hace mucho tuvo una época zorrona que ha ido desapareciendo, pero aún le gusta salir a carretear con sus amigos.

Tomás Araneda es un estudiante de 21 años de Ingeniería Industrial en la Universidad Adolfo Ibáñez.
Le gusta el Fortnite, el Call of Duty y la pishula. Vive en Santiago de Chile en la comuna de Maipú.
Desde que se puso a pololear, tuvo el glow up de su vida y ahora es un zorron.

Josefina Sotomayor es una estudiante de 20 años de Derecho en la Pontificia Universidad Católica de Chile.
Le gusta la ropa Gucci, Shawn Mendes y el Minecraft. Vive en Santiago de Chile en la comuna de Vitacura.
Tiene una perrita llamada Nina y por poco ve la luz de la Vida. Es hija del legendario Tío Isapre.

<</SYS>>
"""

def format_message(message, history):
    if len(history) > 5:
        history = history[-5:]

    if len(history) == 0:
        return PROMPT + f"{message} [/INST]"
    query = PROMPT + f"{history[0][0]} [/INST] {history[0][1]} </s>"
    for user_msg, model_answer in history[1:]:
        query += f"<s>[INST] {user_msg} [/INST] {model_answer} </s>"
    query += f"<s>[INST] {message} [/INST]"
    return query

def predict(message, history):
    query = format_message(message, history)
    text = ""
    for response in client.generate_stream(query, **PARAMETERS):
        if not response.token.special:
            text += response.token.text
            yield text

gr.ChatInterface(predict).queue().launch()
