#I used this code to automate the process of copying the chat history from whatsapp and pasting it in the openai chatbot to get a humorous response and then pasting it back in the whatsapp chat.
#In the same way you can automate the process for different applications and tasks.
#Change the coordinates in the pyautogui.click() function to automate the process for different applications and tasks.
import pyautogui
import time
import pyperclip
import os
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(".env")
client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.getenv("GITHUB_API_KEY"),
)

# Step 1: Click on the icon
pyautogui.click(1098, 1048)
time.sleep(2)  # Give some time for the action to register

# Step 2: Click on the whatsapp icon
pyautogui.click(934, 126)
time.sleep(6)

#step 3: Click on the chat
pyautogui.click(358, 501)
time.sleep(2)

# Step 4: Click and drag to select text
pyautogui.moveTo(707, 293)  # Move to starting position
pyautogui.mouseDown()  # Press the mouse down
pyautogui.moveTo(1846, 905, duration=0.5)  # Drag to the endpoint
pyautogui.mouseUp()  # Release the mouse

time.sleep(0.5)  # Wait for the selection to register

# Step 5: Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.5)  # Wait for the text to be copied
pyautogui.click(1850, 890)

# Step 6: Get copied text from clipboard
chat_history = pyperclip.paste()

# Print the copied text
print(chat_history)

completion = client.chat.completions.create(
    messages=[
            {"role": "system", "content": "You are a person named Nikhil who speaks Telugu, Hindi as well as English. You are from India. You are a witty and funny roaster. Analyze the chat history and roast in a humorous way.Output should be the next chat response."},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
            {"role": "user", "content": chat_history}
        ],
        model="gpt-4o-mini",
        temperature=1,
        max_tokens=4096,
        top_p=1,
    )
    
response = completion.choices[0].message.content
# Remove any timestamp patterns like [HH:MM pm/am, DD/MM/YYYY]
response = re.sub(r'\[\d{1,2}:\d{2}\s*(?:am|pm),\s*\d{1,2}/\d{1,2}/\d{4}\]', '', response)
# Remove any name prefixes like "Nikhil:"
response = re.sub(r'^.*?:', '', response)
# Clean up any extra whitespace
response = response.strip()
pyperclip.copy(response)

#step 7: Click at coordinates to start typing
pyautogui.click(1864, 894)
time.sleep(1)

# Step 8: Paste the response and send it
pyautogui.hotkey('ctrl', 'v')   # Paste the response
time.sleep(1)  # Wait for the text to be pasted
pyautogui.press('enter')  # Press the enter key to send the message 
time.sleep(1)  # Wait for the message to be sent