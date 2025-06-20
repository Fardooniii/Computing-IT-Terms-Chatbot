
# Computing Terms Chatbot

Welcome! This chatbot gives simple definitions of computing terms.

## How to Use

1. Make sure Python 3 is installed.  
2. Put `chatbot.py` and `definitions.json` in the same folder.  
3. Run the chatbot with:

   ```bash
   python chatbot.py


4. When prompted, type in a computing term — it can be one word or a phrase.

5. If you want to quit, just type exit.

What’s Going On Behind the Scenes?

The chatbot reads a list of computing terms and their definitions from the definitions.json file.
When you type something, it tries to find the closest matching term using Python’s built-in difflib library, this means even if you make a small typo it still tries to understand you.
If it finds a match, it shows you the definition. If not, it kindly lets you know it couldn’t find one.

What I Learned Building This?

How to work with JSON files in Python.
How to use fuzzy matching to handle typos and guess what users mean.
Writing clean, interactive programs that take user input and respond.
The basics of building a chatbot without using any heavy AI libraries.

What I’d Like to Improve Next?

Add more definitions so it covers more topics.
Make it better at understanding full sentences or questions.
Maybe connect it to the internet for live data or updates.
Create a simple graphical interface so it’s easier to use.