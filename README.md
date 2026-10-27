🐍 Python Projects Collection

A collection of beginner-friendly Python projects demonstrating chatbot development, data analysis, and machine learning using Python libraries.

This repository contains two projects:

🤖 Simple Chatbot — A rule-based conversational chatbot using NLTK.
🏠 House Price Prediction — A machine learning project that predicts house prices using Linear Regression.
📂 Projects Overview
1. 🤖 Simple Chatbot Using Python

A basic command-line chatbot that responds to user messages using predefined patterns and responses.

Features
Responds to greetings such as hi, hello, and hey.
Introduces itself when asked for its name.
Responds to "How are you?" and simple apologies.
Displays a goodbye message when the user types quit.
Uses pattern matching and predefined responses through NLTK.
Technologies Used
Python 3
NLTK (Natural Language Toolkit)
Regular expressions
Installation

Install the required library:

bash
pip install nltk

How to Run

Navigate to the chatbot project folder and execute:

bash
python chatbot.py


Replace chatbot.py with your actual Python filename if necessary.

Example Output
text
Hi! I'm your chatbot. Type 'quit' to exit.

> hello
Hello!

> how are you
I'm doing great. How about you?

> quit
Bye! Take care.

How It Works
Defines message patterns and possible responses.
Matches user input against predefined regular expressions.
Uses NLTK's Chat utility to manage the conversation.
Continues interacting until the user exits.
2. 🏠 House Price Prediction Using Machine Learning

A simple machine learning project that predicts house prices using Linear Regression based on house area, number of bedrooms, and age.

Features
Uses sample housing data stored in a Pandas DataFrame.
Considers three input features: area, bedrooms, and age.
Splits the dataset into training and testing sets.
Trains a Linear Regression model.
Predicts prices for the test dataset.
Displays model coefficients and the intercept.
Technologies Used
Python 3
Pandas
Scikit-learn
Linear Regression
Machine Learning
Installation

Install the required libraries:

bash
pip install pandas scikit-learn

How to Run

Navigate to the house price prediction project folder and execute:

bash
python house_price_prediction.py


Replace house_price_prediction.py with your actual Python filename if necessary.

Input Features
Feature	Description
Area	House area in square units
Bedrooms	Number of bedrooms
Age	Age of the house
Price	Target variable to predict
Sample Dataset
Area	Bedrooms	Age	Price
1000	2	10	200000
1500	3	5	300000
1800	4	3	400000
2400	4	2	500000
3000	5	1	600000
How It Works
Loads the sample data into a Pandas DataFrame.
Selects Area, Bedrooms, and Age as input features.
Uses Price as the target variable.
Splits the data using train_test_split.
Trains a Linear Regression model.
Predicts prices for the test set.
Prints the predictions, model coefficients, and intercept.
Example Output
text
Predicted prices: [...]
Model Coefficients: [...]
Model Intercept: ...


Note: The actual numerical output is generated when you run the program. Since the dataset contains only five sample records, the model is intended for learning and experimentation, not reliable real-world house valuation.

🛠️ Prerequisites

Before running these projects, ensure you have:

Python 3 installed.
pip installed.
A code editor such as Visual Studio Code.
Basic knowledge of Python.

Check your Python installation:

bash
python --version

📁 Suggested Repository Structure

Keep both projects in separate folders inside one GitHub repository:

text
Python-Projects/
├── README.md
├── chatbot/
│   └── chatbot.py
└── house-price-prediction/
    └── house_price_prediction.py


Your actual Python filenames may differ. Update them in the instructions above if needed.

🚀 Future Improvements
Chatbot
Add more conversation patterns.
Improve response matching.
Build a graphical user interface.
Explore more advanced conversational models.
House Price Prediction
Use a larger, real-world housing dataset.
Evaluate the model using MAE, MSE, or R².
Add a function to predict prices for new house details.
Build a simple web interface for predictions.
👩‍💻 Author

indu-keerthika-3

GitHub: https://github.com/indu-keerthika-3

📄 License

These projects are intended for educational and personal learning purposes. Add a license file if you want to specify formal reuse and distribution permissions.

⭐ If you find these projects helpful, consider starring the repository!
