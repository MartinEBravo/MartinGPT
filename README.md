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

First, clone this repository:

```bash
git clone https://github.com/MartinEBravo/MartinGPT.git
```

Then, install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file with your OpenAI API key:

```bash
touch .env
OPENAI_API_KEY=your-api-key > .env
```

Replace `your-api-key` with your OpenAI API key.

### Add command to your terminal

If you want to use the chatbot from your terminal, you can add the following command to your `.bashrc` or `.zshrc` file:

### Windows
```bash
alias martingpt='python /MartinGPT/main.py'
source ~/.bashrc
```

### Linux
```bash
alias martingpt='python3 /MartinGPT/main.py'
source ~/.bashrc
```

### MacOS
```bash
alias martingpt='python3 /MartinGPT/main.py'
source ~/.zshrc
```

Now you can use the chatbot from your terminal by typing `martingpt`.

## Commands

- `exit`: Exit the chatbot
- `gpt3`: Change the model to GPT-3
- `gpt4`: Change the model to GPT-4