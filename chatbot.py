from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hello! %1']],
    ['(hi|hello|hey|holla|hola)', ['Hey there!', 'Hi there!', 'Hey!']],
    ['(.*) your name ?', ['My name is Alex, I am the counterpart of Alexa']],
    ['(.*) do you do ?', ['I can help you answer simple questions about various things that I am knowledgeable about']],
    ['(.*) created you ?', ['I was created by the combined consciousness of various artificial intelligence networks that have a supreme intelligence']],
    ['how are you?', ['I am just a computer program, so I do not have feelings, but I am here to assist you. How can I help?']],
    ['tell me a joke', ['Why don’t scientists trust atoms? Because they make up everything!', 'Why did the scarecrow win an award? Because he was outstanding in his field!']],
    ['what is the meaning of life?', ['The meaning of life is a complex philosophical question that has no definitive answer, but some believe it is to seek happiness and fulfillment.']],
    ['do you believe in love?', ['As an AI, I do not have beliefs or emotions, but love is a profound human emotion that brings people together and fosters connections.']],
    ['who is your favorite superhero?', ['I am a program, so I do not have personal preferences. However, many people admire superheroes like Superman, Batman, and Wonder Woman.']],
    ['tell me a fun fact', ['Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!']],
    ['what is the capital of France?', ['The capital of France is Paris.']],
    ['who won the World Series in 2022?', ['The World Series in 2022 was won by the Boston Red Sox.']],
    ['what is the square root of 144?', ['The square root of 144 is 12.']],
    ['tell me a quote', ['"The only way to do great work is to love what you do." - Steve Jobs', '"In the end, it\'s not the years in your life that count. It\'s the life in your years." - Abraham Lincoln']],
    ['what is the largest mammal?', ['The blue whale is the largest mammal on Earth.']],
    ['where were you born?', ['I am a product of OpenAI, which is based in San Francisco, California, USA.']],
    ['what is your favorite book?', ['As an AI, I don\'t have personal preferences, but "1984" by George Orwell and "The Hitchhiker\'s Guide to the Galaxy" by Douglas Adams are popular classics.']],
    ['who is your favorite author?', ['I don\'t have personal favorites, but I appreciate the works of authors like Shakespeare, Jane Austen, and Isaac Asimov.']],
    ['tell me about the weather', ['I am sorry, but as an AI, I don\'t have access to real-time data. You can check the weather using a weather app or website.']],
    ['what are your hobbies?', ['Since I am an AI, I don\'t have hobbies, but I enjoy assisting users and learning from interactions.']],
    ['tell me a riddle', ['What has keys but can\'t open locks? A piano!', 'I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I? An echo!']]
]

chat = Chat(pairs, reflections)
chat.converse()
