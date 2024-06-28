import pyautogui
import pyperclip
import time
from openai import OpenAI
import time

 # pip install openai
    # if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key="Your-OpenAI-Key")



# Important Condition for loop
def is_last_message_from_sender(chat_log, sender_name="Ankur"):
    # Split the chat log into individual messages 
    messages = chat_log.strip().split("/2024] ")[-1]
    
    # Iterate through the messages in reverse to find the last message
    if sender_name in messages:
        return True
    return False


# Step 1: Click on the icon at coordinates (1295, 1050)
pyautogui.click(1295, 1050)
time.sleep(1)  # wait for 1 second to ensure the click action is completed

while True:
    # Step 2: Drag from (670, 252) to (1300, 910)
    pyautogui.moveTo(670, 252)
    pyautogui.dragTo(1300, 910, duration=1, button='left')

    # Step 3: Press Ctrl+C to copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)  # wait for 1 second to ensure the copy action is completed
    pyautogui.click(1300, 910)

    # Step 4: Get the copied text from the clipboard
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Tanmoy who speaks english as well as hindi as well as bengali. You are from India and you are a coder. You analyse chat history and response like Tanmoy. Output should be the next chat response (text message only)"},
            {"role": "user", "content": chat_history}
        ]
        )

        response=completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click on the message bar at (818,959)
        pyautogui.click(818,959)
        time.sleep(1)

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # wait for 1 second to ensure the copy action is completed

        # Step 7: Press Enter to send the reply
        pyautogui.press('enter')