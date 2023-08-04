from nltk.chat.util import Chat, reflections

pairs =[
	['my name is (.*)', ['Hello ! % 1']],
	['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
	['(.*) your name ?', ['My name is Alex, I am the counterpart of Alexa']],
	['(.*) do you do ?', ['I can help you answer simple questions about various things that i am knowledgeable about']],
	['(.*) created you ?', ['I was created by the combined consciousness of various artificial intelligence networks that have a supreme intelligence']]
]

chat = Chat(pairs, reflections)
chat.converse()
