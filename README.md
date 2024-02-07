# MartinGPT

```
       _______            _______________________
     _/       \_         /                       \
    / |       | \       |  Welcome to MartinGPT. |
   /  |__   __|  \      |  Ask me anything!      |
  |__/((o| |o))\__|    /_________________________/
  |      | |      |        
  |\     |_|     /|     
  | \           / |
   \| /  ___  \ |/
    \ | / _ \ | /
     \_________/
      _|_____|_
 ____|_________|____
/                   \
```

## Description

This is a simple chatbot implementation to use ChatGPT in your terminal.

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file with the following content:

```bash
OPENAI_API_KEY=your-api-key
```

### Add command to your terminal

If you want to use the chatbot from your terminal, you can add the following command to your `.bashrc` or `.zshrc` file:

```bash
function chatgpt() {
    python /path/to/MartinGPT/main.py
}
```

Replace `/path/to/MartinGPT` with the path to the folder where you cloned this repository.

## Commands

- `exit`: Exit the chatbot
- `gpt3`: Change the model to GPT-3
- `gpt4`: Change the model to GPT-4