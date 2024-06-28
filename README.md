# Auto-Reply AI Chatbot

## Overview
This Python project is an auto-reply chatbot that uses OpenAI's API to analyze chat history and respond automatically. It leverages `pyautogui` for GUI automation and `pyperclip` for clipboard operations. This makes the bot adaptable for various messaging platforms.

## Features
- Automatic message selection and copying
- Analysis of chat history using OpenAI's GPT-3.5 model
- Automated response generation and sending
- Supports multi-language responses (English, Hindi, Bengali and so on)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/tanmoyaiml/auto-reply-ai-chatbot.git
    cd auto-reply-ai-chatbot
    ```

2. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your OpenAI API key:**
    Replace `Your-OpenAI-Key` in `Bot.py` with your actual OpenAI API key.
    ```python
    client = OpenAI(api_key="Your-OpenAI-Key")
    ```

## Usage

1. **Get Cursor Position:**
   Run `getCursor.py` to get the cursor positions required for automation.
    ```bash
    python getCursor.py
    ```
   Note down the cursor positions for the various GUI interactions.

2. **Run the Bot:**
   Execute `Bot.py` to start the auto-reply bot.
    ```bash
    python Bot.py
    ```

## Files

- `getCursor.py`: Script to get cursor positions.
- `getCursor.py` : Script to try the OpenAI response prompt.
- `Bot.py`: Main script to run the auto-reply chatbot.

## Contributing

Feel free to fork this repository and contribute by submitting a pull request. Any enhancements or bug fixes are welcome.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or issues, please open an issue on this repository or contact the repository owner.

