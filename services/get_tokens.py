import tiktoken

def num_tokens_from_string(string: str, model: object) -> int:
    encoding = tiktoken.encoding_for_model(model.name)
    return len(encoding.encode(string))