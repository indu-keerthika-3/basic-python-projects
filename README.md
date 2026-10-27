🤖 Simple Chatbot Using Python

A beginner-friendly, rule-based chatbot built with Python and the Natural Language Toolkit (NLTK). It interacts with users through a command-line interface and responds to simple messages using predefined patterns and responses.

📌 Features
👋 Responds to greetings such as hi, hello, and hey.
🤖 Introduces itself when asked for its name.
😊 Responds to questions like "How are you?"
💬 Handles simple apologies.
👋 Provides a goodbye message when the user types quit.
🔄 Uses predefined patterns and responses for conversations.
🛠️ Technologies Used
Python 3
NLTK (Natural Language Toolkit)
Regular expressions for matching user input.
NLTK Chat utilities for managing conversations.
📋 Requirements
Python 3 installed on your computer.
pip, Python's package installer.
A terminal or command prompt.
🚀 Installation and Setup
1. Clone the repository
bash
git clone https://github.com/indu-keerthika-3/Simple-Chatbot.git

2. Navigate to the project directory
bash
cd Simple-Chatbot

3. Install NLTK
bash
pip install nltk


If your system uses python3 and pip3, you can run:

bash
pip3 install nltk

▶️ How to Run

Run the Python file:

bash
python chatbot.py


Or, if required:

bash
python3 chatbot.py


Replace chatbot.py with your actual Python filename if it is different.

💬 Example Conversation
text
Hi! I'm your chatbot. Type 'quit' to exit.

> hello
Hello!

> what is your name
I am a chatbot created with Python.

> how are you
I'm doing great. How about you?

> sorry
It's okay!

> quit
Bye! Take care.


Note: The exact responses may vary because some patterns have multiple predefined responses.

🧠 How It Works
Import NLTK: Uses the Chat and reflections utilities from nltk.chat.util.
Define patterns: Stores regular expressions and their corresponding responses in a list called pairs.
Match user input: Compares messages against the predefined patterns.
Generate responses: Select
