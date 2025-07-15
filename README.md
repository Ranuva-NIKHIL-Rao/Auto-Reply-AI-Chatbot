# AUTO-REPLY AI CHATBOT

## DESCRIPTION

This project automates the process of interacting with a chat application, specifically designed to analyze chat history and generate humorous responses using OpenAI's gpt-4o-mini model. The virtual assistant, named Nikhil, is a character that roasts people in a funny way, based on the chat history.

## FEATURES

1. **Automated Chat Interaction**

   - Uses pyautogui to perform mouse and keyboard operations, interacting with the chat application without manual intervention.

2. **Chat History Analysis**

   - Copies chat history from the chat application and analyzes it to determine if the last message was sent by a specific user (e.g., "Rohan Das").

3. **Humorous Response Generation**

   - Integrates with OpenAI's GPT-4o-mini model to generate funny, roast-style responses based on the analyzed chat history.

4. **Clipboard Operations**

   - Utilizes pyperclip to copy and paste text, facilitating the retrieval and insertion of chat messages.

5. **Automated Chat Interaction**

   - Uses pyautogui to perform mouse and keyboard operations, interacting with the chat application without manual intervention.

6. **Chat History Analysis**

   - Copies chat history from the chat application and analyzes it to determine if the last message was sent by a specific user (e.g., "Rohan Das").

7. **Humorous Response Generation**
   - Integrates with OpenAI's gpt-4o-mini model to generate funny, roast-style responses based on the analyzed chat history.

## WORKFLOW

1. **Initialization and Setup**

   - Click on the Chrome icon to open the chat application.
   - Wait for a brief period to ensure the application is open and ready for interaction.

2. **Chat History Retrieval**

   - Periodically select and copy chat history by dragging the mouse over the chat area and using the copy shortcut.
   - Retrieve the copied text from the clipboard.

3. **Message Analysis**

   - Analyze the copied chat history to check if the last message is from a specific user (e.g., "Rohan Das").
   - If the last message is from the target user, send the chat history to OpenAI's GPT-4o-mini to generate a humorous response.

4. **Send Response**

   - Click on the chat input area and paste the generated response.
   - Press 'Enter' to send the response.

5. **Repeat**
   - Wait for a brief period to ensure the application is open and ready for interaction.
   - Chat History Retrieval
   - Periodically select and copy chat history by dragging the mouse over the chat area and using the copy shortcut.
   - Retrieve the copied text from the clipboard.
   - Message Analysis
   - Analyze the copied chat history to check if the last message is from a specific user (e.g., "Rohan Das").
   - Generate Response
   - Copy the generated response to the clipboard.
   - Send Response

## LIBRARIES USED

1. **pyautogui**: For automating mouse and keyboard interactions.
2. **time**: For adding delays between operations.
3. **pyperclip**: For clipboard operations.
4. **openai**: For interacting with OpenAI's GPT-4o-mini model.
5. **os**: For environment variable management.
6. **re**: For regular expression operations.
7. **dotenv**: For loading environment variables from a `.env` file.

## SETUP

1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file and add your API keys.
4. Run the `bot.py` script to start the chatbot.

## USAGE

1. Ensure the chat application is open and ready for interaction.
2. Run the `bot.py` script.
3. The bot will automatically interact with the chat application, analyze chat history, and generate humorous responses.
