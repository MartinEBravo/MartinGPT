import tiktoken

def num_tokens_from_string(string: str, model: object) -> int:
    """
    Calculates the number of tokens in a given string using the specified model.

    Args:
        string (str): The input string.
        model (object): The model object.

    Returns:
        int: The number of tokens in the string.
    """
    encoding = tiktoken.encoding_for_model(model.name)
    return len(encoding.encode(string))