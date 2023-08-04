# AI Chatbot using NLTK

This is a simple AI chatbot implemented using the Natural Language Toolkit (NLTK) library in Python. The chatbot can engage in conversations on a variety of topics and respond to user inputs with predefined responses.

## How to Use

1. Clone the repository or download the `chatbot.py` file.

2. Make sure you have Python and the NLTK library installed on your system.

3. Import the necessary modules at the beginning of your Python script:

```python
from nltk.chat.util import Chat, reflections
```

4. Copy the `responses` list from the `chatbot.py` file into your script. It contains pairs of patterns and responses for the chatbot.

5. Create an instance of the chatbot and start the conversation:

```python
chat = Chat(responses, reflections)
chat.converse()
```

6. Run your Python script, and the chatbot will greet you and wait for your input.

## Example Conversations

The chatbot can handle various types of user inputs and provide appropriate responses. Here are some examples of what you can try:

User: "Hello"
Chatbot: "Hey there!"

User: "What is your name?"
Chatbot: "My name is Alex, I am the counterpart of Alexa"

User: "Tell me a joke"
Chatbot: "Why don’t scientists trust atoms? Because they make up everything!"

User: "Who won the World Series in 2022?"
Chatbot: "The World Series in 2022 was won by the Boston Red Sox."

User: "What is the capital of France?"
Chatbot: "The capital of France is Paris."

User: "Do you believe in love?"
Chatbot: "As an AI, I do not have beliefs or emotions, but love is a profound human emotion that brings people together and fosters connections."

User: "Tell me a fun fact"
Chatbot: "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!"

## Extending the Chatbot

You can easily extend the chatbot by adding more pairs to the `responses` list. Each pair consists of a pattern and a list of possible responses. The pattern can be a regular expression that matches user inputs, and the responses will be randomly selected by the chatbot when the pattern matches.

Feel free to add more patterns and responses to make the chatbot even more engaging and interactive!

## Disclaimer

This chatbot is a simple demonstration and may not handle complex conversations or real-time data. It is meant for educational and entertainment purposes only.

---
Note: The code provided in this README assumes that you have the necessary Python environment set up with the NLTK library installed. If you encounter any issues, please refer to the NLTK documentation for installation instructions.
