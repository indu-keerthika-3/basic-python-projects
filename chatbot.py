import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created with Python.",]
    ],
    [
        r"how are you ?",
        ["I'm doing great. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay!", "No problem!",]
    ],
    [
        r"quit",
        ["Bye! Take care.",]
    ],
]

# Create chatbot
def simple_chatbot():
    print("Hi! I'm your chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run chatbot
simple_chatbot()